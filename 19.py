from wand.image import Image as WandImage
from wand.color import Color
from wand.drawing import Drawing
from wand.display import display
img = WandImage(width = 300, height = 300, background = Color("white"))
draw = Drawing()
draw.stroke_color = Color ("yellow") 
draw.fill_color = Color ("yellow")
draw.ellipse ( (150, 150), (150, 150))
draw.draw (img)
display (img) 