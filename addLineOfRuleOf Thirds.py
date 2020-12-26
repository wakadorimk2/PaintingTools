import sys
from PIL import Image, ImageDraw
filename = sys.argv[1]
ext = filename.split('.')[-1]
img = Image.open(filename)
draw = ImageDraw.Draw(img)

# draw vertical lines
sAxis = (img.width // 3, 0)
eAxis = (img.width // 3, img.height)
draw.line([sAxis, eAxis], fill=128)

sAxis = (img.width // 3 * 2, 0)
eAxis = (img.width // 3 * 2, img.height)
draw.line([sAxis, eAxis], fill=128)

# draw horizontal lines
sAxis = (0, img.height // 3)
eAxis = (img.width, img.height // 3)
draw.line([sAxis, eAxis], fill=128)

sAxis = (0, img.height // 3 * 2)
eAxis = (img.width, img.height // 3 * 2)
draw.line([sAxis, eAxis], fill=128)

img.save(f'{filename}_with_Line.{ext}')