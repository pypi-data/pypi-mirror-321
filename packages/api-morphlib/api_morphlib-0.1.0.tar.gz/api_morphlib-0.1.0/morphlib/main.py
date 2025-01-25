# main.py

import os
import json
import logging
import signal
from typing import Any, Dict, List

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

import openai
from dotenv import load_dotenv
from tenacity import retry, wait_random_exponential, stop_after_attempt

# -------------------------------------------------------------------
# 1) Environment & Configuration
# -------------------------------------------------------------------
load_dotenv()  # Load variables from .env if present

API_KEY = os.environ.get("OPENAI_API_KEY")
API_BASE = os.environ.get("OPENAI_API_BASE", "https://api.sambanova.ai/v1")

if not API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please set it.")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

# Set up the official OpenAI client credentials
openai.api_key = API_KEY
openai.api_base = API_BASE  # If you're using Sambanova or another compatible endpoint

# -------------------------------------------------------------------
# 2) Language Mapping (from lang_code.py)
# -------------------------------------------------------------------
# Ensure "lang_code.py" is in the same package/directory
from .lang_code import unimorph_dict

# -------------------------------------------------------------------
# 3) Token Counting with tiktoken (Optional)
# -------------------------------------------------------------------
try:
    import tiktoken
    ENCODER = tiktoken.get_encoding("cl100k_base")  # Common GPT-like encoder
except ImportError:
    logger.warning("tiktoken not installed. Falling back to naive token counting.")
    ENCODER = None

def get_num_tokens(text: str) -> int:
    """
    Use tiktoken if available, else fallback to whitespace-based counting.
    """
    if ENCODER:
        return len(ENCODER.encode(text))
    return len(text.split())

def chunk_text_by_tokens(text: str, max_tokens: int) -> List[str]:
    """
    Split the text into multiple chunks not exceeding 'max_tokens' each.
    """
    if ENCODER:
        tokens = ENCODER.encode(text)
        chunks = []
        current_tokens = []

        for token in tokens:
            if len(current_tokens) + 1 > max_tokens:
                chunks.append(ENCODER.decode(current_tokens))
                current_tokens = [token]
            else:
                current_tokens.append(token)
        if current_tokens:
            chunks.append(ENCODER.decode(current_tokens))
        return chunks
    else:
        # Naive fallback using whitespace
        words = text.split()
        chunks = []
        current_chunk = []
        for word in words:
            if len(current_chunk) + 1 > max_tokens:
                chunks.append(" ".join(current_chunk))
                current_chunk = [word]
            else:
                current_chunk.append(word)
        if current_chunk:
            chunks.append(" ".join(current_chunk))
        return chunks

# -------------------------------------------------------------------
# 4) Playwright-based Wiktionary Loader with signal-based timeout
# -------------------------------------------------------------------
from langchain_community.document_loaders import PlaywrightURLLoader

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException("Timeout reached while loading page via Playwright.")

def fetch_wiktionary_page_playwright(word: str) -> str:
    """
    Loads the Wiktionary page for the given word using Playwright.
    Returns rendered text or an empty string if load fails.
    """
    lower_word = word.lower()
    url = f"https://en.wiktionary.org/wiki/{lower_word}"

    loader = PlaywrightURLLoader(
        urls=[url],
        remove_selectors=["style", "script"]
    )

    try:
        docs = loader.load()
        if not docs:
            logger.warning(f"No docs returned for {url}")
            return ""
        return docs[0].page_content
    except Exception as e:
        logger.error(f"Error loading page with Playwright: {e}")
        return ""

# -------------------------------------------------------------------
# 5) Extract Morphology from Wiktionary Chunks
# -------------------------------------------------------------------
@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def extract_morphology_from_wiktionary(content: str, word: str, pos: str, lang_name: str) -> str:
    """
    Uses 'Meta-Llama-3.3-70B-Instruct' to parse the chunk content for morphological data.
    Returns raw JSON-like text or an empty string if nothing found.
    """
    prompt_text = f"""
You are a linguistics expert. Extract morphological details for the word "{word}"
(part of speech: "{pos}") from the text below, focusing ONLY on the language "{lang_name}". 

Return the information as valid JSON (object or array). 
If nothing is found, return an empty JSON object: {{}}.

Content:
{content}
"""

    try:
        response = openai.ChatCompletion.create(
            model="Meta-Llama-3.3-70B-Instruct",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt_text},
            ],
            temperature=0.1,
            top_p=0.1
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"Extraction from Wiktionary failed: {e}")
        return ""

# -------------------------------------------------------------------
# 5B) Direct Model Fallback (if Wiktionary is empty)
# -------------------------------------------------------------------
@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def generate_morphology_fallback(word: str, pos: str, lang_name: str) -> str:
    """
    If Wiktionary yields no data, generate morphological details from the model alone.
    Returns JSON or an empty string if unknown.
    """
    prompt_text = f"""
You are a linguistics expert. The user found no morphological data for the word "{word}"
(part of speech: "{pos}") in language "{lang_name}" from Wiktionary.

Generate morphological details from your knowledge. Return it as valid JSON.
If nothing is known, return an empty JSON object: {{}}
"""

    try:
        response = openai.ChatCompletion.create(
            model="Meta-Llama-3.3-70B-Instruct",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt_text},
            ],
            temperature=0.3,
            top_p=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"Fallback generation failed: {e}")
        return ""

# -------------------------------------------------------------------
# 6) JSON Cleaning & Parsing
# -------------------------------------------------------------------
import re

def extract_json_from_response(text: str) -> str:
    """
    Attempt to find the FIRST '{...}' or '[...]' block in the text.
    Returns '{}' if no JSON is found.
    """
    match = re.search(r'(\{.*\}|\[.*\])', text, re.DOTALL)
    return match.group(0) if match else "{}"

def safe_parse_json_with_retries(json_str: str) -> Any:
    """
    Try to parse the JSON string, removing trailing chars if needed.
    Returns {} or [] if all fails.
    """
    for i in range(len(json_str), 0, -1):
        sub_str = json_str[:i]
        try:
            return json.loads(sub_str)
        except json.JSONDecodeError:
            continue
    return {}

def combine_json_objects(base: Dict[str, Any], new_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge two JSON objects, giving priority to 'base' but filling missing keys from 'new_data'.
    If both have the same key and are dict, merge recursively.
    If both have the same key and are lists or scalars, we keep 'base'.
    """
    for key, val in new_data.items():
        if key not in base:
            base[key] = val
        else:
            if isinstance(base[key], dict) and isinstance(val, dict):
                base[key] = combine_json_objects(base[key], val)
            # If base is a list or scalar, we keep base's version
    return base

# -------------------------------------------------------------------
# 7) Merge Wiktionary + Model Additional Data
# -------------------------------------------------------------------
def find_missing_keys(data: Dict[str, Any], all_keys: List[str]) -> List[str]:
    """
    Return a list of top-level keys that are missing or empty in 'data'.
    """
    missing = []
    for k in all_keys:
        if k not in data or not data[k]:
            missing.append(k)
    return missing

def fetch_additional_morphology(word: str, pos: str, lang_name: str, keys_needed: List[str]) -> Dict[str, Any]:
    """
    Queries the model for the specified missing morphological keys
    and returns them as a JSON object.
    """
    if not keys_needed:
        return {}
    prompt_text = f"""
You are a linguistics expert. We have partial morphological data for the word "{word}"
(part of speech: "{pos}") in language "{lang_name}".

We still need the following missing morphological keys:
{', '.join(keys_needed)}

Return them as valid JSON. If not found, return an empty JSON object.
"""
    try:
        response = openai.ChatCompletion.create(
            model="Meta-Llama-3.3-70B-Instruct",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt_text},
            ],
            temperature=0.3,
            top_p=0.3
        )
        raw_output = response.choices[0].message.content
        extracted = extract_json_from_response(raw_output)
        return safe_parse_json_with_retries(extracted)
    except Exception as e:
        logger.error(f"Error fetching additional morphology: {e}")
        return {}

# -------------------------------------------------------------------
# 8) Core Processing Function
# -------------------------------------------------------------------
def process_morphology(word: str, part_of_speech: str, lang_code: str) -> Dict[str, Any]:
    """
    Core logic to fetch morphological data from Wiktionary, then combine with
    fallback or additional model data. Returns a dictionary of morphological details.
    """

    # Validate language code
    language_name = unimorph_dict.get(lang_code)
    if not language_name:
        logger.error(f"Language code '{lang_code}' not found in unimorph_dict.")
        raise ValueError(f"Language code '{lang_code}' not found.")

    # Step A) Fetch Wiktionary content
    logger.info(f"Fetching Wiktionary page for '{word}'...")
    page_text = fetch_wiktionary_page_playwright(word)
    if not page_text:
        logger.warning("No Wiktionary data found or an error occurred while loading the page.")
        page_text = ""

    # Step B) Break into chunks if large
    total_tokens = get_num_tokens(page_text)
    logger.info(f"Approximate token count: {total_tokens}")
    MAX_TOKENS_PER_CHUNK = 3000

    if total_tokens > MAX_TOKENS_PER_CHUNK:
        logger.info(f"Text exceeds {MAX_TOKENS_PER_CHUNK} tokens, chunking it.")
        chunks = chunk_text_by_tokens(page_text, MAX_TOKENS_PER_CHUNK)
    else:
        chunks = [page_text]

    # Step C) Extract from Wiktionary chunks
    final_data = {}
    got_any_data = False
    for i, chunk in enumerate(chunks, start=1):
        logger.info(f"Extracting morphology from chunk {i}/{len(chunks)}...")
        raw_json_like = extract_morphology_from_wiktionary(chunk, word, part_of_speech, language_name)
        extracted_str = extract_json_from_response(raw_json_like)
        parsed = safe_parse_json_with_retries(extracted_str)

        # If parsing yields a dict or list, try to combine into final_data
        if parsed and parsed != {} and parsed != []:
            got_any_data = True
            if isinstance(parsed, dict):
                final_data = combine_json_objects(final_data, parsed)
            elif isinstance(parsed, list):
                # If we get a list, store it or combine it under a single key
                final_data = combine_json_objects(final_data, {"data_list": parsed})

    # Step D) If Wiktionary data is empty, do a full fallback generation
    if not got_any_data:
        logger.info("No morphological data from Wiktionary. Falling back to direct generation.")
        fallback_raw = generate_morphology_fallback(word, part_of_speech, language_name)
        fallback_extracted = extract_json_from_response(fallback_raw)
        final_data = safe_parse_json_with_retries(fallback_extracted)

    # Step E) Fill in missing top-level keys
    expected_keys = [
        "part_of_speech",
        "plural_form",
        "declension",
        "possessive_forms",
        "morphological_components",
        "gender",
        "case",
        "number"
    ]
    missing_keys = find_missing_keys(final_data, expected_keys)
    if missing_keys:
        logger.info(f"Missing keys: {missing_keys}. Querying model for additional data.")
        addition_raw = fetch_additional_morphology(word, part_of_speech, language_name, missing_keys)
        final_data = combine_json_objects(final_data, addition_raw)

    logger.info("=== COMBINED JSON OUTPUT ===")
    return final_data

# -------------------------------------------------------------------
# 9) FastAPI Endpoint
# -------------------------------------------------------------------
app = FastAPI()

class MorphologyRequest(BaseModel):
    word: str
    part_of_speech: str
    lang_code: str

@app.post("/morphology")
def get_morphology(data: MorphologyRequest):
    """
    POST endpoint that processes morphological data.
    Expects JSON with keys: "word", "part_of_speech", and "lang_code".
    """
    try:
        result = process_morphology(data.word, data.part_of_speech, data.lang_code)
        return JSONResponse(content=result, status_code=200)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
