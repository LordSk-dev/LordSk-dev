#!/usr/bin/env python3
"""Generate an ultra-stunning, animated cyberpunk ASCII header SVG banner for LordSk-dev."""
import base64
import os

FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")

def get_font_b64(filename):
    with open(os.path.join(FONT_DIR, filename), "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")

BANNER_ART = [
    "  ██╗      ██████╗ ██████╗ ██████╗ ███████╗██╗  ██╗",
    "  ██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██║  ██╗",
    "  ██║     ██║   ██║██████╔╝██║  ██║███████╗███████║",
    "  ██║     ██║   ██║██╔══██╗██║  ██║╚════██║██╔══██╗",
    "  ███████╗╚██████╔╝██║  ██║██████╔╝███████║██║  ██║",
    "  ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝",
    "                                                   ",
    "    :: 夢を追う — chase it until the neon burns out ::"
]

def generate():
    b64_400 = get_font_b64("jbmono-400.woff2")
    b64_600 = get_font_b64("jbmono-600.woff2")

    font_css = f"""
@font-face{{font-family:JBMono;font-style:normal;font-weight:400;font-display:block;src:url(data:font/woff2;base64,{b64_400}) format('woff2')}}
@font-face{{font-family:JBMono;font-style:normal;font-weight:600;font-display:block;src:url(data:font/woff2;base64,{b64_600}) format('woff2')}}

.bg {{ fill: #0b0b14; rx: 12px; }}
.glow-pink {{ fill: #ff4d8d; filter: drop-shadow(0px 0px 6px #ff4d8d); font-weight: 600; }}
.glow-cyan {{ fill: #22d3ee; filter: drop-shadow(0px 0px 6px #22d3ee); font-weight: 600; }}
.glow-purple {{ fill: #c77dff; filter: drop-shadow(0px 0px 6px #c77dff); font-weight: 400; }}
.border-glow {{ stroke: url(#cyber-grad); stroke-width: 1.5; fill: none; opacity: 0.85; }}

@keyframes pulseGlow {{
  0% {{ opacity: 0.7; }}
  50% {{ opacity: 1; filter: drop-shadow(0px 0px 10px #22d3ee); }}
  100% {{ opacity: 0.7; }}
}}
.pulse {{ animation: pulseGlow 3s infinite ease-in-out; }}
"""

    char_w = 9.6
    font_size = 15.0
    line_h = 24
    pad_x = 28
    pad_y = 28
    row_delay = 0.14

    max_len = max(len(line) for line in BANNER_ART)
    width = int(max_len * char_w + pad_x * 2)
    height = len(BANNER_ART) * line_h + pad_y * 2

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="JBMono,ui-monospace,SFMono-Regular,Menlo,Consolas,\'Liberation Mono\',monospace">',
        '<defs>',
        '  <linearGradient id="cyber-grad" x1="0%" y1="0%" x2="100%" y2="100%">',
        '    <stop offset="0%" stop-color="#ff4d8d"/>',
        '    <stop offset="50%" stop-color="#c77dff"/>',
        '    <stop offset="100%" stop-color="#22d3ee"/>',
        '  </linearGradient>',
        '</defs>',
        f'<style>{font_css}</style>',
        f'<rect x="2" y="2" width="{width - 4}" height="{height - 4}" class="bg border-glow pulse"/>'
    ]

    for i, line in enumerate(BANNER_ART):
        y = pad_y + i * line_h
        begin = f"{i * row_delay:.2f}s"
        end = f"{(i + 1) * row_delay:.2f}s"
        w = max(len(line), 1) * char_w
        safe = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        if i in (0, 1):
            cls = "glow-pink"
        elif i in (2, 3):
            cls = "glow-purple"
        elif i in (4, 5):
            cls = "glow-cyan"
        else:
            cls = "glow-purple"

        lines.append(f'<clipPath id="c{i}"><rect x="{pad_x}" y="{y}" height="{line_h}" width="0"><animate attributeName="width" from="0" to="{w:.1f}" begin="{begin}" dur="{row_delay}s" fill="freeze"/></rect></clipPath>')
        lines.append(f'<g clip-path="url(#c{i})"><text xml:space="preserve" x="{pad_x}" y="{y + 17:.1f}" class="{cls}" font-size="{font_size}">{safe}</text></g>')
        lines.append(f'<rect y="{y + 2}" width="4" height="20" fill="#22d3ee" opacity="0"><animate attributeName="x" from="{pad_x}" to="{pad_x + w:.1f}" begin="{begin}" dur="{row_delay}s" fill="freeze"/><set attributeName="opacity" to="0.9" begin="{begin}"/><set attributeName="opacity" to="0" begin="{end}"/></rect>')

    lines.append('</svg>')

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ascii.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Generated cyberpunk ASCII banner at {out_path}")

if __name__ == "__main__":
    generate()
