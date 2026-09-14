#!/usr/bin/env python3
"""Generate an animated ASCII header SVG banner for LordSk-dev."""
import base64
import os

FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")

def get_font_b64(filename):
    with open(os.path.join(FONT_DIR, filename), "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")

BANNER_ART = [
    "                      _                 _ _____  _      ",
    "                     | |               | /  ___|| |     ",
    "                     | |     ___  _ __ | \\ `--. | | __  ",
    "                     | |    / _ \\| '__|| |`--. \\| |/ /  ",
    "                     | |___| (_) | |   | /\\__/ /|   <   ",
    "                     \\_____/\\___/|_|   |_\\____/ |_|\\_\\  ",
    "                                                        ",
    "        :: code  ·  break  ·  rebuild  ·  ship ::       "
]

def generate():
    b64_400 = get_font_b64("jbmono-400.woff2")
    b64_600 = get_font_b64("jbmono-600.woff2")

    font_css = f"""@font-face{{font-family:JBMono;font-style:normal;font-weight:400;font-display:block;src:url(data:font/woff2;base64,{b64_400}) format('woff2')}}
@font-face{{font-family:JBMono;font-style:normal;font-weight:600;font-display:block;src:url(data:font/woff2;base64,{b64_600}) format('woff2')}}
.a{{fill:#6e7681}}
.b{{fill:#424a53;font-weight:600}}
@media(prefers-color-scheme:dark){{.a{{fill:#c9d1d9}}.b{{fill:#f0f6fc}}}}"""

    char_w = 9.0
    font_size = 15.0
    line_h = 22
    pad = 20
    row_delay = 0.12

    max_len = max(len(line) for line in BANNER_ART)
    width = int(max_len * char_w + pad * 2)
    height = len(BANNER_ART) * line_h + pad * 2

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="JBMono,ui-monospace,SFMono-Regular,Menlo,Consolas,\'Liberation Mono\',monospace">',
        f'<style>{font_css}</style>'
    ]

    for i, line in enumerate(BANNER_ART):
        y = pad + i * line_h
        begin = f"{i * row_delay:.2f}s"
        end = f"{(i + 1) * row_delay:.2f}s"
        w = max(len(line), 1) * char_w
        safe = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        cls = "b" if "code" in line or i in (1, 2, 3, 4) else "a"

        lines.append(f'<clipPath id="c{i}"><rect x="{pad}" y="{y}" height="{line_h}" width="0"><animate attributeName="width" from="0" to="{w:.1f}" begin="{begin}" dur="{row_delay}s" fill="freeze"/></rect></clipPath>')
        lines.append(f'<g clip-path="url(#c{i})"><text xml:space="preserve" x="{pad}" y="{y + 16:.1f}" class="{cls}" font-size="{font_size}">{safe}</text></g>')
        lines.append(f'<rect y="{y + 2}" width="6" height="18" class="a" opacity="0"><animate attributeName="x" from="{pad}" to="{pad + w:.1f}" begin="{begin}" dur="{row_delay}s" fill="freeze"/><set attributeName="opacity" to="0.8" begin="{begin}"/><set attributeName="opacity" to="0" begin="{end}"/></rect>')

    lines.append('</svg>')

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ascii.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Generated {out_path}")

if __name__ == "__main__":
    generate()
