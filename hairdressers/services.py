import requests
import logging
import urllib3

logger = logging.getLogger(__name__)

# Disable SSL certificate warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_random_quote():
    url = "https://api.quotable.io/random"
    try:
        # API request with SSL verification disabled
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            data = response.json()
            logger.debug(f"API Response: {data}")
            return {
                'quote': data['content'],
                'author': data['author']
            }
        else:
            logger.error(f"Failed to fetch quote. Status Code: {response.status_code}")
            return None
    except requests.RequestException as e:
        logger.error(f"Error fetching quote: {e}")
        return None
