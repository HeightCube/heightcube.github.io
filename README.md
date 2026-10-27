# heightcube.github.io

The HeightCube studio website, served by GitHub Pages from the root of the `main` branch.
Plain HTML and CSS, no build step, no external requests.

## Files

- `index.html` — the whole page: header, hero, sections, footer, and a small inline script.
- `privacy.html` — the full privacy policy, with the same header and footer as `index.html`.
- `style.css` — all styles, including colors and dark mode.
- `favicon.svg` — the logo used as the browser icon.

## Editing content

- **Text:** edit `index.html` directly. Each section is a `<section>` with an `id`
  (`top`, `about`, `project`, `contact`, `privacy`) that matches the header links.
- **Colors:** change the custom properties at the top of `style.css` (`:root` for light mode,
  the `prefers-color-scheme: dark` block for dark mode). Keep text contrast at WCAG AA (4.5:1).
- **Email address:** it is assembled by the inline script at the bottom of `index.html`
  (`['heightcube', 'website'].join('+') + '@' + ...`) so it is not in the HTML as plain text.
  The same script is repeated at the bottom of `privacy.html`. Update that line in both files,
  and the `(at)` / `(dot)` fallback text inside the `data-mail` links.
- **Privacy policy:** edit `privacy.html`, and update the effective date when you change it.
  The header and footer are copied from `index.html`; keep the two pages in sync.
- **Logo:** the cube paths appear inline in the header of `index.html` and `privacy.html`,
  and in `favicon.svg`. Change all three together.
- **Fractals:** the hero fern is drawn by the inline script (canvas). Its colors come from
  `--fern-a` and `--fern-b` in `style.css`. The small Sierpinski triangles come from the
  `<defs>` block at the top of `<body>`; they are also shown in place of the fern when
  JavaScript is off.

## Preview locally

Open `index.html` in a browser, or run `python3 -m http.server` and visit
<http://localhost:8000>.

## Social previews

There is no `og:image` yet. To add one, put a 1200×630 PNG in the repo and add
`<meta property="og:image" content="https://heightcube.github.io/og.png">` to the `<head>`.
