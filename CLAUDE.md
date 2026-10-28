The HeightCube studio website (GitHub Pages, plain HTML/CSS, no build step, no external requests). Read README.md before editing: it explains the pages, the colours, the obfuscated email address and what must stay in sync between `index.html` and `privacy.html`.

## Assets & Website

### Branding & assets
- Generate image assets (icons, headers, Play Console graphics) with scripts saved in the repo, so they can be reproduced: see `play-console/make_header.py` and `play-console/make_developer_icon.py`. Each script says how to run it in its first lines.
- Take colours and fonts from the site: the custom properties at the top of `style.css` (`:root` for light, the `prefers-color-scheme: dark` block for dark, `--font` for the font stack) and the logo in `favicon.svg`.
- Commit the scripts along with their outputs.

### Checking pages
- Before pushing, check the pages with Playwright (`~/.local/share/playwright-venv/bin/python`, Chromium already installed) at a phone width (about 375 px) and a desktop width (about 1280 px), in both light and dark mode. Look at the screenshots, not only at whether the script ran.
- Keep text contrast at WCAG AA (4.5:1) in both modes.
