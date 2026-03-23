#!/usr/bin/env python3
"""Generate Figure 3: Layered Defense Architecture for AIGC Security."""
from PIL import Image, ImageDraw, ImageFont
import os

FONT_DIR = "/home/zelin-zhang/Zhang_Zelin/Dev_Env/Conda/anaconda3/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf"
FONT_BOLD = ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf"), 20)
FONT_REG = ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSans.ttf"), 16)
FONT_SMALL = ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSans.ttf"), 14)
FONT_TITLE = ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf"), 24)
FONT_LABEL = ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf"), 16)

W, H = 1400, 900
BG = "#FFFFFF"
C_TEXT = "#2C3E50"

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# Title
draw.text((W // 2 - 280, 20), "Layered Defense Architecture for AIGC Security", fill=C_TEXT, font=FONT_TITLE)

# Layer definitions: (label, section, color, maturity, components)
layers = [
    {
        "label": "Layer 1: Detection & Provenance",
        "section": "§4.1-4.2",
        "color": "#27AE60",       # Green = most mature
        "maturity": "ESTABLISHED",
        "components": [
            ("Statistical\nDetection", "Zero-shot, trained\nclassifiers, multimodal"),
            ("Watermarking", "Token/semantic/\ndistribution-level,\nimage watermarks"),
            ("Content\nProvenance", "C2PA, Content\nCredentials,\ncryptographic signing"),
        ]
    },
    {
        "label": "Layer 2: Alignment & Hardening",
        "section": "§4.3.1-4.3.2",
        "color": "#F39C12",       # Orange = moderate
        "maturity": "DEVELOPING",
        "components": [
            ("Alignment", "RLHF, DPO, KTO,\nConstitutional AI"),
            ("Input Defenses", "Perplexity filtering,\nSmoothLLM,\ninstruction hierarchy"),
            ("Output Defenses", "Llama Guard,\nShieldGemma,\nsafety classifiers"),
            ("Model Defenses", "Circuit breakers,\nrepresentation\nengineering, LAT"),
        ]
    },
    {
        "label": "Layer 3: Agentic Security",
        "section": "§4.3.3",
        "color": "#E74C3C",       # Red = least mature (BLUE OCEAN)
        "maturity": "NASCENT",
        "components": [
            ("Architecture", "Trust boundaries,\nprivilege separation,\nharness engineering"),
            ("MCP Security", "OAuth 2.1, ETDI,\ntool call validation,\nsandboxing"),
            ("Runtime\nMonitoring", "AgentSpec, Pro2Guard,\naudit trails,\nanomaly detection"),
        ]
    },
    {
        "label": "Layer 4: Governance & Regulation",
        "section": "§5",
        "color": "#8E44AD",       # Purple = policy
        "maturity": "FRAGMENTED",
        "components": [
            ("EU AI Act", "Risk-based,\nmandatory watermarks,\ntransparency"),
            ("US Framework", "Executive orders,\nNIST AI RMF,\nvoluntary commitments"),
            ("China\nRegulations", "Content labeling,\nalgorithm filing,\nCore Socialist Values"),
            ("Industry\nSelf-Regulation", "Frontier commitments,\nmodel cards,\nred teaming"),
        ]
    },
]

# Layout
margin_left = 50
layer_start_y = 80
layer_h = 180
layer_gap = 15
comp_margin = 250  # space for layer label

def draw_layer(layer_info, y):
    color = layer_info["color"]
    label = layer_info["label"]
    section = layer_info["section"]
    maturity = layer_info["maturity"]
    components = layer_info["components"]

    # Layer background
    layer_w = W - 2 * margin_left
    draw.rounded_rectangle(
        [margin_left, y, margin_left + layer_w, y + layer_h],
        radius=10, fill=color + "15", outline=color, width=2
    )

    # Layer label (left side)
    draw.text((margin_left + 15, y + 10), label, fill=color, font=FONT_BOLD)
    draw.text((margin_left + 15, y + 35), section, fill="#7F8C8D", font=FONT_SMALL)

    # Maturity badge
    maturity_colors = {
        "ESTABLISHED": "#27AE60",
        "DEVELOPING": "#F39C12",
        "NASCENT": "#E74C3C",
        "FRAGMENTED": "#8E44AD",
    }
    badge_color = maturity_colors.get(maturity, "#95A5A6")
    badge_w = 120
    badge_x = margin_left + 15
    badge_y = y + 60
    draw.rounded_rectangle([badge_x, badge_y, badge_x + badge_w, badge_y + 24],
                          radius=4, fill=badge_color)
    bbox = draw.textbbox((0, 0), maturity, font=FONT_SMALL)
    tw = bbox[2] - bbox[0]
    draw.text((badge_x + (badge_w - tw) // 2, badge_y + 4), maturity, fill="#FFFFFF", font=FONT_SMALL)

    # Components (right side)
    n = len(components)
    available_w = layer_w - comp_margin - 20
    comp_w = min(240, (available_w - (n - 1) * 15) // n)
    comp_h = layer_h - 30
    start_x = margin_left + comp_margin

    for i, (comp_name, comp_desc) in enumerate(components):
        cx = start_x + i * (comp_w + 15)
        cy = y + 15

        # Component box
        draw.rounded_rectangle([cx, cy, cx + comp_w, cy + comp_h - 15],
                              radius=8, fill="#FFFFFF", outline=color + "80", width=1)

        # Component name
        name_lines = comp_name.split("\n")
        name_y = cy + 8
        for line in name_lines:
            bbox = draw.textbbox((0, 0), line, font=FONT_LABEL)
            tw = bbox[2] - bbox[0]
            draw.text((cx + (comp_w - tw) // 2, name_y), line, fill=color, font=FONT_LABEL)
            name_y += 20

        # Separator line
        sep_y = name_y + 5
        draw.line([(cx + 10, sep_y), (cx + comp_w - 10, sep_y)], fill=color + "40", width=1)

        # Description
        desc_lines = comp_desc.split("\n")
        desc_y = sep_y + 8
        for line in desc_lines:
            bbox = draw.textbbox((0, 0), line, font=FONT_SMALL)
            tw = bbox[2] - bbox[0]
            draw.text((cx + (comp_w - tw) // 2, desc_y), line, fill="#555555", font=FONT_SMALL)
            desc_y += 18

# Draw layers
for i, layer in enumerate(layers):
    y = layer_start_y + i * (layer_h + layer_gap)
    draw_layer(layer, y)

# Maturity arrow on the right
arrow_x = W - 35
arrow_top = layer_start_y + 20
arrow_bot = layer_start_y + 4 * (layer_h + layer_gap) - layer_gap - 20

draw.line([(arrow_x, arrow_top), (arrow_x, arrow_bot)], fill="#95A5A6", width=2)
# Arrow head pointing down
draw.polygon([(arrow_x - 6, arrow_bot), (arrow_x + 6, arrow_bot), (arrow_x, arrow_bot + 12)], fill="#95A5A6")

# Rotation label (vertical text approximation)
maturity_label = "Maturity"
for j, ch in enumerate(maturity_label):
    draw.text((arrow_x - 7, arrow_top + 40 + j * 18), ch, fill="#95A5A6", font=FONT_SMALL)

# Bottom note
note_y = H - 50
draw.text((margin_left, note_y),
          "Defense-in-depth: no single layer is sufficient. Resilient AI security requires composing all layers.",
          fill="#7F8C8D", font=FONT_REG)

# Save
out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "fig3_defense_layers.png"), dpi=(300, 300))
img.save(os.path.join(out_dir, "fig3_defense_layers.pdf"))
print("Figure 3 saved.")
