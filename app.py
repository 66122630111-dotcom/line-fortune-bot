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
