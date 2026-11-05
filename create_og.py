import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 630

# 1. Warm ivory parchment background (matching oklch 97.8% .016 96 ~ #fdfaf2)
base = Image.new('RGBA', (W, H), (252, 249, 242, 255))

# 2. Blend paper texture
try:
    tex = Image.open('editable/assets/paper-texture.jpg').convert('RGBA')
    tex = tex.resize((W, H), Image.Resampling.LANCZOS)
    base = Image.blend(base, tex, 0.22)
except Exception as e:
    print('Paper texture note:', e)

# 3. Add soft golden aurora glows
glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
g_draw = ImageDraw.Draw(glow)
g_draw.ellipse([200, 50, 1000, 580], fill=(212, 175, 55, 35))
glow = glow.filter(ImageFilter.GaussianBlur(80))
base = Image.alpha_composite(base, glow)

# 4. Add floral corners
try:
    corner = Image.open('editable/assets/floral-corner.png').convert('RGBA')
    # Top-left corner
    c_tl = corner.resize((260, 260), Image.Resampling.LANCZOS)
    base.paste(c_tl, (-20, -20), c_tl)

    # Bottom-right corner (flipped x and y)
    c_br = c_tl.transpose(Image.Transpose.ROTATE_180)
    base.paste(c_br, (W - 240, H - 240), c_br)
except Exception as e:
    print('Corner note:', e)

# 5. Double gold border with corner accents
draw = ImageDraw.Draw(base)
border_gold = (184, 142, 47, 210)
border_light = (212, 175, 55, 120)

draw.rectangle([28, 28, W - 28, H - 28], outline=border_gold, width=2)
draw.rectangle([36, 36, W - 36, H - 36], outline=border_light, width=1)

# Corner dot rosettes
for cx, cy in [(28, 28), (W - 28, 28), (28, H - 28), (W - 28, H - 28)]:
    draw.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=border_gold)

# 6. Add gold flourish decorative divider
try:
    flourish = Image.open('editable/assets/gold-flourish.png').convert('RGBA')
    flourish = flourish.resize((200, 100), Image.Resampling.LANCZOS)
    flourish_x = (W - 200) // 2
    base.paste(flourish, (flourish_x, 48), flourish)
except Exception as e:
    print('Flourish note:', e)

# 7. Typography
# System fonts: Georgia, Arial, Nirmala, Amiri (if available)
f_bismillah = None
for p in ['C:/Windows/Fonts/Nirmala.ttc', 'C:/Windows/Fonts/arial.ttf', 'C:/Windows/Fonts/times.ttf']:
    if os.path.exists(p):
        try:
            f_bismillah = ImageFont.truetype(p, 26)
            break
        except Exception:
            pass

f_eyebrow = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 13)
f_title = ImageFont.truetype('C:/Windows/Fonts/georgiab.ttf', 44)
f_script = None
for p in ['C:/Windows/Fonts/georgia.ttf', 'C:/Windows/Fonts/times.ttf']:
    if os.path.exists(p):
        try:
            f_script = ImageFont.truetype(p, 36)
            break
        except Exception:
            pass
f_date = ImageFont.truetype('C:/Windows/Fonts/georgia.ttf', 20)
f_venue = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 14)
f_host = ImageFont.truetype('C:/Windows/Fonts/georgia.ttf', 15)

col_gold_deep = (140, 109, 35, 255)
col_dark = (35, 30, 25, 245)
col_muted = (100, 90, 80, 230)

def draw_center(y, text, font, color):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    x = (W - w) // 2
    draw.text((x, y), text, fill=color, font=font)

# Bismillah Arabic Calligraphy text
draw_center(135, "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ", f_bismillah, col_gold_deep)

# Eyebrow
draw_center(180, "THE WEDDING RECEPTION OF", f_eyebrow, col_gold_deep)

# Hairline under eyebrow
draw.line([(W - 140) // 2, 204, (W + 140) // 2, 204], fill=border_light, width=1)

# Couple Names
draw_center(222, "MD. HIRAN", f_title, col_dark)
draw_center(276, "&", f_script, col_gold_deep)
draw_center(322, "MARIOM FERDOUSI", f_title, col_dark)

# Hairline under names
draw.line([(W - 200) // 2, 388, (W + 200) // 2, 388], fill=border_light, width=1)

# Date badge
draw_center(408, "SUNDAY · 17 JANUARY 2027 · 12:00 NOON", f_date, col_gold_deep)

# Venue details
draw_center(448, "\"Binapani\" Anusthan Bhaban · Near Yatrik Club, Suri, Birbhum", f_venue, col_muted)

# Host sign-off
draw.line([(W - 100) // 2, 492, (W + 100) // 2, 492], fill=border_light, width=1)
draw_center(510, "Best Wishes from Md. Samsuddin Mia & Sahila Bibi", f_host, col_dark)

# Save images
os.makedirs('images', exist_ok=True)
os.makedirs('assets', exist_ok=True)

# 1. Lossless PNG
base.save('images/og-image.png', 'PNG', optimize=True)
base.save('assets/og-image.png', 'PNG', optimize=True)

# 2. High-quality JPEG
rgb_base = base.convert('RGB')
rgb_base.save('images/og-image.jpg', 'JPEG', quality=95, optimize=True, progressive=True)
rgb_base.save('assets/og-image.jpg', 'JPEG', quality=95, optimize=True, progressive=True)
rgb_base.save('og-image.jpg', 'JPEG', quality=95, optimize=True, progressive=True)

print("Generated clean og-image.png and og-image.jpg successfully!")
