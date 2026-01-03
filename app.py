from flask import Flask, request, jsonify
from google import genai
import random
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

app = Flask(__name__)

client_ai = genai.Client(api_key=GEMINI_API_KEY)

def generate_bug(language, difficulty):
    topics = ["loops", "list comprehension", "dictionaries", "math operations", "string manipulation", "file handling", "functions", "classes and objects"]
    selected_topic = random.choice(topics)

    prompt = f"""
    You are a programming instructor.
    Generate a unique {language} code snippet on {selected_topic} and include a bug, syntax error or a logical error.
    The user will have to identify and fix the bug. Do NOT provide the solution or generate code without an error.
    Dont mention the bug in the code comments.

    Difficulty: {difficulty}

    Return EXACTLY in this format:
    BUGGY_CODE:
    """

    response = client_ai.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt,
        config={
            'temperature': 0.8,
        }
    )

    return response.text

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

    return response.text

Buggy_code = generate_bug("Python", "Easy")
Buggy_code_clean = Buggy_code.replace("BUGGY_CODE:", "").strip()
print(Buggy_code_clean)
fixed_code = input("Enter your fixed code:\n")
print(evaluate_fix(Buggy_code_clean, fixed_code))