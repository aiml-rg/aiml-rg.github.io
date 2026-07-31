# aiml-rg

Website for the **Applied and Interpretable Machine Learning Research Group**
Centre for Industrial Software, Mærsk Mc-Kinney Møller Institute, University of Southern Denmark.

Static HTML and CSS. No build step, no dependencies. Open `index.html` in a browser, or serve the folder:

```
python3 -m http.server 8000
```

## Pages

| URL | File | Purpose |
| --- | --- | --- |
| `/` | `index.html` | What the group is, the four research lines, selected work, news |
| `/research/` | `research/index.html` | The research statement in full |
| `/work/` | `work/index.html` | Figure grid, one tile per result |
| `/work/<name>/` | `work/<name>/index.html` | One result, four slots |
| `/publications/` | `publications/index.html` | Publication list by year |
| `/news/` | `news/index.html` | Dated items, newest first |
| `/people/` | `people/index.html` | Members and collaborators |
| `/join/` | `join/index.html` | PhD positions, theses, visits, industry collaboration |

### Why every page is a directory

GitHub Pages serves static files, so a URL without `.html` only works if the file is called `index.html` inside a directory named after the page. That is the whole trick: `/research/` is `research/index.html`. An extensionless file called `research` would be served as a download, not a page.

**All internal links and asset paths are root-relative** (`/work/ecg/`, `/assets/css/site.css`). One form everywhere, no `../../` arithmetic to get wrong when a page moves or a new one is nested. The cost is that opening a file directly from disk no longer works; run the local server instead.

GitHub Pages redirects `/research` to `/research/`, so the trailing slash always appears in the address bar. There is no way to avoid that on Pages, and it is what almost every static academic site does.

The old flat `*.html` paths are kept at the repository root as one-line redirect stubs, because GitHub Pages caches HTML for ten minutes and a visitor holding a stale page would otherwise click straight into a 404. Each stub carries a canonical link to the real URL and `noindex`, so search engines only ever see one address per page. `404.html` catches everything else and offers the full list of pages in the site's own design.

## Adding to Selected work

The page is called Selected work, not Projects, on purpose. A project implies a named, ongoing thing with several outputs; these are individual results. If a real project ever exists, the word is still free.

Every entry carries the same four slots, in this order: **the question**, **what we found**, **what would sink it**, **the paper**. That template is the group's own method made structural, so keep it. An entry with nothing in the third slot is not ready to be a page.

Copy an existing `work/<name>/` directory, replace the four slots, drop the figure in `assets/img/figures/`, then add a tile to the grid in `work/index.html`.

**An entry is listed only once it has a figure.** Everything else stays on the publications page. This is deliberate: a grid of placeholder boxes is worse than a shorter grid. Figures are shown `object-fit: contain` on a white plate in both themes, never cropped, because a scientific figure cropped to fill a box is a figure you can no longer read.

## Structure

```
assets/
  css/site.css     all styling, one file
  js/theme.js      the auto / light / dark control
  img/             photographs
  img/figures/     paper figures used on Selected work
```

## Design

- **Palette** is the diverging colormap that every attribution figure uses: a white midpoint, a cool pole, a warm pole. Nothing else.
- **Structure** is an annotation gutter. Each section carries its metadata in the margin, the way a read model carries its notes.
- **Type** is IBM Plex Sans for structure, IBM Plex Mono for the utility layer, Newsreader for prose. Every display-size heading sets `text-wrap: balance`, so no title ends on an orphaned word.
- **No decoration.** An earlier draft laid a tinted attribution raster over the group name. At an opacity low enough not to hurt the headline it read as a rendering smudge rather than a figure, so it was removed. If something like it comes back, it has to be legible enough to be recognised as deliberate.

### Images

Photographs are cropped **in the file**, never by a CSS aspect ratio, so a breakpoint can never cut somebody off at the knees. `campus-hero.jpeg` is `sdu-campus.jpeg` cropped to the architecture above the people; the uncropped original stays in the folder as the source.

Portrait slots are 1:1 at 128px, matching SDU's own square profile photographs. **People without a photograph get no image block at all** rather than a grey placeholder box; each person opens with a hairline rule, so the roster reads as a list either way.

### Themes

Three states, cycled by the `auto / light / dark` button in the masthead and stored in `localStorage`: follow the system, force white, force dark. A short inline script in each `<head>` applies the stored choice before first paint, so the page never flashes the wrong theme.

Every text colour clears WCAG AA against its background in both themes, including the 10 to 12px mono utility layer. Measured ratios are in the comments at the top of `site.css`. If you change a colour, re-check it; the small mono text is the first thing to fail.

## Before this goes live

Search the source for `class="todo"` to find every placeholder. Currently:

- news dates
- research lines and photographs for the members
- Rebecca De Rosa's role
- collaborator names
- DOIs and PDF links on publications
- funding status and deadlines for the PhD call
- a shared group email address

One thing to verify before publishing, because it was reconstructed from public sources rather than supplied: **author orders and venues** on the 2026 preprints and the KES 2025 paper.

The group is based in **Sønderborg**. Note that the lead's public SDU listing shows Odense, so if a visitor cross-checks, the two will not match. Worth aligning the SDU profile.

Also worth deciding: the Centre already hosts a **Data and Intelligence Lab**. The site does not currently say how this group relates to it.

## Publishing

GitHub Pages, from the `main` branch root. Settings → Pages → Deploy from a branch → `main` / `(root)`.

## Research lines

Four, in this order: **interpretability**, **representation learning**, **imaging and biosignals**, **language and software**.

There is deliberately **no verification line**. The word pulls the group toward compliance and conformity assessment, which is not where the work sits. Where the question is genuinely about whether a claim holds up, the site says **evaluation**: what a benchmark is actually measuring, what an invariance test would have to look like, what survives the move from a paper to a running service. The Open-Box Fallacy paper stays on the publications page, because it is real, but it does not set the framing.

## Writing

Headlines are one declarative sentence ending in a full stop, and each states a position rather than describing the page's layout. They are also load-bearing against duplication: no claim should appear as a headline on one page and as prose on another. Two things that used to be repeated and are now stated once each: the falsifier idea (front page prose, then the method section on `/research/`) and the research-line names (short claims on the front page, descriptive headings on `/research/`).

If a line is added or removed, three places have to agree: the entry list on `index.html`, the numbered sections on `research/index.html`, and the tile keys on `work/index.html`.
