#!/usr/bin/env python3
"""Generate a stunning, high-tech animated vector SVG banner (NO ASCII) for LordSk / Varun."""
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

.bg {{ fill: #0b0b14; rx: 16px; }}

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

.main-title {{
  font-family: JBMono, sans-serif;
  font-size: 52px;
  font-weight: 600;
  fill: url(#animated-grad);
  filter: drop-shadow(0px 0px 14px rgba(34, 211, 238, 0.7));
  letter-spacing: 6px;
}}

.sub-aliases {{
  font-family: JBMono, monospace;
  font-size: 14px;
  fill: #8b949e;
  letter-spacing: 3px;
}}

.tagline {{
  font-family: JBMono, monospace;
  font-size: 14px;
  fill: url(#animated-grad);
  letter-spacing: 2px;
  filter: drop-shadow(0px 0px 8px rgba(255, 77, 141, 0.6));
}}

.border-glow {{
  stroke: url(#animated-grad);
  stroke-width: 2;
  fill: none;
}}

@keyframes scanLineSweep {{
  0% {{ y: 10; opacity: 0; }}
  15% {{ opacity: 0.5; }}
  85% {{ opacity: 0.5; }}
  100% {{ y: 210; opacity: 0; }}
}}

.scanline {{
  animation: scanLineSweep 3.5s infinite ease-in-out;
  fill: url(#scan-grad);
}}

@keyframes floatParticle1 {{
  0%, 100% {{ transform: translateY(0px) translateX(0px); opacity: 0.3; }}
  50% {{ transform: translateY(-12px) translateX(15px); opacity: 0.9; }}
}}

@keyframes floatParticle2 {{
  0%, 100% {{ transform: translateY(0px) translateX(0px); opacity: 0.4; }}
  50% {{ transform: translateY(14px) translateX(-18px); opacity: 1; }}
}}

.particle-1 {{ animation: floatParticle1 4s infinite ease-in-out; fill: #22d3ee; filter: drop-shadow(0px 0px 8px #22d3ee); }}
.particle-2 {{ animation: floatParticle2 5s infinite ease-in-out; fill: #ff4d8d; filter: drop-shadow(0px 0px 8px #ff4d8d); }}

@keyframes pulseDot {{
  0%, 100% {{ opacity: 0.3; r: 4px; }}
  50% {{ opacity: 1; r: 7px; filter: drop-shadow(0px 0px 10px #c77dff); }}
}}

.pulsing-dot {{ animation: pulseDot 2.5s infinite ease-in-out; fill: #c77dff; }}
"""

    width = 680
    height = 220

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <linearGradient id="animated-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" class="grad-1"/>
      <stop offset="100%" class="grad-2"/>
    </linearGradient>
    <linearGradient id="scan-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#22d3ee" stop-opacity="0"/>
      <stop offset="50%" stop-color="#22d3ee" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#22d3ee" stop-opacity="0"/>
    </linearGradient>
    <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#30363d" stroke-width="0.5" opacity="0.3"/>
    </pattern>
  </defs>
  <style>{font_css}</style>
  
  <!-- Background Card -->
  <rect x="2" y="2" width="{width - 4}" height="{height - 4}" class="bg border-glow"/>
  <rect x="10" y="10" width="{width - 20}" height="{height - 20}" fill="url(#grid)" rx="10"/>
  
  <!-- Animated Scanline -->
  <rect x="6" y="0" width="{width - 12}" height="14" class="scanline"/>
  
  <!-- Floating Particle Orbs -->
  <circle cx="90" cy="50" r="5" class="particle-1"/>
  <circle cx="590" cy="170" r="6" class="particle-2"/>
  <circle cx="610" cy="45" r="4" class="particle-1"/>
  <circle cx="70" cy="175" r="5" class="particle-2"/>
  
  <!-- Top Corner Accents -->
  <path d="M 20 35 L 20 20 L 35 20" stroke="#22d3ee" stroke-width="2" fill="none"/>
  <path d="M {width - 35} 20 L {width - 20} 20 L {width - 20} 35" stroke="#ff4d8d" stroke-width="2" fill="none"/>
  <path d="M 20 {height - 35} L 20 {height - 20} L 35 {height - 20}" stroke="#c77dff" stroke-width="2" fill="none"/>
  <path d="M {width - 35} {height - 20} L {width - 20} {height - 20} L {width - 20} {height - 35}" stroke="#22d3ee" stroke-width="2" fill="none"/>

  <!-- Content Group -->
  <g text-anchor="middle">
    <!-- Main Title with Typewriter Reveal -->
    <clipPath id="title-clip">
      <rect x="40" y="30" width="0" height="70">
        <animate attributeName="width" from="0" to="{width - 80}" begin="0.10s" dur="0.80s" fill="freeze"/>
      </rect>
    </clipPath>
    <g clip-path="url(#title-clip)">
      <text x="{width / 2}" y="82" class="main-title">LORDSK</text>
    </g>
    
    <!-- Aliases Bar -->
    <clipPath id="alias-clip">
      <rect x="60" y="105" width="0" height="30">
        <animate attributeName="width" from="0" to="{width - 120}" begin="0.70s" dur="0.60s" fill="freeze"/>
      </rect>
    </clipPath>
    <g clip-path="url(#alias-clip)">
      <text x="{width / 2}" y="125" class="sub-aliases">varq &nbsp;·&nbsp; varaxx &nbsp;·&nbsp; varun</text>
    </g>

    <!-- Pulsing Divider Line -->
    <line x1="140" y1="148" x2="{width - 140}" y2="148" stroke="url(#animated-grad)" stroke-width="1.5" opacity="0.8"/>
    <circle cx="{width / 2}" cy="148" class="pulsing-dot"/>

    <!-- Tagline with Typewriter Reveal -->
    <clipPath id="tagline-clip">
      <rect x="40" y="158" width="0" height="40">
        <animate attributeName="width" from="0" to="{width - 80}" begin="1.10s" dur="0.70s" fill="freeze"/>
      </rect>
    </clipPath>
    <g clip-path="url(#tagline-clip)">
      <text x="{width / 2}" y="180" class="tagline">:: code &nbsp;·&nbsp; break &nbsp;·&nbsp; rebuild &nbsp;·&nbsp; ship ::</text>
    </g>
  </g>
</svg>"""

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "banner.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated ultra-animated vector banner (NO ASCII) at {out_path}")

if __name__ == "__main__":
    generate()
