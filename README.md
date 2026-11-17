# heightcube.github.io

The HeightCube studio website, served by GitHub Pages from the root of the `main` branch.
Plain HTML and CSS, no build step, no external requests.

## Files

- `index.html` — the whole page: header, hero, sections, footer.
- `privacy.html` — the full privacy policy, with the same header and footer as `index.html`.
- `fr/index.html`, `fr/privacy.html` — the French versions of both pages.
- `de/privacy.html` — the German privacy policy (there is no German home page: its header links go to the English `index.html`). Keep it in step with `privacy.html`; German uses the email fallback `(at)` / `(Punkt)`. The EN and FR privacy pages link it (DE in the header, `hreflang="de"`).
- `es/privacy.html`, `pt-br/privacy.html` — Spanish and Brazilian Portuguese privacy policies (the game's languages), built like the German one: header links go to the English home page, EN link in the header. Every privacy page lists all five languages in a `.policy-langs` line under the date and in `<link rel="alternate" hreflang>`.
- `site.js` — the email script, shared by every page.
- `style.css` — all styles, including colors and dark mode. The custom properties at the top are
  the design tokens: surfaces, text, the green accent, logo colors, type sizes (`--fs-*`), the
  spacing scale (`--s-1` … `--s-9`) and radii. Use them instead of hard-coded values.
- `favicon.svg` — the logo used as the browser icon. It is also shown as an image in the home hero
  (`.hero-art`) and in the footer, so it switches to its dark colors on its own.
- `apps/flagquest/` — FlagQuest 4 Kids icon and screenshots (`en/`, `fr/`), shown in the Apps section.
- `aceofshapes/index.html` — Ace of Shapes press kit (EN): facts, description (= the store listing), screenshots, downloads. Same header/footer as the privacy page, paths with `../`. Assets in `apps/aceofshapes/` (icon, feature graphic, `shots/*.webp` 540×1080 from the store screenshots, `aceofshapes-presskit.zip` with the full-size PNGs): regenerate them when the store art changes (icon redo pending).
- `play-console/` — Play Console developer icon and header image, with the scripts that make them.
- `app-ads.txt` — authorised ad sellers (AdMob publisher `pub-3710520883558713`), read by AdMob from the developer website set in Play Console. Must stay at the site root; add a line per new ad network.

## Editing content

- **Text:** edit `index.html` directly. Each section is a `<section>` with an `id`
  (`top`, `about`, `apps`, `contact`, `privacy`) that matches the header links.
- **Layout of the home page:** the hero (`.hero`: text, then the logo tile `.hero-art`, shown on wide
  screens only), About
  (`.split`: heading beside the text on wide screens), Apps on a full-width tinted band (`.band`),
  Contact in a centred card, and a short privacy note (`.privacy-note`). Each app card has a head
  (`.app-head`), a body (`.app-body`: text beside the screenshots on wide screens) and the three
  promises (`.points`, with small inline stroke icons).
- **French:** every change to `index.html` or `privacy.html` goes into `fr/` too. The French pages
  load shared files with `../` (`../style.css`, `../site.js`, `../apps/...`). Each page links its
  other-language twin in the header (the EN/FR link) and in `<link rel="alternate" hreflang>`.
  French text uses a no-break space before `:`, `?` and `!`.
- **Two lines of apps:** the Apps section first shows the two lines side by side (`.tiers`): apps
  **for kids** (no ads, no in-app purchases, no internet, nothing collected) and **games** (free to
  play, supported by ads and in-app purchases). Then one card per app (`article.card.app`,
  `#kids` and `#games`). The no-ads / no-data promises belong to the kids line only, here and in
  the privacy policy; don't state them for the whole studio.
- **The game:** Ace of Shapes, the studio's first free-to-play game (card `#games`, same layout as FlagQuest): icon `apps/aceofshapes/icon.png`,
  3 screenshots from `apps/aceofshapes/shots/` (the press kit's, 540×1080), three points (free to play, no pay-to-win, quick runs) and a
  link to the press kit `aceofshapes/`. Live on Google Play since 2026-11-17. The old teaser styles (`.teaser*`, `.app-icon-shapes`) are unused.
- **App screenshots:** 540×960 WebP, made from the store screenshots in the app's repo
  (`store-assets/screenshots/<lang>/`). Update the `alt` texts if the pictures change.
- **Google Play link:** both apps are live: the badge is a link (`a.badge badge-link`) to
  `https://play.google.com/store/apps/details?id=com.heightcube.flagquest` / `…aceofshapes` (`&hl=fr` on the French page).
- **Colors:** change the custom properties at the top of `style.css` (`:root` for light mode,
  the `prefers-color-scheme: dark` block for dark mode). Keep text contrast at WCAG AA (4.5:1),
  including `--accent` and `--link` on `--surface-2`, and `--accent-ink` on `--accent-soft`
  (badges). The `theme-color` meta tags in every page repeat `--bg`.
- **Header on phones:** below 30em the About link is hidden, and if the links still do not fit
  (the privacy pages, with two language links, on phones narrower than about 375 px) they wrap
  onto a second row, aligned right.
- **Email address:** it is assembled by `site.js`
  (`['heightcube', 'website'].join('+') + '@' + ...`) so it is not in the HTML as plain text.
  Update that line, and the `(at)` / `(dot)` (French: `(arobase)` / `(point)`) fallback text
  inside the `data-mail` links of every page.
- **Privacy policy:** edit `privacy.html`, `fr/privacy.html`, `de/privacy.html`, `es/privacy.html` and `pt-br/privacy.html` together, and update the effective date in all five when you change it. Add a language when a game is translated into it (Ace of Shapes: EN, FR, ES, PT-BR, DE).
  The header and footer are copied from `index.html`; keep the pages in sync (the footer's small
  logo is `favicon.svg`, `../favicon.svg` in `fr/` and `de/`).
- **Logo:** the cube paths appear inline in the header of every page, and in `favicon.svg`.
  Change them all together.

## Preview locally

Open `index.html` in a browser, or run `python3 -m http.server` and visit
<http://localhost:8000>.

## Social previews

There is no `og:image` yet. To add one, put a 1200×630 PNG in the repo and add
`<meta property="og:image" content="https://heightcube.github.io/og.png">` to the `<head>`.
