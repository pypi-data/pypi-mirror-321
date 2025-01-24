# Gogoanime Downloader
Download anime from [Gogoanime](https://anitaku.bz/). User must have an account on This website 

## Features
* Single episode download
* All episodes download

## Setup
```
pip install git+https://github.com/HSAkash/gogoanime.git
```
or 
```
pip install gogoanime
```

## Directories
<pre>
gogoanime/
├── gogoanime/         # Main package directory
│   ├── __init__.py    # Make it a package
│   ├── download.py 
│   ├── constants.py
│   ├── login.py
│   ├── user.py
│   ├── anime_info.py
│   ├── get_download_url.py
│   └── __main__.py    # Entry point for CLI
├── README.md          # Project description
├── LICENSE            # License file (optional)
└── pyproject.toml     # Dependencies & setup
</pre>


# Run the command
## Help command
```
gogoanime --help
```
```
usage: test.py [-h] [-s START] [-e END] [-q QUALITY] [-d DESTINATION] [--yes-playlist] [--start-episode] url

Description of program

  Download anime from Gogoanime.
  Args:
    url: URL of the anime or 'logout' for log out from the website.
    destination: Directory to save the anime.
    quality: Video quality (e.g., 720p, 1080p).
    workers: Number of workers to use.
    start_episode: Flag for starting episode URL.
    start_n: Start episode number.
    end_n: End episode number.
    yes_playlist: Flag for playlist download.
    login: Flag for user login.
    verbose: Quiet mode.

Options:
  -d, --destination TEXT  Directory to save the anime.
  -q, --quality TEXT      Video quality (e.g., 720, 1080).
  -w, --workers INTEGER   Number of workers to use.
  --start-episode         start episode url.
  -s, --start-n INTEGER   start episode number.
  -e, --end-n INTEGER     end episode number.
  --yes-playlist          For playlist download.
  --login                 For Login user.
  --verbose               Quiet.
  --help                  Show this message and exit.
```

## User Command
* Login
```
gogoanime --login <url>
```
* Logout
```
gogoanime logout
```

## Download commands
### Single
```
# auto quality 720p
gogoanime <anime_episode url>
# Example
gogoanime https://anitaku.bz/naruto-episode-1
```
```
# Give quality of video also destination where to save
gogoanime -d <forlder path> -q <quality> <url>
# Example
gogoanime -d 'anime/naruto' -q 1080 https://anitaku.bz/naruto-episode-1
```
### Playlist
* All episode download
```
gogoanime --yes-playlist <anime_url=https://anitaku.bz/naruto-episode-1>
```
* N-N episodes download
```
gogoanime -s <start_episode_number> -e <end_episode number> --yes-playlist <anime_url=https://anitaku.bz/naruto-episode-1>
```
* if given episode url is the starting position
```
gogoanime --start-episode -e <end_episode number> --yes-playlist <anime_url=https://anitaku.bz/naruto-episode-1>
```
* If end or start position not given then start position will be the 1st episode and end position will be the last episode

## <p style="padding: 8px;color:white; display:fill;background-color:#79AC78; border-radius:5px; font-size:100%"> <b>Author</b>
HSAkash
* [Linkedin](https://www.linkedin.com/in/hemel-akash/)
* [Kaggle](https://www.kaggle.com/hsakash)
* [Facebook](https://www.facebook.com/hemel.akash.7/)
