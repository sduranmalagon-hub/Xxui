from PIL import Image, ImageDraw, ImageFont
import numpy as np
F = '/usr/share/fonts/opentype/inter/InterDisplay-%s.otf'
RED, BLACK = (225,6,0), (0,0,0)
im = Image.open('dia-del-arquitecto-v2.png').convert('RGB')
a = np.array(im).mean(axis=2); W,H = im.size
# puzzle frame: bottom border row and its horizontal extent
rows = np.where((a<150).sum(axis=1)>3)[0]; bottom = rows.max()
cols = np.where(a[bottom-3] < 150)[0]; L, R = cols.min(), cols.max()
print('puzzle', L, R, bottom)
d = ImageDraw.Draw(im)

def tracked(text, font, width):
    """Return per-glyph x offsets so text spans exactly `width`."""
    # word spaces open up to 2.6x the letter gap so words stay legible when justified
    ws = [font.getbbox(c)[2]-font.getbbox(c)[0] if c!=' ' else 0 for c in text]
    gap = (width - sum(ws)) / ((len(text)-1) + 1.6*text.count(' '))
    xs, x = [], 0
    for c, w in zip(text, ws):
        xs.append(x); x += w + gap + (1.6*gap if c==' ' else 0)
    return xs, gap

def draw_line(text, weight, width, y, colors):
    # find size so that natural tracking is ~0.12em
    size = 300
    while True:
        f = ImageFont.truetype(F % weight, size)
        xs, gap = tracked(text, f, width)
        if gap >= 0.12*size: break
        size -= 2
    top = f.getbbox('H')[1]
    for c, x, col in zip(text, xs, colors):
        bx = f.getbbox(c)[0] if c!=' ' else 0
        d.text((L + x - bx, y - top), c, font=f, fill=col)
    return f.getbbox('H')[3]-top, size

band_top, band_bot = bottom, H
w = R - L
# measure heights first
h2, s2 = 0, 0
f_tmp = None
t1, t2 = 'FELIZ DÍA DEL', 'ARQUITECTO'
# layout: line1 cap height ~ 0.32 of line2
gap1 = 46
# dry-run sizes
def size_for(text, weight):
    size = 300
    while True:
        f = ImageFont.truetype(F % weight, size); _, g = tracked(text, f, w)
        if g >= 0.12*size: return f
        size -= 2
f2 = size_for(t2, 'Medium'); cap2 = f2.getbbox('H')[3]-f2.getbbox('H')[1]
f1 = ImageFont.truetype(F % 'Light', int(f2.size*0.36)); cap1 = f1.getbbox('H')[3]-f1.getbbox('H')[1]
block = cap1 + gap1 + 6 + gap1 + cap2
y0 = band_top + (band_bot - band_top - block)//2 - 10
# line 1: light, tracked to full width
xs,_ = tracked(t1, f1, w); top = f1.getbbox('H')[1]
for c,x in zip(t1,xs):
    d.text((L + x - (f1.getbbox(c)[0] if c!=' ' else 0), y0 - top), c, font=f1, fill=BLACK)
# red rule
ry = y0 + cap1 + gap1
d.rectangle([W//2-45, ry, W//2+45, ry+5], fill=RED)
# line 2: semibold, the A in red echoing the centre piece
y2 = ry + 6 + gap1
xs,_ = tracked(t2, f2, w); top = f2.getbbox('H')[1]
for i,(c,x) in enumerate(zip(t2,xs)):
    d.text((L + x - f2.getbbox(c)[0], y2 - top), c, font=f2, fill=RED if i==0 else BLACK)
print('sizes', f1.size, f2.size, 'block', y0, y2+cap2)
im.save('dia-del-arquitecto-final.png')
