from PIL import Image, ImageDraw

triangle = Image.new('1', (400, 400))

draw = ImageDraw.Draw(triangle)
draw.polygon([20, 20, 20, 140, 60, 60], None, 'white')

triangle.save('triangle.png')
