from PIL import Image

image_path = 'ya.jpg'

img = Image.open(image_path)
width, height = img.size

print(width, height)
img.show()