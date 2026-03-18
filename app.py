from flask import Flask, render_template, request, jsonify
from modules.entropy import calculate_entropy
from modules.dictionary_checker import dictionary_attack
from modules.breach_checker import check_breach
from modules.security_score import security_score
from utils.password_generator import generate_password
from utils.history_manager import check_password_reuse
from modules.guess_estimator import crack_time_estimate

app = Flask(__name__)


def password_strength(entropy):

    if entropy < 28:
        return "Very Weak"

    elif entropy < 36:
        return "Weak"

    elif entropy < 60:
        return "Moderate"

    elif entropy < 80:
        return "Strong"

    else:
        return "Very Strong"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["GET"])
def generate():
    password = generate_password()
    return jsonify({"password": password})


@app.route("/check", methods=["POST"])
def check():

    data = request.get_json()

    if not data or "password" not in data:
        return jsonify({"error": "Password not provided"}), 400

    password = data["password"]

    try:

        entropy = calculate_entropy(password)

        strength = password_strength(entropy)

        breach = check_breach(password)

        common = dictionary_attack(password)

        reuse = check_password_reuse(password)

        crack_time = crack_time_estimate(entropy)

        score = security_score(entropy, breach, common)

        return jsonify({

            "entropy": entropy,
            "strength": strength,
            "crack_time": crack_time,
            "breach_count": breach,
            "common_password": common,
            "reuse_detected": reuse,
            "security_score": score

        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)