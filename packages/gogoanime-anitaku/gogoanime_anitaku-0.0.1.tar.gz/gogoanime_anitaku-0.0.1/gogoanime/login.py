import sys
import keyring
import requests
from gogoanime import logger
from gogoanime.user import get_session
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import getpass
from gogoanime.constants import APP_NAME, LOGIN_URL, BASE_URL, HEADERS

class GogoAnimeLogin:

    def __init__(self, url=BASE_URL, service_name=APP_NAME,):
        self.service_name = service_name
        self.session = requests.Session()
        parsed_url = urlparse(url)
        self.base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        self.login_url = self.base_url + LOGIN_URL

    def is_authenticated(self):
        """Check whether the user is already authenticated or not."""
        credentials = get_session(self.base_url)
        if credentials.get("user", None):
            logger.info("User " + credentials.get('user') +" is already authenticated.")
            sys.exit(0)
        return credentials.get("sessions", None)

    def save_credentials(self, auth, gogoanime):
        """Save credentials securely in the keyring."""
        keyring.set_password(self.service_name, "auth", auth)
        keyring.set_password(self.service_name, "gogoanime", gogoanime)

    def login(self):
        """Handle login. Prompt user for credentials if not saved."""
        session = self.is_authenticated()

        get_response = session.get(self.login_url)
        
        soup = BeautifulSoup(get_response.content, 'html.parser')
        csrf = soup.find("input", {"name": "_csrf"})['value']
        login_data = {
            "_csrf": csrf,
            "email": input("email: "),
            "password": getpass.getpass("password: "),
        }
        
        post_response = session.post(self.login_url, data=login_data)
        if post_response.status_code == 200:
            logger.info("Login successful.")
            self.save_credentials(session.cookies.get("auth"), session.cookies.get("gogoanime"))
        else:
            logger.error("Login failed. Please check your credentials and try again.")



    def logout(self):
        """Clear stored credentials."""
        keyring.delete_password(self.service_name, "auth")
        keyring.delete_password(self.service_name, "gogoanime")
        logger.info("Logged out and credentials cleared.")
