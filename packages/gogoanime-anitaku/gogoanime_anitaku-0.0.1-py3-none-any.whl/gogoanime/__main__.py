import os
import sys
import click
import requests
from tqdm import tqdm
from gogoanime.download import download
from gogoanime.login import GogoAnimeLogin
from gogoanime.user import get_session
from gogoanime import logger
from gogoanime.anime_info import GogoanimeInfo
from gogoanime.get_download_url import GogoanimeUrls



@click.command()
@click.argument('url', required=True)
@click.option('--destination', '-d', type=str, help='Directory to save the anime.')
@click.option('--quality', '-q', type=str, default='720', help='Video quality (e.g., 720, 1080).')
@click.option('--workers', '-w', type=int, default=16, help='Number of workers to use.')
@click.option('--start-episode', is_flag=True, help='start episode url.')
@click.option('--start-n', '-s', type=int, default=1, help='start episode number.')
@click.option('--end-n', '-e', type=int, help='end episode number.')
@click.option('--yes-playlist', is_flag=True, help='For playlist download.')
@click.option('--login', is_flag=True, help='For Login user.')
@click.option('--verbose', is_flag=True, help='If this is true then download information will no longer be printed.')



def main(
    url,
    destination,
    quality,
    workers,
    start_episode,
    start_n,
    end_n,
    yes_playlist,
    login,
    verbose
):
    """
    Download anime from Gogoanime.
    Args:
        url: URL of the anime or 'logout' to log out from the website.
        destination: Directory to save the anime.
        quality: Video quality (e.g., 720p, 1080p).
        workers: Number of workers to use.
        start_episode: Flag for starting episode URL.
        start_n: Start episode number.
        end_n: End episode number.
        yes_playlist: Flag for playlist download.
        login: Flag for user login.
        verbose: If this is true then download information will no longer be printed.
    """
    try:
        if url.startswith('https://'):
            # If user wants to login, do it before downloading
            if login:
                login = GogoAnimeLogin(url)
                login.login()
                sys.exit(0)

            # GET user credentials
            credentials = get_session(url)
            sessions = credentials.get('sessions', None)
            user = credentials.get('user', None)
            if not user:
                logger.error("User not found. Please login first.")
                sys.exit(1)

            # get anime info
            anime_info_obj = GogoanimeInfo(url, sessions)
            anime_info = anime_info_obj.get_anime_info()
            print(f"""\n\n############### Anime Info ###############""")
            for key in anime_info:
                print(f"{key}: {anime_info[key]}")
            print(f"""############### Anime Info ###############\n\n""")

            # get download urls
            urls_obj = GogoanimeUrls(anime_info, sessions, quality)

            # set current episode url
            current_epi_url = url
            if not start_episode and yes_playlist:
                current_epi_url = f'{anime_info.get("anime_episode_url")}{start_n}'
            
            

            # set destination folder    
            if not destination:
                destination = anime_info.get('anime_name','anime_name').replace(' ', '_')
            
            

            if yes_playlist:
                if not end_n:
                    end_n = int(anime_info.get('totalNumberOfEpisodes'))

                if start_episode:
                    start_n = int(current_epi_url.split(anime_info.get("anime_episode_url"))[-1].split('-')[0])

                pbar = tqdm(total=end_n, unit="B", initial=start_n-1, unit_scale=True)
                while True:
                    video_url, next_api_url, FileName = urls_obj.get_url(
                        current_epi_url,
                        quality=quality,
                        destination=destination
                    )
                    if not verbose:
                        logger.info(f"Downloading {FileName}...")
                    download(video_url, FileName, workers=workers, quiet=verbose)
                    if not verbose:
                        logger.info(f"Download complete!")

                    flag, update_index = is_end_episode_updateIndex(current_epi_url, end_n, anime_info.get("anime_episode_url"))

                    pbar.update(update_index)
                    if not next_api_url or flag:
                        logger.info("Download completed successfully")
                        break
                    current_epi_url = next_api_url
                
            else:
                video_url, next_api_url, FileName = urls_obj.get_url(
                    current_epi_url,
                    quality=quality,
                    destination=destination
                )
                if not verbose:
                    logger.info(f"Downloading {FileName}...")
                download(video_url, FileName, workers=workers, quiet=verbose)
                if not verbose:
                    logger.info(f"Download complete!")






        elif url == 'logout':
            login = GogoAnimeLogin()
            login.logout()
            sys.exit(0)
        else:
            logger.error("Invalid URL, please provide a valid gogoanime URL.")
            sys.exit(1)

    except requests.exceptions.ConnectionError :
        # or HTTPSConnectionPool
        logger.error("Failed to connect to the internet.")
        sys.exit(1)


def is_end_episode_updateIndex(url, end_n, anime_epi_url):
    """Check if the episode number is greater than or equal to the end episode number."""
    flag = False
    url_ends = list(map(float, [x for x in url.split(anime_epi_url)[-1].split('-') if len(x) > 0]))
    update_index = int(url_ends[-1]-url_ends[0] + 1)
    if len(url_ends)==1 and int(url_ends[0])!=url_ends[0]:
        update_index = 0
    if end_n == url_ends[-1] or end_n < url_ends[-1]:
        flag = True
    return flag, update_index
    

if __name__ == "__main__":
    # Ensure Click executes the `main()` function with the CLI arguments
    main()
