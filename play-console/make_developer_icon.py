# Renders the Play Console developer icon (512x512, opaque 24-bit PNG) from favicon.svg.
# Run: ~/.local/share/playwright-venv/bin/python play-console/make_developer_icon.py
import base64, re, struct, zlib
from pathlib import Path
from playwright.sync_api import sync_playwright

repo = Path(__file__).resolve().parent.parent  # repo root
svg = open(f"{repo}/favicon.svg").read()
# Light palette only: drop the dark-mode media query
svg = re.sub(r"@media[^{]*\{.*?\}\}", "", svg, flags=re.S)
SIZE, LOGO, BG = 512, 384, "#f4f6f1"  # logo ~75% so a circular crop keeps the whole cube

html = f"""<canvas id=c width={SIZE} height={SIZE}></canvas><script>
const img = new Image();
img.onload = () => {{
  const x = document.getElementById('c').getContext('2d');
  x.fillStyle = '{BG}'; x.fillRect(0, 0, {SIZE}, {SIZE});
  const o = ({SIZE} - {LOGO}) / 2;
  x.drawImage(img, o, o, {LOGO}, {LOGO});
  window.done = true;
}};
img.src = 'data:image/svg+xml;base64,{base64.b64encode(svg.encode()).decode()}';
</script>"""

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.set_content(html); pg.wait_for_function("window.done")
    rgba = bytes(pg.evaluate("Array.from(document.getElementById('c').getContext('2d').getImageData(0,0,%d,%d).data)" % (SIZE, SIZE)))
    b.close()

rows = b"".join(b"\0" + b"".join(rgba[i:i+3] for i in range(r*SIZE*4, (r+1)*SIZE*4, 4)) for r in range(SIZE))
def chunk(t, d): return struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d))
png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", SIZE, SIZE, 8, 2, 0, 0, 0)) \
    + chunk(b"IDAT", zlib.compress(rows, 9)) + chunk(b"IEND", b"")
open(f"{repo}/play-console/developer-icon-512.png", "wb").write(png)
