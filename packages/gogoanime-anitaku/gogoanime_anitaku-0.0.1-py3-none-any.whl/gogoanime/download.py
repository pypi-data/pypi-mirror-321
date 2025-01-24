import os
import sys
import subprocess
from gogoanime import logger


def download(url, destination_file_path, workers=16, quiet=False):
    """
    Download a file from a URL using aria2c with multiple workers.
    args:
        url: The URL of the file to download.
        destination_file_path: The path to save the downloaded file.
        workers: The number of workers to use for the download.
        quiet: Whether to run aria2c in quiet mode. Nothing will be printed to the console if True.
    """

    if os.path.exists(destination_file_path) and not os.path.exists(f"{destination_file_path}.aria2"):
            if not quiet:
                logger.info(f"File already downloaded: {destination_file_path}")
            return

    command = [
        "aria2c",
        "-x", f"{workers}",
        "-s", f"{workers}",
        "-k", "1M",
        "-d", ".",
        "-o", destination_file_path,
        url
    ] # Command to download the file using aria2c

    if quiet:
        command.insert(1, "-q")

    # Run the command and get real-time updates
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Process the output in real time
    try:
        for line in process.stdout:
            if "Redirecting" not in line:
                print(line.strip(), end='\r')  # Print the output line by line
    except KeyboardInterrupt:
        process.terminate()  # Allow the user to stop the process with Ctrl+C
        # print("Download interrupted!")
        logger.error("Download interrupted!")
        process.wait()
        sys.exit(1)
    finally:
        process.wait()  # Ensure the process has finished



if __name__ == "__main__":
    url = 'https://ggredi.info/download.php?url=aHR0cHM6LyAdeqwrwedffryretgsdFrsftrsvfsfsr9odGd0c2AawehyfcghysfdsDGDYdgdsfsdfwstdgdsgtertR0cXZsLmFuZjU5OC5jb20vdXNlcjEzNDIvNTMxOGJhZDQ4YWQ2MTQ0MThhOWZlMTIwMzg5NmJjMzUvRVAuMS52MC4xNzI4MTQ1NTA2LjEwODBwLm1wND90b2tlbj1rT2thTmFoaG5nNENsMk9FckVYSDRnJmV4cGlyZXM9MTczNDI1NTY5NCZpZD0yMzQzODQmdGl0bGU9KDE5MjB4MTA4MC1nb2dvYW5pbWUpYmxlYWNoLXNlbm5lbi1rZXNzZW4taGVuLXNvdWtva3UtdGFuLWVwaXNvZGUtMS5tcDQ='
    path = "video/file2.mp4"
    download(url, path)