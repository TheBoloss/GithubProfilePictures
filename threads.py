import random
import threading
import urllib.request
from queue import Queue


def download_image(q):
    while True:
        # Get the next URL from the queue
        url, filename = q.get()

        print(f"Downloading {url}")
        # Download the image from the URL and save it to disk
        urllib.request.urlretrieve(url, filename)

        # Mark the task as done in the queue
        q.task_done()


# Set up a queue to hold the image download tasks
q = Queue()

# Start a pool of worker threads to download the images
for i in range(40):
    thread = threading.Thread(target=download_image, args=(q,))
    thread.daemon = True
    thread.start()

# Download images indefinitely
while True:
    # Generate a random user ID between 1 and 1000000
    user_id = random.randint(1, 1000000)

    # Construct the URL for the user's avatar
    url = f"https://avatars.githubusercontent.com/u/{user_id}"

    # Add the download task to the queue
    q.put((url, f"images/{user_id}.jpg"))

# Note: this script will continue downloading images indefinitely, so you may want to add a way to stop the script manually (e.g. by pressing Ctrl+C in the terminal).
