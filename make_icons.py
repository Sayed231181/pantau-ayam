from PIL import Image
import os
src = Image.open('icon.png').convert('RGBA')
res = 'android/app/src/main/res'
legacy = {'mdpi': 48, 'hdpi': 72, 'xhdpi': 96, 'xxhdpi': 144, 'xxxhdpi': 192}
fore = {'mdpi': 108, 'hdpi': 162, 'xhdpi': 216, 'xxhdpi': 324, 'xxxhdpi': 432}
for d, n in legacy.items():
    p = f'{res}/mipmap-{d}'
    os.makedirs(p, exist_ok=True)
    img = src.resize((n, n), Image.LANCZOS)
    img.save(f'{p}/ic_launcher.png')
    img.save(f'{p}/ic_launcher_round.png')
for d, n in fore.items():
    p = f'{res}/mipmap-{d}'
    os.makedirs(p, exist_ok=True)
    canvas = Image.new('RGBA', (n, n), (255, 255, 255, 255))
    k = int(n * 0.66)
    logo = src.resize((k, k), Image.LANCZOS)
    canvas.paste(logo, ((n - k) // 2, (n - k) // 2))
    canvas.save(f'{p}/ic_launcher_foreground.png')
os.makedirs(f'{res}/values', exist_ok=True)
open(f'{res}/values/ic_launcher_background.xml', 'w').write(
    '<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">#FFFFFF</color>\n</resources>\n')
print('ikon selesai')
