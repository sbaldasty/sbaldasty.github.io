import requests

from pathlib import Path
from PIL import Image

TARGET_WIDTH = 280
TARGET_HEIGHT = 210

def google_photo(path, id, x, y, width, angle=0):
    output_file = f'content/{path}.jpg'
    print(output_file)

    raw_image_path = Path(f'tmp/{id}.jpg')
    if not raw_image_path.is_file():
        url = f'https://lh3.googleusercontent.com/{id}=d-rw-no'
        response = requests.get(url)
        if response.status_code == 200:
            print('* Downloaded')
            with open(raw_image_path, 'wb') as f:
                f.write(response.content)
        else:
            print(f'* Download failed: status code {response.status_code}')

    image = Image.open(raw_image_path)
    image = image.rotate(angle, expand=True)
    image = image.crop((x, y, x + width, y + width * TARGET_HEIGHT / TARGET_WIDTH))
    image = image.resize((TARGET_WIDTH, TARGET_HEIGHT))
    image.save(output_file, quality=75)
