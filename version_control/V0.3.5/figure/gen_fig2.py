#!/usr/bin/env python3
"""Generate Figure 2: AIGC Threat Taxonomy Tree."""
from PIL import Image, ImageDraw, ImageFont
import os

FONT_DIR = "/home/zelin-zhang/Zhang_Zelin/Dev_Env/Conda/anaconda3/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf"
FONT_BOLD = ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf"), 22)
FONT_REG = ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSans.ttf"), 17)
FONT_SMALL = ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSans.ttf"), 14)
FONT_TITLE = ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf"), 26)

W, H = 1600, 1100
BG = "#FFFFFF"
# Colors
C_ROOT = "#2C3E50"
C_S1 = "#E74C3C"   # Content Weaponization - red
C_S2 = "#E67E22"   # Model-Level Attacks - orange
C_S3 = "#2980B9"   # Adversarial Manipulation - blue (HIGHLIGHT)
C_S3_BG = "#D6EAF8" # light blue background for blue ocean
C_S4 = "#8E44AD"   # Misinfo/Deepfakes - purple
C_S5 = "#27AE60"   # Ethical/Societal - green
C_ARROW = "#C0392B"
C_TEXT = "#2C3E50"

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

def rounded_rect(x, y, w, h, color, text, font, text_color="#FFFFFF", border=None):
    r = 8
    draw.rounded_rectangle([x, y, x+w, y+h], radius=r, fill=color, outline=border or color, width=2)
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((x + (w - tw) / 2, y + (h - th) / 2 - 2), text, fill=text_color, font=font)

def leaf_box(x, y, w, h, text, font, bg="#F8F9FA", border="#BDC3C7", text_color="#2C3E50"):
    draw.rounded_rectangle([x, y, x+w, y+h], radius=6, fill=bg, outline=border, width=1)
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((x + (w - tw) / 2, y + (h - th) / 2 - 1), text, fill=text_color, font=font)

def draw_line(x1, y1, x2, y2, color="#95A5A6", width=2):
    draw.line([(x1, y1), (x2, y2)], fill=color, width=width)

# Title
draw.text((W//2 - 250, 20), "AIGC Threat Taxonomy", fill=C_TEXT, font=FONT_TITLE)

# Root node
root_w, root_h = 340, 45
root_x, root_y = (W - root_w) // 2, 70
rounded_rect(root_x, root_y, root_w, root_h, C_ROOT, "AIGC Security Threats", FONT_BOLD)

# Level 1 categories - positions
cats = [
    ("§3.1 Content\nWeaponization", C_S1, 80),
    ("§3.2 Model-Level\nAttacks", C_S2, 370),
    ("§3.3 Adversarial\nManipulation", C_S3, 660),
    ("§3.4 Misinfo &\nDeepfakes", C_S4, 990),
    ("§3.5 Ethical &\nSocietal Risks", C_S5, 1280),
]

cat_w, cat_h = 230, 50
cat_y = 170

# Draw lines from root to categories
for label, color, cx in cats:
    mid_x = cx + cat_w // 2
    draw_line(W // 2, root_y + root_h, mid_x, cat_y, color="#7F8C8D")

# Draw category boxes
for label, color, cx in cats:
    rounded_rect(cx, cat_y, cat_w, cat_h, color, label.split("\n")[0], FONT_REG)
    if "\n" in label:
        line2 = label.split("\n")[1]
        bbox = draw.textbbox((0, 0), line2, font=FONT_SMALL)
        tw = bbox[2] - bbox[0]
        draw.text((cx + (cat_w - tw) / 2, cat_y + 30), line2, fill="#FFFFFF", font=FONT_SMALL)

# Blue ocean highlight for §3.3
highlight_x, highlight_y = 645, 155
draw.rounded_rectangle([highlight_x, highlight_y, highlight_x + 260, highlight_y + 650],
                       radius=12, fill=None, outline=C_S3, width=3)
draw.text((highlight_x + 5, highlight_y + 635), "BLUE OCEAN", fill=C_S3, font=FONT_SMALL)

# Leaves for each category
leaf_w, leaf_h = 210, 32
leaf_gap = 38

# §3.1 leaves
s1_leaves = ["AI-Generated Phishing", "AI-Assisted Malware", "Weaponized LLMs", "Non-Consensual NCII"]
s1_x = 90
for i, t in enumerate(s1_leaves):
    ly = 260 + i * leaf_gap
    draw_line(80 + cat_w // 2, cat_y + cat_h, s1_x + leaf_w // 2, ly)
    leaf_box(s1_x, ly, leaf_w, leaf_h, t, FONT_SMALL)

# §3.2 leaves
s2_leaves = ["Data/Supply Chain Poisoning", "Model Extraction/Inversion", "Fine-tuning Attacks"]
s2_x = 365
for i, t in enumerate(s2_leaves):
    ly = 260 + i * leaf_gap
    draw_line(370 + cat_w // 2, cat_y + cat_h, s2_x + leaf_w // 2, ly)
    leaf_box(s2_x, ly, leaf_w, leaf_h, t, FONT_SMALL)

# §3.3 leaves (BLUE OCEAN - highlighted)
s3_leaves = [
    ("Direct Prompt Injection", False),
    ("Jailbreaking (5 types)", False),
    ("Indirect Prompt Injection", False),
    ("Agentic Exploitation", True),  # Most novel
]
s3_x = 660
for i, (t, is_novel) in enumerate(s3_leaves):
    ly = 260 + i * leaf_gap
    draw_line(660 + cat_w // 2, cat_y + cat_h, s3_x + leaf_w // 2, ly)
    if is_novel:
        leaf_box(s3_x, ly, leaf_w, leaf_h, t, FONT_SMALL, bg=C_S3_BG, border=C_S3, text_color=C_S3)
    else:
        leaf_box(s3_x, ly, leaf_w, leaf_h, t, FONT_SMALL, bg="#EBF5FB", border="#85C1E9")

# Sub-leaves for Agentic Exploitation
agent_leaves = ["MCP Tool Poisoning", "Cross-Server Attacks", "Inter-Agent Trust"]
agent_x = 670
for i, t in enumerate(agent_leaves):
    ly = 430 + i * leaf_gap
    draw_line(s3_x + leaf_w // 2, 260 + 3 * leaf_gap + leaf_h, agent_x + 190 // 2, ly)
    leaf_box(agent_x, ly, 190, leaf_h, t, FONT_SMALL, bg=C_S3_BG, border=C_S3, text_color=C_S3)

# §3.4 leaves
s4_leaves = ["Deepfake Fraud", "Voice Cloning Scams", "Information Operations", "Ecosystem Degradation"]
s4_x = 985
for i, t in enumerate(s4_leaves):
    ly = 260 + i * leaf_gap
    draw_line(990 + cat_w // 2, cat_y + cat_h, s4_x + leaf_w // 2, ly)
    leaf_box(s4_x, ly, leaf_w, leaf_h, t, FONT_SMALL)

# §3.5 leaves
s5_leaves = ["Bias Amplification", "Psychological Impact", "Copyright & Accountability"]
s5_x = 1290
for i, t in enumerate(s5_leaves):
    ly = 260 + i * leaf_gap
    draw_line(1280 + cat_w // 2, cat_y + cat_h, s5_x + leaf_w // 2, ly)
    leaf_box(s5_x, ly, leaf_w, leaf_h, t, FONT_SMALL)

# Attack Surface Evolution Arrow (bottom)
arrow_y = 870
arrow_labels = [
    ("Direct PI", 200),
    ("Jailbreaking", 500),
    ("Indirect PI", 800),
    ("Agentic\nExploitation", 1100),
]

draw.text((W // 2 - 200, arrow_y - 40), "Attack Surface Evolution Ladder", fill=C_ARROW, font=FONT_BOLD)

# Arrow line
draw.line([(150, arrow_y + 20), (1350, arrow_y + 20)], fill=C_ARROW, width=3)
# Arrow head
draw.polygon([(1350, arrow_y + 10), (1350, arrow_y + 30), (1380, arrow_y + 20)], fill=C_ARROW)

for label, x in arrow_labels:
    # Circle marker
    draw.ellipse([x - 8, arrow_y + 12, x + 8, arrow_y + 28], fill=C_ARROW)
    lines = label.split("\n")
    for j, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=FONT_REG)
        tw = bbox[2] - bbox[0]
        draw.text((x - tw // 2, arrow_y + 35 + j * 20), line, fill=C_TEXT, font=FONT_REG)

# Complexity label
draw.text((1390, arrow_y + 12), "Complexity &", fill="#7F8C8D", font=FONT_SMALL)
draw.text((1390, arrow_y + 28), "Autonomy", fill="#7F8C8D", font=FONT_SMALL)

# Save
out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "fig2_threat_taxonomy.png"), dpi=(300, 300))
img.save(os.path.join(out_dir, "fig2_threat_taxonomy.pdf"))
print("Figure 2 saved.")
