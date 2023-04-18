from PIL import Image
import urllib.request
import random

for i in range(1000):
    id = random.randint(1, 10e7)
    # Download the image from the URL
    url = "https://avatars.githubusercontent.com/u/"+str(id)
    print(f"Downloading {id}")
    urllib.request.urlretrieve(url, f"images/{id}.jpg")


# img = Image.open(f"images/{id}.jpg")
# img.show()

quit()
