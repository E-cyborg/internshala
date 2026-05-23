from flask import (
    Flask,
    render_template,
    request,
    jsonify
)

import json
import os

from datetime import datetime

app = Flask(__name__)

os.makedirs("logs", exist_ok=True)

LOG_FILE = "logs/chat_history.json"


# -------------------
# Logs
# -------------------

def load_logs():

    if os.path.exists(LOG_FILE):

        with open(
            LOG_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    return []


def save_log(
    user_msg,
    bot_msg
):

    logs = load_logs()

    logs.append({

        "timestamp":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        "user":
            user_msg,

        "bot":
            bot_msg
    })

    with open(
        LOG_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            logs,
            f,
            ensure_ascii=False,
            indent=2
        )


# -------------------
# Bot Logic
# -------------------

def generate_response(text):

    text_lower =text.lower()


    # Greeting
    if any(
        w in text_lower
        for w in [
            "hi",
            "hello",
            "namaste"
        ]
    ):

        if "naa peru" in text_lower:

            try:

                name = (
                    text_lower
                    .split("naa peru")[1]
                    .strip()
                    .split()[0]
                )

                return (
                    f"Namaste {name.capitalize()} ji, aapko kaise help chahiye?"
                )

            except:
                pass

        return (
            "Namaste ji! Aapko kaise help chahiye?"
        )


    # Demo
    if any(
        w in text_lower
        for w in [
            "demo",
            "kavali",
            "software"
        ]
    ):

        return (
            "Sure, meeku demo schedule chestanu."
        )


    # Help
    if any(
        w in text_lower
        for w in [
            "help",
            "madad",
            "problem"
        ]
    ):

        return (
            "Bilkul! Mee problem cheppandi."
        )


    # Thanks
    if any(
        w in text_lower
        for w in [
            "thanks",
            "shukriya"
        ]
    ):

        return (
            "Shukriya ji! Meeku help cheyadam santosham."
        )


    # Bye
    if any(
        w in text_lower
        for w in [
            "bye",
            "tata"
        ]
    ):

        return (
            "Bye ji! Malli kaluddam."
        )


    return (
        "Konchem clear ga cheppandi please."
    )


# -------------------
# Routes
# -------------------

@app.route("/")
def index():

    return render_template(
        "index.html"
    )


@app.route(
    "/respond",
    methods=["POST"]
)
def respond():

    try:

        data =request.get_json()

        user_text =data.get(
                "text",
                ""
            ).strip()

        if not user_text:

            return jsonify({
                "error":
                    "No text"
            }), 400


        bot_response =generate_response(
                user_text
            )

        save_log(
            user_text,
            bot_response
        )

        return jsonify({

            "response":
                bot_response
        })


    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


@app.route("/logs")
def logs():

    return jsonify(
        load_logs()
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )