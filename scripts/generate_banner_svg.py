#!/usr/bin/env python3
"""Generate a high-impact animated card banner SVG for LordSk / Varun."""
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

.bg-card {{ fill: #0f1319; rx: 18px; }}
.inner-card {{ fill: #161b22; rx: 12px; stroke: #30363d; stroke-width: 1; }}

@keyframes pulseGlowGrad {{
  0% {{ stop-color: #ff4d8d; }}
  33% {{ stop-color: #c77dff; }}
  66% {{ stop-color: #22d3ee; }}
  100% {{ stop-color: #ff4d8d; }}
}}

@keyframes pulseGlowGrad2 {{
  0% {{ stop-color: #22d3ee; }}
  33% {{ stop-color: #ff4d8d; }}
  66% {{ stop-color: #c77dff; }}
  100% {{ stop-color: #22d3ee; }}
}}

.grad-1 {{ animation: pulseGlowGrad 5s infinite linear; }}
.grad-2 {{ animation: pulseGlowGrad2 5s infinite linear; }}

.card-title {{
  font-family: JBMono, sans-serif;
  font-size: 46px;
  font-weight: 600;
  fill: url(#card-grad);
  filter: drop-shadow(0px 0px 12px rgba(34, 211, 238, 0.6));
  letter-spacing: 4px;
}}

.card-sub {{
  font-family: JBMono, monospace;
  font-size: 14px;
  fill: #8b949e;
  letter-spacing: 2px;
}}

.status-pill-green {{
  fill: #0d2818;
  stroke: #2ea043;
  stroke-width: 1.5;
  rx: 14px;
}}

.status-pill-purple {{
  fill: #1f1235;
  stroke: #c77dff;
  stroke-width: 1.5;
  rx: 14px;
}}

.pill-text-green {{
  font-family: JBMono, monospace;
  font-size: 11px;
  font-weight: 600;
  fill: #3fb950;
}}

.pill-text-purple {{
  font-family: JBMono, monospace;
  font-size: 11px;
  font-weight: 600;
  fill: #c77dff;
}}

@keyframes dotPulse {{
  0%, 100% {{ r: 3.5px; opacity: 0.6; }}
  50% {{ r: 5px; opacity: 1; }}
}}

.dot-green {{ animation: dotPulse 1.8s infinite ease-in-out; fill: #3fb950; filter: drop-shadow(0px 0px 6px #3fb950); }}
.dot-purple {{ animation: dotPulse 2.2s infinite ease-in-out; fill: #c77dff; filter: drop-shadow(0px 0px 6px #c77dff); }}

.card-border {{
  stroke: url(#card-grad);
  stroke-width: 2;
  fill: none;
}}

@keyframes laserSweep {{
  0% {{ x1: 0; x2: 120; opacity: 0.2; }}
  50% {{ opacity: 0.9; }}
  100% {{ x1: 580; x2: 700; opacity: 0.2; }}
}}

.laser-line {{ animation: laserSweep 4s infinite linear; stroke: url(#card-grad); stroke-width: 2; }}
"""

    width = 700
    height = 240

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <linearGradient id="card-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" class="grad-1"/>
      <stop offset="100%" class="grad-2"/>
    </linearGradient>
  </defs>
  <style>{font_css}</style>
  
  <!-- Main Card Container -->
  <rect x="2" y="2" width="{width - 4}" height="{height - 4}" class="bg-card card-border"/>
  <rect x="14" y="14" width="{width - 28}" height="{height - 28}" class="inner-card"/>
  
  <!-- Laser Sweep Line -->
  <line y1="14" y2="14" class="laser-line"/>
  
  <!-- Status Pills Bar -->
  <g transform="translate(30, 32)">
    <rect x="0" y="0" width="180" height="28" class="status-pill-green"/>
    <circle cx="18" cy="14" r="4" class="dot-green"/>
    <text x="32" y="18" class="pill-text-green">● OPEN FOR DEVS</text>

    <rect x="195" y="0" width="220" height="28" class="status-pill-purple"/>
    <circle cx="213" cy="14" r="4" class="dot-purple"/>
    <text x="227" y="18" class="pill-text-purple">● FULL-STACK ARCHITECT</text>
  </g>

  <!-- Title & Branding -->
  <g text-anchor="start" transform="translate(32, 125)">
    <clipPath id="title-wipe">
      <rect x="0" y="-45" width="0" height="60">
        <animate attributeName="width" from="0" to="620" begin="0.10s" dur="0.75s" fill="freeze"/>
      </rect>
    </clipPath>
    <g clip-path="url(#title-wipe)">
      <text x="0" y="0" class="card-title">LORDSK / VARUN</text>
    </g>
    <text x="2" y="26" class="card-sub">varq &nbsp;·&nbsp; varaxx &nbsp;·&nbsp; varun &nbsp;·&nbsp; full-stack &amp; systems</text>
  </g>

  <!-- Bottom Accent Divider & Tagline -->
  <line x1="32" y1="184" x2="{width - 32}" y2="184" stroke="#30363d" stroke-width="1"/>
  <line x1="32" y1="184" x2="280" y2="184" stroke="url(#card-grad)" stroke-width="2"/>
  
  <text x="32" y="208" font-family="JBMono, monospace" font-size="12" fill="#8b949e" letter-spacing="1">
    :: CODE &nbsp;·&nbsp; BREAK &nbsp;·&nbsp; REBUILD &nbsp;·&nbsp; SHIP &nbsp;::
  </text>
</svg>"""

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "banner.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated high-impact card banner at {out_path}")

if __name__ == "__main__":
    generate()
