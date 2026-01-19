from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import random
import json
import hashlib

app = Flask(__name__)
CORS(app)  # allows cross-origin requests

# Load messages once when app starts
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "score_message.json"), "r") as f:
    SCORE_MESSAGES = json.load(f)


def calculate_score(name1, name2):
    combined = (name1 + name2).lower().replace(" ", "")
    hash_val = int(hashlib.md5(combined.encode()).hexdigest(), 16)

    # Always return score between 46–100
    return 46 + (hash_val % 55)

def get_msg(score):
    for range_key, messages in SCORE_MESSAGES.items():
        low, high=map(int,range_key.split('-'))
        if low <=score <= high:
            return random.choice(messages)
    return "A special friendship 💕"


@app.route('/api/friendship', methods=['POST'])
def friendship():
    data = request.get_json()
    name1 = data.get('name1')
    name2 = data.get('name2')

    if not name1 or not name2:
        return jsonify({"error": "Both names are required!"}), 400

    # Example: Calculate friendship score (random for demo)
    score = calculate_score(name1,name2)

    # Example message
    message = get_msg(score)

    return jsonify({
        "score": score,
        "message": message
    })

if __name__ == '__main__':
    app.run(debug=True)
