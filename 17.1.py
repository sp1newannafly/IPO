from PIL import Image

image_path = 'W7Nker8i59Q.jpg'

img = Image.open(image_path)
width, height = img.size

print(width, height)
img.show()
