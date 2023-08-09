from pathlib import Path
from PIL import Image

def _process_photo(path, id, x, y, width, angle, target_width, target_height):
    output_file = f'content/{path}.jpg'
    raw_image_path = Path(f'tmp/{id}.jpg')
    image = Image.open(raw_image_path)
    image = image.rotate(angle, expand=True)
    image = image.crop((x, y, x + width, y + width * target_height / target_width))
    image = image.resize((target_width, target_height))
    image.save(output_file, quality=75)

def gallery(path, id, x, y, width, angle=0):
    _process_photo(path, id, x, y, width, angle, 280, 210)

def thumbnail(path, id, x, y, width, angle=0):
    _process_photo(f'{path}thumbnail', id, x, y, width, angle, 60, 50)
