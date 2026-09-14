#!/usr/bin/env python3
"""Generate a high-impact, premium visual vector SVG banner for LordSk / Varun."""
import base64
import os

FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")

def get_font_b64(filename):
    with open(os.path.join(FONT_DIR, filename), "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")

def generate():
    b64_400 = get_font_b64("jbmono-400.woff2")
    b64_600 = get_font_b64("jbmono-600.woff2")

    font_css = f"""
@font-face{{font-family:JBMono;font-style:normal;font-weight:400;font-display:block;src:url(data:font/woff2;base64,{b64_400}) format('woff2')}}
@font-face{{font-family:JBMono;font-style:normal;font-weight:600;font-display:block;src:url(data:font/woff2;base64,{b64_600}) format('woff2')}}

svg {{ font-family: JBMono, system-ui, -apple-system, sans-serif; }}

.card-bg {{ fill: #0b0e14; rx: 16px; }}
.card-inner {{ fill: #131722; rx: 12px; stroke: #262c3a; stroke-width: 1.5; }}

@keyframes gradPulse {{
  0% {{ stop-color: #ff4d8d; }}
  33% {{ stop-color: #c77dff; }}
  66% {{ stop-color: #22d3ee; }}
  100% {{ stop-color: #ff4d8d; }}
}}

@keyframes gradPulse2 {{
  0% {{ stop-color: #22d3ee; }}
  33% {{ stop-color: #ff4d8d; }}
  66% {{ stop-color: #c77dff; }}
  100% {{ stop-color: #22d3ee; }}
}}

.g1 {{ animation: gradPulse 6s infinite linear; }}
.g2 {{ animation: gradPulse2 6s infinite linear; }}

.hero-title {{
  font-family: JBMono, monospace, sans-serif;
  font-size: 48px;
  font-weight: 600;
  fill: url(#neon-grad);
  filter: drop-shadow(0px 0px 10px rgba(34, 211, 238, 0.5));
  letter-spacing: 5px;
}}

.hero-sub {{
  font-family: JBMono, monospace;
  font-size: 14px;
  fill: #8c959f;
  letter-spacing: 2px;
}}

.pill-box-green {{
  fill: #092215;
  stroke: #238636;
  stroke-width: 1.5;
  rx: 12px;
}}

.pill-box-cyan {{
  fill: #091f2c;
  stroke: #1f6feb;
  stroke-width: 1.5;
  rx: 12px;
}}

.pill-txt-green {{ font-family: JBMono, monospace; font-size: 11px; font-weight: 600; fill: #3fb950; }}
.pill-txt-cyan {{ font-family: JBMono, monospace; font-size: 11px; font-weight: 600; fill: #58a6ff; }}

@keyframes dotGlow {{
  0%, 100% {{ r: 3.5px; opacity: 0.7; }}
  50% {{ r: 5px; opacity: 1; }}
}}

.dot-g {{ animation: dotGlow 1.8s infinite ease-in-out; fill: #3fb950; filter: drop-shadow(0px 0px 6px #3fb950); }}
.dot-c {{ animation: dotGlow 2.2s infinite ease-in-out; fill: #58a6ff; filter: drop-shadow(0px 0px 6px #58a6ff); }}

.outer-border {{
  stroke: url(#neon-grad);
  stroke-width: 2;
  fill: none;
}}

@keyframes beamSweep {{
  0% {{ x1: 0; x2: 100; opacity: 0.1; }}
  50% {{ opacity: 0.9; }}
  100% {{ x1: 600; x2: 700; opacity: 0.1; }}
}}

.laser-beam {{ animation: beamSweep 4s infinite linear; stroke: url(#neon-grad); stroke-width: 2; }}
"""

    width = 700
    height = 230

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <linearGradient id="neon-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" class="g1"/>
      <stop offset="100%" class="g2"/>
    </linearGradient>
  </defs>
  <style>{font_css}</style>
  
  <!-- Main Card Container -->
  <rect x="2" y="2" width="{width - 4}" height="{height - 4}" class="card-bg outer-border"/>
  <rect x="14" y="14" width="{width - 28}" height="{height - 28}" class="card-inner"/>
  
  <!-- Laser Beam -->
  <line y1="14" y2="14" class="laser-beam"/>
  
  <!-- Status Pills Bar -->
  <g transform="translate(32, 32)">
    <rect x="0" y="0" width="165" height="26" class="pill-box-green"/>
    <circle cx="16" cy="13" r="4" class="dot-g"/>
    <text x="28" y="17" class="pill-txt-green">● OPEN FOR DEVS</text>

    <rect x="180" y="0" width="210" height="26" class="pill-box-cyan"/>
    <circle cx="196" cy="13" r="4" class="dot-c"/>
    <text x="208" y="17" class="pill-txt-cyan">● FULL-STACK ARCHITECT</text>
  </g>

  <!-- Title & Branding -->
  <g transform="translate(32, 118)">
    <text x="0" y="0" class="hero-title">LORDSK / VARUN</text>
    <text x="2" y="25" class="hero-sub">varq &nbsp;·&nbsp; varaxx &nbsp;·&nbsp; varun &nbsp;·&nbsp; full-stack &amp; systems engineer</text>
  </g>

  <!-- Bottom Divider & Tagline -->
  <line x1="32" y1="175" x2="{width - 32}" y2="175" stroke="#262c3a" stroke-width="1"/>
  <line x1="32" y1="175" x2="300" y2="175" stroke="url(#neon-grad)" stroke-width="2"/>
  
  <text x="32" y="198" font-family="JBMono, monospace" font-size="12" fill="#8c959f" letter-spacing="1">
    :: CODE &nbsp;·&nbsp; BREAK &nbsp;·&nbsp; REBUILD &nbsp;·&nbsp; SHIP &nbsp;::
  </text>
</svg>"""

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "banner.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated clean high-impact visual banner at {out_path}")

if __name__ == "__main__":
    generate()
