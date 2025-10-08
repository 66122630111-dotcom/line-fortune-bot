from flask import Flask, request, jsonify
import requests, random

app = Flask(__name__)

LINE_ACCESS_TOKEN = "YOUR_CHANNEL_ACCESS_TOKEN"

def reply_message(reply_token, text):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer " + LINE_ACCESS_TOKEN
    }
    body = {
        "replyToken": reply_token,
        "messages": [{"type": "text", "text": text}]
    }
    requests.post("https://api.line.me/v2/bot/message/reply", headers=headers, json=body)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    event = data["events"][0]
    reply_token = event["replyToken"]
    user_text = event["message"]["text"]

    if user_text == "ดูดวง":
        fortunes = [
            "วันนี้คุณจะโชคดี 🍀",
            "ระวังเรื่องการเงิน 💸",
            "จะมีคนเอาข่าวดีมาให้ ✨",
            "อาจมีเรื่องให้กังวล แต่จะผ่านไปได้ 💪"
        ]
        reply_message(reply_token, random.choice(fortunes))
    else:
        reply_message(reply_token, f"คุณพิมพ์ว่า: {user_text}")

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(port=5000)
