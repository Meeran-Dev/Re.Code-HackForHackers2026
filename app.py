from flask import Flask, request, jsonify, render_template
from generate import generate_bug, evaluate_fix
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate-bug", methods=["POST"])
def generate_bug_api():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    language = data.get("language", "Python")
    difficulty = data.get("difficulty", "Easy")

    try:
        code = generate_bug(language, difficulty)
        return jsonify({
            "status": "success",
            "buggy_code": code
        })
    except Exception as e:
        print("Error during bug generation:", str(e))
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@app.route("/evaluate-fix", methods=["POST"])
def evaluate_fix_api():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    buggy_code = data.get("buggy_code")
    user_code = data.get("user_code")

    if not buggy_code or not user_code:
        return jsonify({
            "status": "error",
            "message": "Buggy code and user code are required."
        }), 400

    try:
        feedback = evaluate_fix(buggy_code, user_code)
        return jsonify({
            "status": "success",
            "feedback": feedback
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)