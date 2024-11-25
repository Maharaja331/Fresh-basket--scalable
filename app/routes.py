import os
from flask import Blueprint, render_template, request, jsonify
import speech_recognition as sr

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/process_audio", methods=["POST"])
def process_audio():
    recognizer = sr.Recognizer()
    audio_file = request.files["audio"]
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return jsonify({"text": text})
        except sr.UnknownValueError:
            return jsonify({"error": "Could not understand the audio"})
