"""Render the app's own geometric brand mark for platform packaging.

Requires Pillow only when regenerating these checked-in assets.
"""
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
navy, cream, orange = '#14333F', '#F6F5F0', '#F4A365'
image = Image.new('RGB', (1024, 1024), navy)
draw = ImageDraw.Draw(image)
draw.ellipse((160, 160, 864, 864), outline='#3E6C70', width=5)
draw.arc((265, 265, 759, 759), 45, 310, fill=cream, width=76)
draw.ellipse((708, 230, 830, 352), fill=orange)
draw.line((475, 465, 525, 515, 595, 420), fill=orange, width=25)
image.save(ROOT / 'Images' / 'app-icon.png')
image.save(ROOT / 'Images' / 'app-icon.ico', sizes=[(16, 16), (32, 32), (48, 48), (256, 256)])
presplash = Image.new('RGB', (720, 1280), navy)
mark = image.resize((360, 360), Image.Resampling.LANCZOS)
presplash.paste(mark, (180, 460))
presplash.save(ROOT / 'Images' / 'presplash.png')
print('Brand assets generated.')
