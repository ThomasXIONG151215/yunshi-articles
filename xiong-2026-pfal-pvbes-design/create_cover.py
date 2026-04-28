"""
Energy Baseline - WeChat Article Cover
Design Philosophy: Scientific diagram meets agricultural precision
Canvas: 1200 x 630 px (WeChat cover standard)
"""
from PIL import Image, ImageDraw, ImageFont
import math

# Canvas size (WeChat cover standard)
W, H = 1200, 630

# Color palette - climate zone inspired
COLORS = {
    'bg': (250, 249, 245),        # Warm off-white
    'lhasa': (66, 133, 244),      # Clear sky blue
    'haikou': (251, 188, 5),      # Tropical sun yellow
    'shanghai': (234, 134, 83),   # Eastern warmth
    'urumqi': (158, 115, 180),   # Continental purple
    'harbin': (100, 116, 139),    # Northern slate
    'text_dark': (28, 27, 26),    # Near black
    'text_light': (255, 255, 255),# White
    'accent': (217, 119, 87),     # Warm accent
    'grid': (229, 227, 219),       # Subtle grid
    'solar': (251, 191, 36),       # Solar yellow
    'battery': (55, 125, 34),      # Battery green
    'container': (75, 85, 99),    # Steel gray
}

def load_font(size, bold=False):
    """Try to load a good font, fall back to default."""
    font_paths = [
        "C:/Users/熊元科/AppData/Local/Microsoft/Windows/Fonts/Geomanist-Regular.otf",
        "C:/Users/熊元科/AppData/Local/Microsoft/Windows/Fonts/Inter-VariableFont.ttf",
        "C:/Windows/Fonts/segui.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ]
    for path in font_paths:
        try:
            return ImageFont.truetype(path, size)
        except:
            continue
    return ImageFont.load_default()

def draw_climate_columns(img):
    """Draw 5 vertical columns representing climate zones."""
    draw = ImageDraw.Draw(img)
    margin = 80
    col_width = (W - 2 * margin) / 5
    cities = [
        ('拉萨', COLORS['lhasa'], '40m²'),
        ('海口', COLORS['haikou'], '50m²'),
        ('上海', COLORS['shanghai'], '80m²'),
        ('乌鲁木齐', COLORS['urumqi'], '110m²'),
        ('哈尔滨', COLORS['harbin'], '120m²'),
    ]

    for i, (city, color, pv_area) in enumerate(cities):
        x = margin + i * col_width
        # Column background
        col_h = 200
        y = H - col_h - 60

        # Draw column with gradient effect (lighter at top)
        for h_offset in range(col_h):
            ratio = h_offset / col_h
            r = int(color[0] * (0.6 + 0.4 * ratio))
            g = int(color[1] * (0.6 + 0.4 * ratio))
            b = int(color[2] * (0.6 + 0.4 * ratio))
            draw.line([(x + 10, y + h_offset), (x + col_width - 10, y + h_offset)], fill=(r, g, b))

        # City label
        font_bold = load_font(22, bold=True)
        draw.text((x + col_width/2 - 30, y + col_h + 10), city, fill=COLORS['text_dark'], font=font_bold)

        # PV area annotation
        font_small = load_font(16)
        draw.text((x + col_width/2 - 20, y + 30), pv_area, fill=(255,255,255), font=font_small)

    return y  # Return top y of columns

def draw_container_silhouette(img, cx, cy, scale=1.0):
    """Draw a stylized container plant factory silhouette."""
    draw = ImageDraw.Draw(img)
    w, h = 280 * scale, 160 * scale
    x, y = cx - w/2, cy - h/2

    # Main container body
    draw.rectangle([x, y, x+w, y+h], fill=COLORS['container'])

    # Roof structure
    draw.polygon([
        (x - 10, y), (x + w/2, y - 40 * scale),
        (x + w + 10, y)
    ], fill=(100, 116, 139))

    # Vents
    for i in range(4):
        vx = x + 30 + i * 60 * scale
        draw.rectangle([vx, y + 20, vx + 30, y + 35], fill=(55, 65, 79))

    # LED panels (inside container)
    for i in range(3):
        px = x + 40 + i * 75 * scale
        draw.rectangle([px, y + 60, px + 50, y + 120], fill=(251, 191, 36))

    # Wheels
    draw.ellipse([x + 20, y + h - 10, x + 45, y + h + 5], fill=(50, 50, 50))
    draw.ellipse([x + w - 45, y + h - 10, x + w - 20, y + h + 5], fill=(50, 50, 50))

    return x, y, w, h

def draw_energy_flow(img, cx, cy):
    """Draw energy flow arrows from sun to container."""
    draw = ImageDraw.Draw(img)

    # Sun (top center)
    sun_x, sun_y = cx, cy - 180
    sun_r = 45
    draw.ellipse([sun_x - sun_r, sun_y - sun_r, sun_x + sun_r, sun_y + sun_r], fill=COLORS['solar'])

    # Sun rays
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        inner_r = sun_r + 5
        outer_r = sun_r + 20
        draw.line([
            (sun_x + inner_r * math.cos(rad), sun_y + inner_r * math.sin(rad)),
            (sun_x + outer_r * math.cos(rad), sun_y + outer_r * math.sin(rad))
        ], fill=COLORS['solar'], width=3)

    # PV array symbol (between sun and container)
    pv_x, pv_y = cx - 60, cy - 80
    for row in range(2):
        for col in range(3):
            px = pv_x + col * 25
            py = pv_y + row * 20
            draw.rectangle([px, py, px + 20, py + 15], outline=COLORS['accent'], width=2)

    # Battery symbol
    bat_x, bat_y = cx + 80, cy - 80
    draw.rectangle([bat_x, bat_y, bat_x + 35, bat_y + 30], fill=COLORS['battery'])
    draw.rectangle([bat_x + 12, bat_y - 8, bat_x + 23, bat_y], fill=COLORS['battery'])

    # Flow arrows
    arrow_color = COLORS['accent']
    # Sun to PV
    draw.line([(sun_x, sun_y + sun_r), (pv_x + 35, pv_y + 10)], fill=arrow_color, width=2)
    # PV to battery
    draw.line([(pv_x + 65, pv_y + 15), (bat_x, bat_y + 15)], fill=arrow_color, width=2)
    # PV to container
    draw.line([(pv_x + 35, pv_y + 30), (pv_x + 35, cy - 30)], fill=arrow_color, width=2)

    # Labels
    font_label = load_font(14)
    draw.text((pv_x - 5, pv_y - 20), "PV", fill=COLORS['text_dark'], font=font_label)
    draw.text((bat_x + 5, bat_y - 20), "BES", fill=COLORS['text_dark'], font=font_label)

def draw_title_section(img):
    """Draw the title and key info."""
    draw = ImageDraw.Draw(img)

    # Main title
    font_title = load_font(48, bold=True)
    title = "植物工厂光伏储能设计基准"
    # Center text
    bbox = draw.textbbox((0, 0), title, font=font_title)
    title_w = bbox[2] - bbox[0]
    draw.text(((W - title_w) / 2, 50), title, fill=COLORS['text_dark'], font=font_title)

    # Subtitle
    font_sub = load_font(24)
    subtitle = "VFED仿真框架  ×  5气候带  ×  10584配置验证"
    bbox = draw.textbbox((0, 0), subtitle, font=font_sub)
    sub_w = bbox[2] - bbox[0]
    draw.text(((W - sub_w) / 2, 110), subtitle, fill=COLORS['accent'], font=font_sub)

def draw_data_annotations(img):
    """Draw key data points."""
    draw = ImageDraw.Draw(img)
    font_data = load_font(28, bold=True)

    # 5 cities
    draw.text((100, 170), "5", fill=COLORS['lhasa'], font=font_data)
    font_label = load_font(14)
    draw.text((130, 178), "气候带", fill=COLORS['text_dark'], font=font_label)

    # 10584
    draw.text((100, 210), "10584", fill=COLORS['accent'], font=font_data)
    draw.text((195, 218), "组配置", fill=COLORS['text_dark'], font=font_label)

    # VFED
    font_vfed = load_font(36, bold=True)
    draw.text((100, 255), "VFED", fill=COLORS['text_dark'], font=font_vfed)
    font_label2 = load_font(12)
    draw.text((100, 295), "Vertical Farm Energy Designer", fill=(120, 116, 102), font=font_label2)

def draw_grid_pattern(img):
    """Draw subtle background grid."""
    draw = ImageDraw.Draw(img)
    grid_spacing = 40
    for x in range(0, W, grid_spacing):
        draw.line([(x, 0), (x, H)], fill=COLORS['grid'], width=1)
    for y in range(0, H, grid_spacing):
        draw.line([(0, y), (W, y)], fill=COLORS['grid'], width=1)

def draw_framework_diagram(img, x, y):
    """Draw VFED framework layers."""
    draw = ImageDraw.Draw(img)
    font_small = load_font(13)

    layers = [
        ('气候数据', COLORS['lhasa']),
        ('EnergyPlus热模型', COLORS['shanghai']),
        ('光伏-储能-负荷模型', COLORS['accent']),
        ('参数优化', COLORS['battery']),
    ]

    box_w, box_h = 130, 28
    for i, (label, color) in enumerate(layers):
        bx = x
        by = y + i * (box_h + 8)
        # Box
        draw.rounded_rectangle([bx, by, bx + box_w, by + box_h], radius=4, fill=color)
        # Label
        draw.text((bx + 10, by + 6), label, fill=(255,255,255), font=font_small)
        # Connector line
        if i < len(layers) - 1:
            draw.line([(bx + box_w/2, by + box_h), (bx + box_w/2, by + box_h + 8)], fill=(180,180,170), width=1)

def main():
    # Create canvas
    img = Image.new('RGB', (W, H), COLORS['bg'])
    draw = ImageDraw.Draw(img)

    # Background grid
    draw_grid_pattern(img)

    # Title section (top)
    draw_title_section(img)

    # Left side: framework diagram
    draw_framework_diagram(img, 60, 170)

    # Center top: energy flow diagram
    draw_energy_flow(img, W/2, 280)

    # Center: container silhouette
    draw_container_silhouette(img, W/2, 400, scale=0.9)

    # Bottom: climate columns
    draw_climate_columns(img)

    # Right side: data annotations
    draw_data_annotations(img)

    # Bottom right: attribution
    font_small = load_font(12)
    draw.text((W - 250, H - 40), "上海交通大学 · 熊元科 鲍华等", fill=(120, 116, 102), font=font_small)

    # Save
    output_path = "D:/ACADEMIC_Writing/wechat_official_account/论文导读/xiong-2026-pfal-pvbes-design/cover_v1.png"
    img.save(output_path, 'PNG', quality=95)
    print(f"Cover saved to: {output_path}")

    # Also create a 900x383 version (WeChat article header)
    img_header = img.resize((900, 383), Image.LANCZOS)
    header_path = "D:/ACADEMIC_Writing/wechat_official_account/论文导读/xiong-2026-pfal-pvbes-design/cover_header.png"
    img_header.save(header_path, 'PNG', quality=95)
    print(f"Header saved to: {header_path}")

if __name__ == "__main__":
    main()
