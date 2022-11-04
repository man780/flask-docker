"""Flask main page"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def home():
    """Home page"""
    return jsonify(message="Hello World!")


@app.route("/health_check")
def health_check():
    """Health Check"""
    return jsonify(success=True)
