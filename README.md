# Oleg Devyatov — CV / Portfolio

Single-page bilingual (EN / RU) portfolio of a senior product designer. Dark, motion-aware, multi-layer hero, full case popups with galleries, lightbox with 2× horizontal-scroll zoom, skills matrix with cross-project chips, experience timeline, tool cloud.

**Live:** https://olezhapth2.github.io/cv/
**Repo:** https://github.com/olezhapth2/cv

---

## Architecture

Zero build step. Three files:

- [`index.html`](./index.html) — structure, project data (all case content lives in `data-*` attributes on the cards), inline JS for hero carousel, popup, lightbox, matrix, language switching, theme/font toggles.
- [`styles.css`](./styles.css) — all styles. Mobile-first responsive, mobile animation cuts via `@media (max-width: 900px), (hover: none)`.
- [`images/`](./images/) — covers and galleries (PNG, lazy-loaded).

That's the whole site. No framework, no bundler, no dependencies beyond Google Fonts.

## Features

- **Bilingual content** via `data-en` / `data-ru` attributes and `.lang-en` / `.lang-ru` body classes. Live language switch re-renders the open popup without closing it.
- **Deep hero** — 6 floating orbs, mouse parallax, glassmorphism carousel cards, per-card gradient glow, optional hover cover-image reveal.
- **9 project cases** with sticky-header popups, 2.8:1 galleries, clickable external links in case blocks, and a carousel gallery that wraps infinitely.
- **Lightbox** with 2× horizontal scroll for detailed viewing + thumbnail preview strip below.
- **Skills matrix** — chips cross-reference projects; clicking a chip opens the relevant project popup. Chips are shuffled on each load for variety.
- **Experience timeline** — collapsible year groups, deep links to project popups from inline references.
- **Tools cloud** — inline text list + devicon logos below.
- **Theme & font toggles** in the header — 8 font sets and 8 palettes, cycled in place via CSS variables.
- **Mobile perf** — heavy animations (float loops, conic spins, backdrop-filter, 3D hover transforms, gradient shifts) are disabled on touch and narrow viewports. Popup and lightbox scroll lock use `--vh` set from `window.innerHeight` to avoid address-bar glitches.

## Local preview

Any static server will do:

```bash
python3 -m http.server 8080
# then open http://127.0.0.1:8080
```

Or Docker:

```bash
docker build -t oleg-cv .
docker run --rm -p 8080:80 oleg-cv
```

## GitHub Pages deployment

The repo ships with a `.github/workflows/` config that deploys `main` → `gh-pages` automatically. In the repo settings:

1. **Settings → Pages → Build and deployment**
2. **Source:** Deploy from a branch
3. **Branch:** `gh-pages`, folder `/ (root)` → Save

After each push to `main`, wait 1–3 minutes and open the live URL.

`index.html` contains a small inline script that sets a dynamic `<base href="/cv/">` only on `*.github.io`, so assets resolve correctly under the repo path. The script reads `location.pathname` directly, so renaming the repo doesn't require a code change.

`.nojekyll` disables Jekyll processing.

## Code tour

- Hero HTML: [`index.html` L108–L292](./index.html#L108)
- Project cards & case data: [`index.html` L298–L556](./index.html#L298)
- Skills matrix chip data: [`index.html` L1161–L1230](./index.html#L1161)
- Experience timeline: [`index.html` L623–L762](./index.html#L623)
- Popup render + gallery carousel JS: [`index.html` L844–L1000](./index.html#L844)
- Hero carousel + hover cover JS: [`index.html` L1260–L1470](./index.html#L1260)
- Mobile animation kill-switch: [`styles.css` — search `Mobile performance`](./styles.css)

## License

Portfolio content (text, case write-ups, images) © Oleg Devyatov. Code is published as a reference implementation — feel free to study and borrow the patterns.
