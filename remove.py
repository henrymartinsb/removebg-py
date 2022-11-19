from rembg import remove
from PIL import Image


input_path = 'img.png'

output_path = 'img_sf.png'

input = Image.open(input_path)

output = remove(input)

output.save(output_path)