#!/usr/bin/env python3
"""Generate Figure 2: Attack Surface Evolution Ladder + Threat Taxonomy.
V0.4: Ladder is the PRIMARY visual element (left axis), taxonomy branches from each level."""
from PIL import Image, ImageDraw, ImageFont
import os

FONT_DIR = "/home/zelin-zhang/Zhang_Zelin/Dev_Env/Conda/anaconda3/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf"
FONT_BOLD = ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf"), 18)
FONT_REG = ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSans.ttf"), 15)
FONT_SMALL = ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSans.ttf"), 13)
FONT_TITLE = ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf"), 22)
FONT_LEVEL = ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf"), 16)

W, H = 1500, 950
BG = "#FFFFFF"

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# Title
draw.text((W//2 - 300, 15), "AIGC Threat Taxonomy and Evolution Ladder", fill="#2C3E50", font=FONT_TITLE)

# Colors for each level
LEVEL_COLORS = ["#27AE60", "#F39C12", "#E74C3C", "#8E44AD", "#2C3E50"]
LEVEL_BGS = ["#EAFAF1", "#FEF9E7", "#FDEDEC", "#F4ECF7", "#EBEDEF"]

# Ladder levels (LEFT SIDE - primary)
levels = [
    {"num": "1", "name": "Direct PI", "year": "2022", "access": "Direct input",
     "agency": "Passive output", "scope": "Single output", "maturity": "Low",
     "threats": ["Goal hijacking", "Prompt leaking", "Instruction override"]},
    {"num": "2", "name": "Jailbreaking", "year": "2023", "access": "Crafted input",
     "agency": "Active instruction\nfollowing", "scope": "Session state", "maturity": "Low",
     "threats": ["Template-based (DAN)", "Optimization (GCG, PAIR)", "Multi-turn (Crescendo)",
                 "Multi-modal (FigStep)", "Encoding-based (cipher)"]},
    {"num": "3", "name": "Indirect PI", "year": "2023", "access": "Third-party\ncontent",
     "agency": "Retrieval +\nexecution", "scope": "Persistent state", "maturity": "Very low",
     "threats": ["RAG poisoning", "Web content injection", "Email/doc injection",
                 "Data exfiltration"]},
    {"num": "4", "name": "Agentic\nExploitation", "year": "2024", "access": "Tool chains,\nMCP servers",
     "agency": "Autonomous\nmulti-step", "scope": "Cross-system\ncascade", "maturity": "Very low",
     "threats": ["Tool poisoning (72.8%)", "Cross-server composition", "MCP supply chain",
                 "IDE vulnerabilities"]},
    {"num": "5", "name": "Multi-Agent\n(Emerging)", "year": "2025", "access": "Inter-agent\nmessages",
     "agency": "Delegated\nautonomy", "scope": "Cross-org\ncascade", "maturity": "None",
     "threats": ["Inter-agent trust (82.4%)", "Memory poisoning", "Privilege escalation"]},
]

# Layout
ladder_x = 50
ladder_w = 200
level_h = 140
level_gap = 25
start_y = 70
threat_x = 300
threat_w = 1150

def draw_rounded_rect(x, y, w, h, color, fill_color=None):
    draw.rounded_rectangle([x, y, x+w, y+h], radius=8, fill=fill_color or color+"20", outline=color, width=2)

for i, lv in enumerate(levels):
    y = start_y + i * (level_h + level_gap)
    color = LEVEL_COLORS[i]
    bg = LEVEL_BGS[i]

    # Level box (left)
    draw_rounded_rect(ladder_x, y, ladder_w, level_h, color, bg)
    # Level number circle
    cx, cy = ladder_x + 25, y + 25
    draw.ellipse([cx-15, cy-15, cx+15, cy+15], fill=color)
    draw.text((cx-5, cy-8), lv["num"], fill="#FFF", font=FONT_BOLD)
    # Level name
    name_lines = lv["name"].split("\n")
    for j, line in enumerate(name_lines):
        draw.text((cx + 22, y + 10 + j*20), line, fill=color, font=FONT_LEVEL)
    # Year
    draw.text((ladder_x + 10, y + level_h - 22), lv["year"], fill="#7F8C8D", font=FONT_SMALL)
    # Maturity badge
    badge_x = ladder_x + 60
    badge_y = y + level_h - 25
    draw.rounded_rectangle([badge_x, badge_y, badge_x + 80, badge_y + 20], radius=3, fill=color)
    bbox = draw.textbbox((0, 0), lv["maturity"], font=FONT_SMALL)
    tw = bbox[2] - bbox[0]
    draw.text((badge_x + (80-tw)//2, badge_y + 2), lv["maturity"], fill="#FFF", font=FONT_SMALL)

    # Connector arrow
    arrow_y = y + level_h // 2
    draw.line([(ladder_x + ladder_w, arrow_y), (threat_x, arrow_y)], fill=color, width=2)
    # Arrow head
    draw.polygon([(threat_x-8, arrow_y-5), (threat_x-8, arrow_y+5), (threat_x, arrow_y)], fill=color)

    # Three dimensions (small text under connector)
    dim_y = y + level_h // 2 + 8
    dims = f"Access: {lv['access'].replace(chr(10), ' ')}  |  Agency: {lv['agency'].replace(chr(10), ' ')}  |  Scope: {lv['scope'].replace(chr(10), ' ')}"
    draw.text((threat_x + 5, y + level_h - 18), dims, fill="#7F8C8D", font=FONT_SMALL)

    # Threat boxes (right)
    n_threats = len(lv["threats"])
    box_w = min(200, (threat_w - (n_threats-1)*10) // n_threats)
    for j, threat in enumerate(lv["threats"]):
        tx = threat_x + j * (box_w + 10)
        ty = y + 5
        th = level_h - 30
        draw.rounded_rectangle([tx, ty, tx+box_w, ty+th], radius=6, fill="#FFFFFF", outline=color+"80", width=1)
        # Wrap text
        words = threat.split()
        lines = []
        current = ""
        for w in words:
            test = current + " " + w if current else w
            bbox = draw.textbbox((0, 0), test, font=FONT_SMALL)
            if bbox[2] - bbox[0] > box_w - 16:
                lines.append(current)
                current = w
            else:
                current = test
        if current:
            lines.append(current)
        for k, line in enumerate(lines):
            bbox = draw.textbbox((0, 0), line, font=FONT_SMALL)
            tw = bbox[2] - bbox[0]
            draw.text((tx + (box_w-tw)//2, ty + 15 + k*18), line, fill="#2C3E50", font=FONT_SMALL)

# Vertical evolution arrow on far left
arr_x = 25
arr_top = start_y + 30
arr_bot = start_y + 5 * (level_h + level_gap) - level_gap - 30
draw.line([(arr_x, arr_top), (arr_x, arr_bot)], fill="#E74C3C", width=3)
draw.polygon([(arr_x-7, arr_bot), (arr_x+7, arr_bot), (arr_x, arr_bot+12)], fill="#E74C3C")
# Vertical label
for j, ch in enumerate("ESCALATION"):
    draw.text((arr_x-6, arr_top + 30 + j*22), ch, fill="#E74C3C", font=FONT_SMALL)

# Column headers
draw.text((ladder_x + 20, start_y - 25), "EVOLUTION LEVEL", fill="#2C3E50", font=FONT_BOLD)
draw.text((threat_x + 5, start_y - 25), "THREAT VECTORS", fill="#2C3E50", font=FONT_BOLD)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "fig2_threat_taxonomy.png"), dpi=(300, 300))
img.save(os.path.join(out_dir, "fig2_threat_taxonomy.pdf"))
print("Figure 2 saved.")
