import os
import random
import openai
import nltk
import requests
from dotenv import load_dotenv
from nltk.tokenize.punkt import PunktSentenceTokenizer

# Ensure nltk can find your local download
nltk.data.path.append("D:/unlinguist/nltk_data")

# Load environment variables
load_dotenv()

# OpenRouter (GPT) setup
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

# LibreTranslate Docker endpoint
LIBRETRANSLATE_URL = "http://localhost:5080/translate"

# Languages supported
target_langs = ["fr", "de", "it", "es", "pt", "ru", "zh-Hans"]

# Ensure punkt is available
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt", download_dir="D:/unlinguist/nltk_data")

# Initialize sentence tokenizer
sentence_tokenizer = PunktSentenceTokenizer()

# === GPT Response ===
def generate_response(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200,
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"[OpenRouter Error] {str(e)}"

# === LibreTranslate ===
def libre_translate(text: str, source: str, target: str) -> str:
    payload = {
        "q": text,
        "source": source,
        "target": target,
        "format": "text"
    }
    try:
        response = requests.post(LIBRETRANSLATE_URL, json=payload)
        response.raise_for_status()
        return response.json()["translatedText"]
    except requests.RequestException as e:
        return f"[LibreTranslate Error] {str(e)}"

# === Absurd Multilingual Translation ===
def jumble_translate(text: str) -> str:
    try:
        sentences = sentence_tokenizer.tokenize(text)
        jumbled = []
        for sentence in sentences:
            target = random.choice([lang for lang in target_langs if lang != "en"])
            translated = libre_translate(sentence, source="en", target=target)
            jumbled.append(translated)
        return " ".join(jumbled)
    except Exception as e:
        return f"[Translation Error] {str(e)}"

# === Additive Random Shift Cipher ===
def additive_shift_cipher(text: str):
    """
    Encrypts text with a random shift for each letter (A=0,...Z=25).
    Returns (ciphertext, shifts_list)
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = text.upper()
    ciphertext = ""
    shifts = []

    for char in text:
        if char.isalpha():
            shift = random.randint(1, 25)
            shifts.append(shift)
            idx = alphabet.index(char)
            new_char = alphabet[(idx + shift) % 26]
            ciphertext += new_char
        else:
            ciphertext += char
            shifts.append(None)  # No shift for non-letters

    return ciphertext, shifts

def cipher_clue(shifts):
    """
    Returns a clue string for the shifts so the user can decrypt.
    """
    return "Shifts: " + " ".join(str(s) if s is not None else "_" for s in shifts)
