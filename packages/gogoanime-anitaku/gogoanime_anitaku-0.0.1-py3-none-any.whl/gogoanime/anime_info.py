from bs4 import BeautifulSoup
from urllib.parse import urlparse
from gogoanime import logger
import sys


class GogoanimeInfo:
    def __init__(self, url, session):
        """
        Get information about an anime from a URL.
        args:
            url: The URL of the anime.
            session: The requests session to use for the request.
        """
        self.url = url
        self.session = session
        parsed_url = urlparse(url)
        self.base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        self._get_anime_url()
        self.soup = self._get_soup()
        self._get_anime_name()
        self._get_totalNumberOfEpisodes()


    def _get_soup(self):
        """
        Get the BeautifulSoup object of the anime page.
        """
        response = self.session.get(self.url)
        if response.status_code == 404:
            response = self.session.get(self.anime_url)
            if response.status_code == 404:
                message = f"Anime not found: {self.url}"
                logger.error(message)
                sys.exit(1)
            logger.info("Anime episode number is not correct")
        return BeautifulSoup(response.text, 'html.parser')
    

    def _get_anime_name(self):
        self.anime_name = 'Not found'
        try:
            self.anime_name = self.soup.find_all('div', {'class':'anime-info'})[0].find_all('a')[0].text.strip()
        except Exception:
            self.anime_name = self.soup.find_all('div', {'class':'anime_info_body_bg'})[0].find_all('h1')[0].text.strip()

    def _get_totalNumberOfEpisodes(self):
        episode_page = self.soup.find('ul', id='episode_page')
        ep_end = 0
        if episode_page:
            a_tags = episode_page.find_all('a')
            for a_tag in a_tags:
                ep_end = a_tag.get('ep_end')

        self.totalNumberOfEpisodes = int(ep_end)


    def _get_anime_url(self):
        self.anime_url = self.url
        if 'category' not in self.url:
            self.anime_url = f"{self.base_url}/category/{self.url.split('/')[-1].split('-episode-')[0]}"
        self.epi_url = f"{self.base_url}/{self.anime_url.split('category/')[-1]}-episode-"

    def get_anime_info(self):
        self._get_totalNumberOfEpisodes()
        return {
            'anime_name': self.anime_name,
            'anime_url': self.anime_url,
            'anime_episode_url': self.epi_url,
            'base_url': self.base_url,
            'totalNumberOfEpisodes': self.totalNumberOfEpisodes
        }