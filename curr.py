import requests

def get_bitcoin_price_in_rub():
    try:
        # URL для получения цены BTC в рублях
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCRUB"
        response = requests.get(url)
        response.raise_for_status()  # Проверяем наличие ошибок
        
        data = response.json()
        price = float(data['price'])
        return f"Текущая цена 1 биткоина: {price:.2f} рублей"
    except requests.exceptions.RequestException as e:
        return f"Ошибка при запросе данных: {e}"
    except KeyError:
        return "Ошибка при обработке данных ответа API"

if __name__ == "__main__":
    print(get_bitcoin_price_in_rub())
