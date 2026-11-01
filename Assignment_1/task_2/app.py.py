
from flask import Flask, request, jsonify
import secrets

app = Flask(__name__)

# Generate unique API keys for three consumers
API_KEYS = {
    secrets.token_hex(16): "Consumer 1",
    secrets.token_hex(16): "Consumer 2",
    secrets.token_hex(16): "Consumer 3"
}

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "API Key Authentication System is running"
    })

@app.route("/keys", methods=["GET"])
def get_keys():
    return jsonify(API_KEYS)

@app.route("/process", methods=["POST"])
def process_text():

    # Get API key from request header
    api_key = request.headers.get("x-api-key")

    # Check API key
    if api_key not in API_KEYS:
        return jsonify({"error": "Invalid or missing API key"}), 401

    # Get text from request
    data = request.get_json(silent=True)

    if not data or not isinstance(data.get("text"), str) or not data["text"].strip():
        return jsonify({"error": "Please provide valid text"}), 400

    text = data["text"]

    return jsonify({
        "consumer": API_KEYS[api_key],
        "original_text": text,
        "processed_text": text.upper()
    })

if __name__ == "__main__":
    app.run(port=5001, debug=True)
