#!/usr/bin/env python3
"""Generate an ultra-animated, cyberpunk ASCII header SVG banner for LordSk-dev."""
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
    "        chase it until the neon burns out ::"
]

def generate():
    b64_400 = get_font_b64("jbmono-400.woff2")
    b64_600 = get_font_b64("jbmono-600.woff2")

    font_css = f"""
@font-face{{font-family:JBMono;font-style:normal;font-weight:400;font-display:block;src:url(data:font/woff2;base64,{b64_400}) format('woff2')}}
@font-face{{font-family:JBMono;font-style:normal;font-weight:600;font-display:block;src:url(data:font/woff2;base64,{b64_600}) format('woff2')}}

.bg {{ fill: #0b0b14; rx: 12px; }}

@keyframes gradCycle {{
  0% {{ stop-color: #ff4d8d; }}
  33% {{ stop-color: #c77dff; }}
  66% {{ stop-color: #22d3ee; }}
  100% {{ stop-color: #ff4d8d; }}
}}

@keyframes gradCycle2 {{
  0% {{ stop-color: #22d3ee; }}
  33% {{ stop-color: #ff4d8d; }}
  66% {{ stop-color: #c77dff; }}
  100% {{ stop-color: #22d3ee; }}
}}

.grad-1 {{ animation: gradCycle 6s infinite linear; }}
.grad-2 {{ animation: gradCycle2 6s infinite linear; }}

.neon-text {{
  fill: url(#animated-grad);
  filter: drop-shadow(0px 0px 7px rgba(34, 211, 238, 0.6));
  font-weight: 600;
}}

.sub-text {{
  fill: url(#animated-grad);
  filter: drop-shadow(0px 0px 5px rgba(255, 77, 141, 0.5));
}}

.border-glow {{
  stroke: url(#animated-grad);
  stroke-width: 1.5;
  fill: none;
}}

@keyframes scanSweep {{
  0% {{ y: 0; opacity: 0; }}
  20% {{ opacity: 0.45; }}
  80% {{ opacity: 0.45; }}
  100% {{ y: 240; opacity: 0; }}
}}

.scanline {{
  animation: scanSweep 4s infinite ease-in-out;
  fill: url(#scan-grad);
}}

@keyframes cursorBlink {{
  0%, 100% {{ opacity: 0.9; }}
  50% {{ opacity: 0.1; }}
}}

.cursor-pulse {{
  animation: cursorBlink 0.9s infinite ease-in-out;
  fill: #22d3ee;
  filter: drop-shadow(0px 0px 8px #22d3ee);
}}
"""

    char_w = 9.6
    font_size = 15.0
    line_h = 24
    pad_x = 28
    pad_y = 28
    row_delay = 0.12

    max_len = max(len(line) for line in BANNER_ART)
    width = int(max_len * char_w + pad_x * 2)
    height = len(BANNER_ART) * line_h + pad_y * 2

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="JBMono,ui-monospace,SFMono-Regular,Menlo,Consolas,\'Liberation Mono\',monospace">',
        '<defs>',
        '  <linearGradient id="animated-grad" x1="0%" y1="0%" x2="100%" y2="100%">',
        '    <stop offset="0%" class="grad-1"/>',
        '    <stop offset="100%" class="grad-2"/>',
        '  </linearGradient>',
        '  <linearGradient id="scan-grad" x1="0%" y1="0%" x2="0%" y2="100%">',
        '    <stop offset="0%" stop-color="#22d3ee" stop-opacity="0"/>',
        '    <stop offset="50%" stop-color="#22d3ee" stop-opacity="0.3"/>',
        '    <stop offset="100%" stop-color="#22d3ee" stop-opacity="0"/>',
        '  </linearGradient>',
        '</defs>',
        f'<style>{font_css}</style>',
        f'<rect x="2" y="2" width="{width - 4}" height="{height - 4}" class="bg border-glow"/>',
        f'<rect x="4" y="0" width="{width - 8}" height="12" class="scanline"/>'
    ]

    for i, line in enumerate(BANNER_ART):
        y = pad_y + i * line_h
        begin = f"{i * row_delay:.2f}s"
        end = f"{(i + 1) * row_delay:.2f}s"
        w = max(len(line), 1) * char_w
        safe = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        cls = "sub-text" if i >= 6 else "neon-text"

        lines.append(f'<clipPath id="c{i}"><rect x="{pad_x}" y="{y}" height="{line_h}" width="0"><animate attributeName="width" from="0" to="{w:.1f}" begin="{begin}" dur="{row_delay}s" fill="freeze"/></rect></clipPath>')
        lines.append(f'<g clip-path="url(#c{i})"><text xml:space="preserve" x="{pad_x}" y="{y + 17:.1f}" class="{cls}" font-size="{font_size}">{safe}</text></g>')
        lines.append(f'<rect y="{y + 2}" width="4" height="20" fill="#22d3ee" opacity="0"><animate attributeName="x" from="{pad_x}" to="{pad_x + w:.1f}" begin="{begin}" dur="{row_delay}s" fill="freeze"/><set attributeName="opacity" to="0.9" begin="{begin}"/><set attributeName="opacity" to="0" begin="{end}"/></rect>')

    # Add permanent pulsing glowing cursor at end of banner text
    last_y = pad_y + (len(BANNER_ART) - 1) * line_h + 2
    last_x = pad_x + len(BANNER_ART[-1]) * char_w + 6
    lines.append(f'<rect x="{last_x:.1f}" y="{last_y}" width="8" height="18" class="cursor-pulse"/>')

    lines.append('</svg>')

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ascii.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Generated animated cyberpunk ASCII banner at {out_path}")

if __name__ == "__main__":
    generate()
