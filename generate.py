from google import genai
import random
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client_ai = genai.Client(api_key=GEMINI_API_KEY)

def generate_bug(language, difficulty):
    topics = ["loops", "list comprehension", "dictionaries", "math operations", "string manipulation", "file handling", "functions", "classes and objects"]
    selected_topic = random.choice(topics)

    prompt = f"""
    Generate a unique {language} code snippet on {selected_topic}.
    The code MUST contain exactly one bug (syntax or logical).
    Do NOT explain the bug.
    Do NOT add comments mentioning the bug.
    Difficulty: {difficulty}
    """

    response = client_ai.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt,
        config={
            'temperature': 0.8,
        }
    )

    if not response or not response.text:
        raise ValueError("Error during code generation.")
    
    return response.text.strip()

def evaluate_fix(buggy_code, user_code):
    prompt = f"""
    You are an expert programmer.

    BUGGY CODE:
    {buggy_code}

    USER FIX:
    {user_code}

    Answer clearly:
    Is the fix correct?
    What was the bug?
    Why does it occur?
    Best practice solution

    Talk as if you are talking to the user who submitted the fix but dont introduce or say hi, just begin answering.
    """

    response = client_ai.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    if not response or not response.text:
        raise ValueError("Error during fix evaluation.")

    return response.text