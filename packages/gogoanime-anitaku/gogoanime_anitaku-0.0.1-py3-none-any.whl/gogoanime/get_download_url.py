from bs4 import BeautifulSoup
import requests
import os
import sys
from gogoanime import logger
import time


class GogoanimeUrls:
    def __init__(self, anime_info, session, quality):
        self.anime_info = anime_info
        self.session = session
        self.quality = quality

    def _get_soup(self):
        """
        Get the BeautifulSoup object of the anime page.
        """
        response = self.session.get(self.current_url)
        try:
            response.raise_for_status()
        except Exception as e:
            message = f"Episode Page not found: {self.current_url}"
            logger.error(message)
            message = 'Give the exact episode url with -se or --start-episode flag'
            logger.error(message)
            sys.exit(1)
        return BeautifulSoup(response.text, 'html.parser')
    
    
    def get_download_link_dict(self):
        """
        Get all download links quality wise.
        """
        link_dict = {}

        try:
            links = self.soup.find_all('div', class_='list_dowload')[0].find_all('a')
        except IndexError:
            return link_dict
        for link in links:
            key = link.text.strip().split('x')[-1]
            link_dict[key] = link['href']
        return link_dict
    
    def get_download_url(self, link_dict, quality='1080'):
        if quality not in link_dict:
            """
            if quality not found, then get the last quality means the highest quality.
            Args:
                link_dict (dictionary): {'quality': url}
                quality (str): 720,1080 ...
            """
            keys = link_dict.keys()
            if keys:
                quality = list(keys)[-1]
            else:
                quality = None
        if quality:
            link = link_dict[quality]
            response = requests.head(link)
            if response.headers.get('Location'):
                res = requests.head(response.headers.get('Location'))
                if res.headers.get('Content-Type') == 'video/mp4':
                    return response.headers.get('Location') , quality
        return None, None
    
    def get_next_episode_url(self):
        next_url = None
        try:
            next_url = self.soup.find_all('div', class_='anime_video_body_episodes_r')[0].find_all('a')[0]['href']
            next_url = f"{self.anime_info.get('base_url')}{next_url}"
        except Exception as e:
            pass
        return next_url
        
    def get_url(self, gogoanimeUrl, fileName=None, quality='1080', destination=None):
        # authenicate user send request to gogoanime and get all download links
        self.current_url = gogoanimeUrl
        self.quality = quality

        for i in range(10):
            self.soup = self._get_soup()
            # get download link dict
            link_dict = self.get_download_link_dict()
            # get download url
            url, quality = self.get_download_url(link_dict, self.quality)
            if not url:
                message = f"Error retrying {i+1}. Going to sleep for 10 seconds"
                logger.info(message)
                time.sleep(10)
                continue
            if fileName is None:
                fileName = gogoanimeUrl.split("/")[-1]
                file_extension = url.split('.')[-1]
                fileName = f"{fileName}-{quality}.{file_extension}"
            if destination:
                fileName = os.path.join(destination, fileName)
            
            return (url, self.get_next_episode_url(), fileName)
        
        message = f"Failed to download the video after {10*10}s retries"
        logger.error(message)
        sys.exit(1)