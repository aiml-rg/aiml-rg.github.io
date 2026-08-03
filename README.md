# aiml-sdu.github.io

The website of the **Applied and Interpretable Machine Learning Research Group**, Centre for Industrial Software, Mærsk Mc-Kinney Møller Institute, University of Southern Denmark.

Live at **https://aiml-sdu.github.io**

Plain HTML and CSS. No framework, no build step, nothing to install. Editing a page means editing the page.

---

## Making a change

Everything on the site is text in an HTML file. Find the words you want to change, change them, open a pull request. The recipes below say which file.

### Change some wording

| What | File |
| --- | --- |
| The headline, the four research lines, selected work on the front page | `index.html` |
| The research statement | `research/index.html` |
| One study | `work/<name>/index.html` |
| The publication list | `publications/index.html` |
| A person, a role, a collaborator | `people/index.html` |
| A news item | `news/index.html` |
| Positions, supervision, contact | `join/index.html` |

Search the file for a phrase you can see on the page. The text between the tags is the text on the screen.

```html
<p class="line">Interpretability and verification of learned systems.</p>
         ↑ leave this alone      ↑ change this
```

### Add or correct your own entry on the People page

Open `people/index.html`, find the block with your name, and edit the three lines. To add someone, copy an existing block and change it.

```html
<div class="person">
  <p class="name">Ada Lovelace</p>
  <p class="role">PhD Fellow</p>
  <p class="line">One or two sentences on what you actually work on.</p>
  <div class="links">
    <a href="https://example.org">Site</a>
  </div>
</div>
```

Leave out any line you do not want. A person with no photograph gets no image block at all, which is deliberate: an empty grey box looks worse than no box.

### Add a photograph

1. Crop it before you add it. The frame will not crop for you, and a picture cropped by a browser gets cut differently on a phone than on a laptop.
2. Keep it under 1.5 MB. The check will refuse anything larger.
3. Put it in `assets/img/`.
4. Reference it with a leading slash and real dimensions:

```html
<img src="/assets/img/your-file.jpeg" alt="What is in the picture" width="2048" height="1080">
```

For a portrait, 1:1 square is the shape the page expects.

### Add a publication

Open `publications/index.html` and copy the nearest entry. Newest first inside each year.

```html
<div class="pub">
  <div class="pub-year">2026</div>
  <div>
    <p class="pub-title">The exact title of the paper</p>
    <p class="pub-meta">A. Author, B. Author &middot; <span class="venue">Venue</span></p>
  </div>
</div>
```

### Add a news item

Open `news/index.html` and copy an existing entry into the right year.

```html
<div class="entry">
  <div class="entry-key">2026</div>
  <div class="entry-body">
    <p>What happened, in one sentence. <a href="/work/">Link if there is one</a>.</p>
  </div>
</div>
```

### Add an entry to Selected work

This one has a rule. Every entry carries the same four slots, in this order: **the question**, **what we found**, **what would sink it**, **the paper**. That template is the group's own method made structural. An entry with nothing in the third slot is not ready to be a page.

An entry is listed only once there is a figure to show. Work without one lives on the publications page.

1. Put the figure in `assets/img/figures/`
2. Copy an existing `work/<name>/` directory and rename it
3. Replace the four slots
4. Add a tile to the grid in `work/index.html`

### Change the mark or the favicon

`assets/img/mark.svg` is the mark. It carries no colour: it is applied as a CSS mask over the current text colour, so it follows the theme instead of needing a light copy and a dark copy that drift apart.

`assets/img/favicon-v2.svg` is the only coloured version, because a browser tab cannot inherit a colour.

**If you change the favicon, change its filename too.** Browsers cache favicons harder than anything else and will keep showing the old one through a hard refresh. Bump the number and update the three `<link>` lines in every page.

---

## Before you open the pull request

Look at it, then run the check.

```bash
python3 -m http.server 8000      # then open http://localhost:8000
python3 .github/scripts/check_site.py
```

Opening an HTML file straight from Finder will not work, because every path on the site starts from the site root. Use the server.

The check catches the four things that actually take the site down: an unclosed tag, a link to a page that does not exist, a missing image, and a path that forgot its leading slash. It is the same check that runs on the pull request, so if it passes here it passes there.

---

## How a change reaches the site

`main` is what is published, so nothing is pushed to it directly.

1. Branch: `git switch -c people-add-ada`
2. Commit and push
3. Open a pull request
4. The check runs, and one other person reads it
5. Merge. The site updates in about a minute.

Two people looking at a change catches wrong dates, wrong titles and wrong roles, which no automated check can see. That is the reason for the review, not ceremony.

If something on the live site is wrong and needs to be gone right now, an admin can merge without waiting.

---

## Rules that are not obvious

**Paths start from the site root.** Always `/assets/img/x.jpg`, never `assets/img/x.jpg` and never `../assets/img/x.jpg`. One form everywhere means moving a page cannot break its images.

**Pages are directories.** `/research/` is `research/index.html`. That is how the URL stays free of `.html`. A new page is a new directory with an `index.html` in it.

**Photographs are cropped in the file, never by CSS.** A CSS crop changes with the window, which is how you end up with a group photograph cut off at the knees on a laptop.

**Colour has to clear WCAG AA.** The measured contrast ratios are in the comments at the top of `assets/css/site.css`. If you change a colour, re-check it. The small monospaced text is always the first thing to fail.

**No placeholder boxes.** If content is not ready, leave it out or mark it with `class="todo"`. A grey rectangle where a photograph should be looks worse than a shorter page.

---

## Reference

### Pages

| URL | File |
| --- | --- |
| `/` | `index.html` |
| `/research/` | `research/index.html` |
| `/work/` and `/work/<name>/` | `work/index.html`, `work/<name>/index.html` |
| `/publications/` | `publications/index.html` |
| `/news/` | `news/index.html` |
| `/people/` | `people/index.html` |
| `/join/` | `join/index.html` |

The only HTML files at the root are `index.html`, which is the front page, and `404.html`. Every other page lives in its own directory. If a link from before the site was restructured ever turns up, `404.html` catches it and offers the full list of pages.

### Files

```
assets/
  css/site.css     all styling, one file
  js/theme.js      the light and dark control
  img/             photographs, the mark, the favicons
  img/figures/     paper figures used on Selected work
  brand/           avatar exports; no page loads these
.github/
  scripts/check_site.py    the check, runnable locally
  workflows/checks.yml     the same check, on every pull request
```

### Design

**Palette** is the diverging colormap that every attribution figure uses: a white midpoint, a cool pole, a warm pole. Nothing else.

**Structure** is an annotation gutter. Each section carries its metadata in the margin, the way a read model carries its notes.

**Type** is IBM Plex Sans for structure, IBM Plex Mono for the utility layer, Newsreader for prose. Display headings set `text-wrap: balance`, so no title ends on an orphaned word.

**No decoration.** An earlier draft laid a tinted raster over the group name. At an opacity low enough not to hurt the headline it read as a rendering smudge, so it went. Anything like it has to be legible enough to be recognised as deliberate.

**The mark is provisional.** One square, cut twice on the diagonal, the three pieces opened out by an equal amount: a section through something that cannot be opened. Eleven alternatives are set out in the proposals PDF. This one is in place so the site is not empty while that is decided.

**Themes** are light and dark, stored in `localStorage`, with the system preference as the starting point on a first visit. A short inline script in each `<head>` settles the theme before first paint, and the button's glyph keys off the same attribute, so the icon is right on the first frame.

### Still to fill in

Search for `class="todo"` to find every placeholder currently on the site.

Two things to verify against a source rather than trusting the page: author orders and venues on the 2026 preprints, and the campus a member is actually based at.
