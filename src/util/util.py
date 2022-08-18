from PIL import Image
import requests
from io import BytesIO


def process_image_url(image_url: str):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.convert("L")

    return img
