import sys
from PIL import Image, ImageOps

len_argv = len(sys.argv)

if len_argv < 3:
    print("Too few command-line arguments")
    sys.exit(1)

if len_argv > 3:
     print("Too many command-line arguments")
     sys.exit(1)

image_extension_formats = {".jpg", ".jpeg", ".png"}

if not all(arg.lower().endswith(tuple(image_extension_formats)) for arg in sys.argv[1:3]):
    print("Invalid input or output")
    sys.exit(1)

if sys.argv[1][-4:].lower() != sys.argv[2][-4:].lower():
    print("Input and output have different extensions")
    sys.exit(1)

try:
    input_image = Image.open(sys.argv[1])

except FileNotFoundError:
    print("Input does not exist")
    sys.exit(1)

shirt_image = Image.open("shirt.png")
size = shirt_image.size
output_image = ImageOps.fit(input_image, size)
output_image.paste(shirt_image, shirt_image)
output_image.save(sys.argv[2])

sys.exit(0)
