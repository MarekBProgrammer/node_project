"""
Emotion Detection Web Application using Flask and Watson NLP.

This module provides a Flask web application for analyzing emotions in text
using IBM Watson Natural Language Processing (NLP) API.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the main HTML page with the emotion detector interface."""
    return render_template('index.html')


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    Analyze emotion in the provided text using Watson NLP.

    Returns:
        str: Formatted response with emotion scores and dominant emotion,
             or error message if text is invalid.
    """
    input_text = request.args.get("textToAnalyze")

    # Check if text was provided
    if not input_text or input_text.strip() == "":
        return "Nieprawidłowy tekst! Spróbuj ponownie!"

    # Call emotion detection function
    result = emotion_detector(input_text)

    # Handle error when dominant_emotion is None
    if result['dominant_emotion'] is None:
        return "Nieprawidłowy tekst! Spróbuj ponownie!"

    # Format the response
    response_text = (
        f"Dla danego zdania, odpowiedź systemu to "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} oraz "
        f"'sadness': {result['sadness']}. "
        f"Dominującą emocją jest {result['dominant_emotion']}."
    )

    return response_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
