# Re.Code - HackForHackers2026

A Flask web application that generates buggy code snippets in various programming languages and evaluates user-submitted fixes using Google Gemini AI.

## Features

- Generate buggy code in multiple languages: Python, JavaScript, Java, C++, Ruby, Go, C#, C, PHP, Swift
- Select difficulty levels: Easy, Medium, Hard
- Submit your fixed code and get AI-powered feedback on correctness, the bug, and best practices

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/Meeran-Dev/Re.Code-HackForHackers2026.git
   cd Re.Code-HackForHackers2026
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your Google Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

## Running the Application

1. Run the Flask app:
   ```
   python app.py
   ```

2. Open your browser and go to `http://localhost:5000`
