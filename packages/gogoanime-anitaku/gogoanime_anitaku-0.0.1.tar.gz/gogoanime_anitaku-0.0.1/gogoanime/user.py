from bs4 import BeautifulSoup
from gogoanime.constants import HEADERS, APP_NAME
import keyring
import requests


def get_credentials(service_name=APP_NAME):
    """Retrieve saved credentials from the keyring."""
    auth = keyring.get_password(service_name, "auth")
    gogoanime = keyring.get_password(service_name, "gogoanime")
    return auth, gogoanime


def get_session(url):
    """Get session object with saved credentials."""
    auth, gogoanime = get_credentials()
    sessions = requests.Session()
    sessions.headers.update(HEADERS)
    credentials = {
        "sessions": sessions
    }
    if auth and gogoanime:
        sessions.cookies.set("auth", auth)
        sessions.cookies.set("gogoanime", gogoanime)
        res = sessions.get(url)
        bs4_object = BeautifulSoup(res.content, 'html.parser')
        user = bs4_object.find_all('a', class_='account')

        credentials["sessions"] = sessions
        if user:
            credentials['user'] = user[0].text.split()[0]
        else:
            pass
    return credentials
