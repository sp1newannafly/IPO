from wand.image import Image as WandImage
from wand.drawing import Drawing
from wand.color import Color
from wand.display import display
img = WandImage(width = 400, height = 300, background = Color("white"))
draw = Drawing()
draw.stroke_color = Color ("black")
draw.point(100,200)
draw.draw(img)
display (img) 
draw.stroke_color = Color ("blue")
draw.line ((0, 0), (400, 300))
draw.draw(img)
display (img)