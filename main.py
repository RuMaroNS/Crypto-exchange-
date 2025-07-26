import requests
import json

def get_chat_id(bot_token, user_tag):
    # Мы не можем получить chat_id по usertag напрямую.
    # Нужно, чтобы пользователь взаимодействовал с ботом, например, отправив сообщение.

    # URL для получения обновлений
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get("ok"):
            # Ищем chat_id среди всех обновлений
            for update in data["result"]:
                if "message" in update:
                    user = update["message"]["from"]
                    if user["username"] == user_tag:
                        return update["message"]["chat"]["id"]
        else:
            print("Ошибка в ответе Telegram API:", data)
    else:
        print("Ошибка при запросе chat_id:", response.text)

    return None

def send_message(user_tag, card_number, summ, bot_token, transaction_id):
    # Получаем chat_id пользователя
    chat_id = get_chat_id(bot_token, user_tag)
    if not chat_id:
        print("Не удалось получить chat_id пользователя")
        return

    # URL для отправки сообщения
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    # Формируем текст сообщения
    text = f"Карта: {card_number}\nСумма: {summ}"

    # Inline кнопка
    reply_markup = {
        "inline_keyboard": [
            [
                {
                    "text": "Accept",
                    "callback_data": f"accept_{transaction_id}"
                }
            ]
        ]
    }

    # Отправляем запрос к API Telegram
    response = requests.post(url, json={
        "chat_id": chat_id,
        "text": text,
        "reply_markup": reply_markup
    })

    # Проверяем ответ
    if response.status_code == 200:
        print("Сообщение успешно отправлено")
    else:
        print("Ошибка при отправке сообщения:", response.text)

# Пример вызова функции
send_message(
    user_tag="F1owerGG",
    card_number="4990 5678 9012 3456",
    summ="1000 RUB",
    bot_token="8031219703:AAEGc-sX9uiJqcWH_TP9L_mlPF2BzXcNk1A",
    transaction_id="txn_123456"
)
