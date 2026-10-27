# Renders the Play Console header image (4096x2304 JPEG, under 1 MB).
# Run: ~/.local/share/playwright-venv/bin/python play-console/make_header.py
import base64, re
from pathlib import Path
from playwright.sync_api import sync_playwright

repo = Path(__file__).resolve().parent.parent  # repo root
svg = re.sub(r"@media[^{]*\{.*?\}\}", "", open(f"{repo}/favicon.svg").read(), flags=re.S)
logo = "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()
W, H = 4096, 2304

html = f"""<!doctype html><html><head><style>
html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;background:#f4f6f1}}
body{{background:radial-gradient(60% 70% at 50% 55%, #ffffff, #f4f6f1 70%, #e8eee1);
  font-family:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif;color:#24372c}}
canvas{{position:absolute;inset:0}}
.c{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}}
img{{width:520px;height:520px}}
h1{{margin:70px 0 0;font-size:260px;font-weight:700;letter-spacing:-6px;line-height:1}}
p{{margin:60px 0 0;font-size:96px;color:#4a5d50}}
.e{{margin:0 0 70px;font-size:64px;letter-spacing:12px;text-transform:uppercase;color:#588157;font-weight:600}}
</style></head><body>
<canvas id=f width={W} height={H}></canvas>
<div class=c><p class=e>Independent studio · Geneva</p><img src="{logo}"><h1>HeightCube</h1>
<p>Building Android apps with love.</p></div>
<script>
const x = document.getElementById('f').getContext('2d');
let seed = 7;  // change for a different fern
const rand = () => {{ seed = (seed + 0x6D2B79F5) | 0; let t = Math.imul(seed ^ seed >>> 15, 1 | seed); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }};
const A=[0x3a,0x5a,0x40], B=[0x94,0xad,0x79];
function fern(ox, oy, scale, rot, mirror, n) {{
  let a=0,b=0; const c=Math.cos(rot), s=Math.sin(rot);
  for (let i=0;i<n;i++) {{
    const r=rand(); let na;
    if (r<.01) {{na=0;b=.16*b}}
    else if (r<.86) {{na=.85*a+.04*b;b=-.04*a+.85*b+1.6}}
    else if (r<.93) {{na=.2*a-.26*b;b=.23*a+.22*b+1.6}}
    else {{na=-.15*a+.28*b;b=.26*a+.24*b+.44}}
    a=na; const px=mirror*a*scale, py=-b*scale, t=b/10;
    x.fillStyle=`rgb(${{A[0]+(B[0]-A[0])*t}},${{A[1]+(B[1]-A[1])*t}},${{A[2]+(B[2]-A[2])*t}})`;
    x.fillRect(ox+px*c-py*s, oy+px*s+py*c, 3, 3);
  }}
}}
fern(380, {H}+40, 210, 0.22, 1, 900000);
fern({W}-380, {H}+40, 210, -0.22, -1, 900000);
</script></body></html>"""

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": W, "height": H})
    pg.set_content(html); pg.wait_for_load_state("load")
    for q in (95, 90, 85, 80):
        data = pg.screenshot(type="jpeg", quality=q)
        if len(data) < 1_000_000: break
    b.close()
open(f"{repo}/play-console/header-4096x2304.jpg", "wb").write(data)
print("quality", q, "bytes", len(data))
