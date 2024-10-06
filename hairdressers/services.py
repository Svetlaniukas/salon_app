import requests
import logging

logger = logging.getLogger(__name__)

def get_random_quote():
    url = "https://zenquotes.io/api/random"
    try:
        # Отправляем запрос к новому API
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()[0]  # Ответ возвращает список с одной цитатой
            return {
                'quote': data['q'],  # 'q' — это сама цитата
                'author': data['a']  # 'a' — это автор
            }
        else:
            logger.error(f"Failed to fetch quote. Status Code: {response.status_code}")
            return {
                'quote': "This is a fallback quote because the API is unavailable.",
                'author': "System"
            }
    except requests.RequestException as e:
        logger.error(f"Error fetching quote: {e}")
        return {
            'quote': "This is a fallback quote because the API is unavailable.",
            'author': "System"
        }
