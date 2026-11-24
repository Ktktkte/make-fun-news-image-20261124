#!/usr/bin/env python3
"""Draw the news-image-20261124 front page: THE DAILY, Tuesday 24 November 2026."""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
M = 48  # margin
INK = (15, 15, 15)
GREY = (70, 70, 70)
RED = (139, 0, 0)  # single restrained accent
PAPER = (252, 250, 244)

SERIF_B = "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def wrap(text, f, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=f) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines

def para(text, f, x, y, max_w, leading, color=INK):
    for line in wrap(text, f, max_w):
        d.text((x, y), line, font=f, fill=color)
        y += leading
    return y

def rule(y, wdt=3, color=INK, x0=M, x1=W - M):
    d.line([(x0, y), (x1, y)], fill=color, width=wdt)
    return y + wdt

y = 30
# Masthead
f_mast = font(SERIF_B, 96)
t = "THE DAILY"
d.text(((W - d.textlength(t, font=f_mast)) / 2, y), t, font=f_mast, fill=INK)
y += 108
f_date = font(SANS_B, 25)
t = "TUESDAY 24 NOVEMBER 2026"
d.text(((W - d.textlength(t, font=f_date)) / 2, y), t, font=f_date, fill=RED)
y += 38
y = rule(y, 6, RED)
y = rule(y + 5, 2, INK)
y += 18

# --- Lead story ---
f_lead = font(SERIF_B, 57)
y = para("ICJ finds Myanmar guilty of Rohingya genocide", f_lead, M, y, W - 2 * M, 64)
y += 6
f_body = font(SERIF, 23)
y = para("The court ruled 9\u20136 that Myanmar\u2019s forces committed genocide against the Rohingya in 2017 \u2014 the first time it has found a state responsible. Fourteen countries, including the UK, Spain, Canada and Australia, recognised the decision on Monday.", f_body, M, y, W - 2 * M, 30)
y += 16
y = rule(y, 2)
y += 16

# --- Row 2: NATO (left) / El Chapo (right) ---
col_w = (W - 2 * M - 28) // 2
x2 = M + col_w + 28
f_h2 = font(SERIF_B, 31)
f_b2 = font(SERIF, 21)
y2a = para("NATO vows to defend against space threats", f_h2, M, y, col_w, 37)
y2a += 4
y2a = para("The alliance answered reports that Russia may launch a nuclear-armed satellite within 60 days. Tripoli demanded explanations from Kyiv after the Ukrainian attack on Russian ships near Benghazi.", f_b2, M, y2a, col_w, 27)
y2b = para("US drone helped capture El Chapo Isidro", f_h2, x2, y, col_w, 37)
y2b += 4
y2b = para("Fausto Isidro Meza Flores was seized in Sinaloa over the weekend. Mexico will try him despite a US extradition request.", f_b2, x2, y2b, col_w, 27)
d.line([(M + col_w + 14, y), (M + col_w + 14, max(y2a, y2b))], fill=GREY, width=1)
y = max(y2a, y2b) + 16
y = rule(y, 2)
y += 16

# --- Row 3: Nepal quake (left) / measles (right) ---
y3a = para("5.6-magnitude quake strikes Nepal", f_h2, M, y, col_w, 37)
y3a += 4
y3a = para("The tremor hit Koshi province, near the Chinese border, on Tuesday.", f_b2, M, y3a, col_w, 27)
y3b = para("Measles claims ninth life in Pennsylvania", f_h2, x2, y, col_w, 37)
y3b += 4
y3b = para("The epidemic has now spread to 46 counties across the state.", f_b2, x2, y3b, col_w, 27)
d.line([(M + col_w + 14, y), (M + col_w + 14, max(y3a, y3b))], fill=GREY, width=1)
y = max(y3a, y3b) + 16
y = rule(y, 2)
y += 16

# --- Bottom strip: SpaceX lawsuit + GTA 6 patch ---
f_h3 = font(SERIF_B, 27)
f_b3 = font(SERIF, 20)
y = para("Oregon and Virginia sue SpaceX over alleged Grok-generated child abuse images.", f_h3, M, y, W - 2 * M, 33)
y += 4
y = para("GTA 6 PS5 patch 01.002.002: first fixes land.", f_b3, M, y, W - 2 * M, 26, color=GREY)
y += 10
y = rule(y, 2)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
