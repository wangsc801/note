from PIL import Image, ImageDraw

image = Image.new('RGB', (300, 300))
draw = ImageDraw.Draw(image)
draw.rectangle([60, 60, 120, 120], fill='blue')
image.save('draw_a_blue_rectangle.png')
image.close()
