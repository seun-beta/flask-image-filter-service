import os
import random
import string
from io import BytesIO, StringIO

import requests
from PIL import Image, ImageOps

module_path = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(module_path, "input_file")


def string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def process_image_url(image_url: str):

    response = requests.get(image_url)

    image = Image.open(BytesIO(response.content))
    img = ImageOps.grayscale(image)

    temp = StringIO()
    img.save(temp, format="png")

    file_name = string_generator()

    path_and_file = module_path + "/tmp/" + file_name + ".jpeg"

    img.save(fp=path_and_file, format="png")

    return path_and_file
