# heightcube.github.io

The HeightCube studio website, served by GitHub Pages from the root of the `main` branch.
Plain HTML and CSS, no build step, no external requests.

## Files

- `index.html` — the whole page: header, hero, sections, footer.
- `privacy.html` — the full privacy policy, with the same header and footer as `index.html`.
- `fr/index.html`, `fr/privacy.html` — the French versions of both pages.
- `site.js` — the email script and the hero fern, shared by every page.
- `style.css` — all styles, including colors and dark mode.
- `favicon.svg` — the logo used as the browser icon.
- `apps/flagquest/` — FlagQuest 4 Kids icon and screenshots (`en/`, `fr/`), shown in the Apps section.
- `play-console/` — Play Console developer icon and header image, with the scripts that make them.

## Editing content

- **Text:** edit `index.html` directly. Each section is a `<section>` with an `id`
  (`top`, `about`, `apps`, `contact`, `privacy`) that matches the header links.
- **French:** every change to `index.html` or `privacy.html` goes into `fr/` too. The French pages
  load shared files with `../` (`../style.css`, `../site.js`, `../apps/...`). Each page links its
  other-language twin in the header (the EN/FR link) and in `<link rel="alternate" hreflang>`.
  French text uses a no-break space before `:`, `?` and `!`.
- **Two lines of apps:** the Apps section first shows the two lines side by side (`.tiers`): apps
  **for kids** (no ads, no in-app purchases, no internet, nothing collected) and **games** (free to
  play, supported by ads and in-app purchases). Then one card per app (`article.card.app`,
  `#kids` and `#games`). The no-ads / no-data promises belong to the kids line only, here and in
  the privacy policy; don't state them for the whole studio.
- **The game:** its name is to be announced (placeholder card `#games`). Before it is released,
  fill in section 3 of the privacy policy (both languages) with the ad and payment services it
  uses and the data they process.
- **App screenshots:** 540×960 WebP, made from the store screenshots in the app's repo
  (`store-assets/screenshots/<lang>/`). Update the `alt` texts if the pictures change.
- **Google Play link:** FlagQuest 4 Kids is marked "Coming soon" (`badge` in the Apps card) until the
  listing is live; then replace the badge with a link to
  `https://play.google.com/store/apps/details?id=com.heightcube.flagquest`.
- **Colors:** change the custom properties at the top of `style.css` (`:root` for light mode,
  the `prefers-color-scheme: dark` block for dark mode). Keep text contrast at WCAG AA (4.5:1).
- **Email address:** it is assembled by `site.js`
  (`['heightcube', 'website'].join('+') + '@' + ...`) so it is not in the HTML as plain text.
  Update that line, and the `(at)` / `(dot)` (French: `(arobase)` / `(point)`) fallback text
  inside the `data-mail` links of every page.
- **Privacy policy:** edit `privacy.html`, and update the effective date when you change it.
  The header and footer are copied from `index.html`; keep the pages in sync.
- **Logo:** the cube paths appear inline in the header of every page, and in `favicon.svg`.
  Change them all together.
- **Fractals:** the hero fern is drawn by `site.js` (canvas). Its colors come from
  `--fern-a` and `--fern-b` in `style.css`. The small Sierpinski triangles come from the
  `<defs>` block at the top of `<body>`; they are also shown in place of the fern when
  JavaScript is off.

## Preview locally

Open `index.html` in a browser, or run `python3 -m http.server` and visit
<http://localhost:8000>.

## Social previews

There is no `og:image` yet. To add one, put a 1200×630 PNG in the repo and add
`<meta property="og:image" content="https://heightcube.github.io/og.png">` to the `<head>`.
