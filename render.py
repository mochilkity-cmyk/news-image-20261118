"""Render the news-image-20261118 entry: a 1024x1024 infographic of
Wednesday 18 November 2026 world news. Drawn with PIL (a build tool
only; the entry program itself is a plain copy in main.ts).
Run: python3 render.py  -> writes entry.png next to this file."""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (15, 42, 68)
INK = (18, 35, 58)
GREY = (61, 74, 92)
BG = (244, 246, 248)
CARD = (255, 255, 255)
BORDER = (216, 222, 230)
SUBBLUE = (159, 184, 208)
FOOTGREY = (110, 122, 138)

# (kicker, accent colour, headline, detail)
STORIES = [
    ("MIDDLE EAST", (192, 57, 43),
     "Iran strikes Kuwait and Bahrain",
     "Iran hit US bases in Kuwait and Bahrain early today, after US "
     "jets struck a missile site on Qeshm Island."),
    ("ASIA-PACIFIC", (108, 74, 182),
     "Trump lands in Shenzhen for summit",
     "Xi greeted Trump at the airport and met Putin; the first "
     "Trump-Xi-Putin talks are set for Thursday."),
    ("AMERICAS", (31, 111, 235),
     "Peltola wins Alaska Senate seat",
     "Democrat Mary Peltola beat Dan Sullivan with 50.1% of the vote, "
     "giving Democrats a 56-44 Senate majority."),
    ("EUROPE", (14, 124, 107),
     "Ukraine hits two Russian refineries",
     "Drones struck the Ilsky and Afipsky refineries overnight; "
     "output is down about 45% since late October."),
    ("TECHNOLOGY", (217, 115, 13),
     "Nvidia posts record $115.8bn quarter",
     "Revenue doubled to $115.8bn in its first report since "
     "Huang resigned; the board ruled out his return."),
    ("HEALTH", (46, 125, 50),
     "Ebola in DR Congo tops 11,000 cases",
     "WHO says cases more than doubled in 3 months; 400-500 new "
     "cases a week, emergency stays in force."),
]


def wrap(draw, text, font, max_w):
    """Wrap text to fit max_w pixels; returns a list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # ---- header band ----
    d.rectangle([0, 0, W, 150], fill=NAVY)
    f_date = ImageFont.truetype(BOLD, 52)
    f_sub = ImageFont.truetype(BOLD, 24)
    d.text((32, 24), "WEDNESDAY 18 NOVEMBER 2026", font=f_date, fill=(255, 255, 255))
    d.text((34, 96), "WORLD NEWS  ·  THE DAY IN SIX STORIES",
           font=f_sub, fill=SUBBLUE)

    # ---- story cards: 2 cols x 3 rows ----
    cw, ch, gap, m = 488, 256, 16, 16
    f_kick = ImageFont.truetype(BOLD, 19)
    f_head = ImageFont.truetype(BOLD, 30)
    f_det = ImageFont.truetype(REG, 22)
    for i, (kicker, accent, head, detail) in enumerate(STORIES):
        col, row = i % 2, i // 2
        x = m + col * (cw + gap)
        y = 166 + row * (ch + gap)
        # card
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=14,
                            fill=CARD, outline=BORDER, width=2)
        # accent bar
        d.rounded_rectangle([x + 2, y + 16, x + 12, y + ch - 16], radius=5,
                            fill=accent)
        tx = x + 30
        tw = cw - 30 - 22  # text width
        d.text((tx, y + 20), kicker, font=f_kick, fill=accent)
        head_lines = wrap(d, head, f_head, tw)
        assert len(head_lines) <= 2, f"headline too long: {head!r} -> {head_lines}"
        hy = y + 54
        for ln in head_lines:
            d.text((tx, hy), ln, font=f_head, fill=INK)
            hy += 37
        det_lines = wrap(d, detail, f_det, tw)
        assert len(det_lines) <= 3, f"detail too long: {detail!r} -> {det_lines}"
        dy = y + 54 + 2 * 37 + 8
        for ln in det_lines:
            d.text((tx, dy), ln, font=f_det, fill=GREY)
            dy += 28

    # ---- footer ----
    f_foot = ImageFont.truetype(REG, 19)
    foot = "Sources: Reuters · AP · AFP · WHO · UN News  —  events of 18 Nov 2026"
    fw = d.textlength(foot, font=f_foot)
    d.text(((W - fw) / 2, 982), foot, font=f_foot, fill=FOOTGREY)

    img.save("entry.png", "PNG")
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
