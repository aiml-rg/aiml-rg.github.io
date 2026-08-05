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
| The headline and the four research lines | `index.html` |
| The research statement, and any of the four studies | `research/index.html` |
| The publication list | `publications/index.html` |
| A person or a role | `people/index.html` |
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

**This list is selected, not complete.** That is the whole point of it. Members' full records are linked at the bottom of the page, and that is where completeness belongs.

The page does not say any of this about itself. An earlier headline read "The group is new, so this is a short list", which was both an apology nobody asked for and untrue: the list is short because it is chosen, not because there is little to choose from. Serkan alone has fifty research outputs on the SDU portal. Selection is an editorial policy, and it belongs here, not in the reader's face.

Three bands, and an entry has to earn the one it goes in:

- **Peer-reviewed** — through review somewhere real. A journal, a conference, a named workshop.
- **Preprints** — the group's current work, honest about not having been refereed.
- **What members bring** — a short set of papers members did elsewhere, each carrying something the group is built on: clinical machine learning built with hospital teams, industrial machine learning running in production.

  Two things to keep right in the wording here. Frame it as what it adds, not as where it was not done: a disclaimer reads as an apology for work that needs none. But what a member brings is the **experience** of having done it, not the collaborations themselves — the hospital teams are in Istanbul and stayed there. "Members brought the experience" is true; "the work came here with them" quietly hands the group a clinical partnership it does not have.

**What does not go on.** A paper at a venue nobody outside its own country indexes. A paper off all four research lines that only pads the count. A second paper on a topic where a stronger one is already listed. Four entries were removed for exactly these reasons when the list was last revised, and removing them made the page stronger, because a reader who spots one weak entry starts discounting the rest.

The test is not "is this ours" but "does this establish something". A group's publication page is read as a claim about competence, so every line has to carry one.

Then open `publications/index.html` and copy the nearest entry. Newest first within a band.

```html
<div class="pub">
  <div class="pub-year">2026</div>
  <div>
    <p class="pub-title"><a href="CANONICAL RECORD">Title exactly as the record prints it</a></p>
    <p class="pub-authors">Outside Author, <a href="/people/#surname">Group Member</a>, Outside Author</p>
    <p class="pub-meta"><span class="venue">Venue</span> volume, article</p>
  </div>
</div>
```

**The citation rules, all of them.** They exist because the list was previously formatted a different way in almost every entry, and one of those ways was wrong about who wrote what.

- **Every author, in the order the record prints them.** No `et al.`, ever. The longest list here is nine names and nine names fit. `et al.` is also how the list previously came to credit six papers to "S. Ayvaz et al." on which he was second, third or last author, which reads as a claim of first authorship.
- **Full first names**, one spelling per person across the whole site. Initials are what let two different people hide behind `R. Terrenzi`.
- **Diacritics stay.** Where a publisher stripped them and another record for the same person keeps them, use the fuller form. A publisher's typesetting is not a person's spelling.
- **Group members are links, nobody is bold.** A name is a group member if and only if it has a card on `people/index.html`; link it to that card's anchor. With seven members on one paper, bolding half an author list is louder than the paper.
- **The venue names its own kind**, so no label is needed: a journal gives its name and volume, a conference its full name with the acronym in brackets, a workshop reads `X workshop at ICML 2026`, and a preprint's venue is `arXiv:2605.10601`. Never write `Preprint` with no identifier, and never write a placeholder like `Journal article`.
- **The title links to one canonical record**: publisher DOI first, then arXiv, then OpenReview. The DOI is never printed as a visible string. If no record exists, the title is not a link, and that absence is the honest signal.
- **The year appears once**, in the `.pub-year` rail, unless the venue's own name carries it.
- **`.tag` is for a distinction only** — an oral, say. Not for the kind of venue, which the venue already states.
- **No citation counts, no h-index, no metrics.**

Before adding an entry, resolve its DOI or arXiv id and copy the authors from what comes back. `https://api.crossref.org/works/<doi>` and `http://export.arxiv.org/api/query?id_list=<id>` both answer without a key.

### Add or change a study

The four studies are sections of `research/index.html`, each under the research line it belongs to. They are not separate pages: four studies on four URLs could not be read side by side, and each one needed a masthead, a pagehead and a footer to carry two hundred words.

Every study carries the same three slots, in this order: **the question**, **what we found**, **the paper**. Where a result has a real falsifier, it goes in the second slot as a sentence about what was checked. It used to have a fourth slot of its own, and three of the four filled it with the finding restated backwards in the past perfect, which said nothing.

A study is listed only once there is a figure to show. Work without one lives on the publications page.

1. Put the figure in `assets/img/figures/`
2. Copy an existing `<div class="study" id="...">` block into the right research line
3. Replace the three slots, and give the block an `id` nothing else uses
4. Add the study to the `.jump` contents list at the top of the page

The `id` matters: the check verifies that every `#fragment` on the site resolves to an element that exists, so a typo fails the build instead of silently dropping the reader at the top of a long page.

**Two copies of four citations.** Each study repeats its paper's citation inside its `.paper` slot, so those four papers are cited on both `/research/` and `/publications/`. Nothing enforces that the two agree, so when a paper's status changes — a preprint gets a DOI, a venue is confirmed — **edit both**. The study copy has no `.pub-year` rail, so its year goes at the end of `pub-meta` (`102, 107227 &middot; 2025`).

**Say whose work it is.** Not everything on the site was done at SDU, and silence on provenance reads as a claim of credit. Two rules decide where an entry goes, and they are about authorship and dates, not about topic:

1. **Serkan Ayvaz and Toygar Tanyel both on a paper → it is the group's**, whatever it is about.
2. **Otherwise, "done at SDU" follows Ayvaz's appointment.** He has been at the Centre for Industrial Software since August 2023. A paper of his from before that is his earlier work, not the group's — which is why the 2021 predictive-maintenance paper sits under *Before and elsewhere* alongside work by members with no Ayvaz co-authorship at all.

The consequence on `/publications/` is the *What members bring* band. On `/research/` the imaging section says outright that the two studies under it were done with clinical teams in Istanbul, and their middle slot reads "What the study found" where the group's own studies read "What we found".

Say it once, in prose, and let a quiet marker carry the rest. An earlier draft also stamped each of those two studies `Earlier study · not SDU work`, which repeated what the paragraph above them already said and put a denial on the card of work that stands perfectly well on its own.

**A link has to earn its place too.** The Pioneer Centre listing was on this page twice: first as a sentence claiming an affiliation no source characterises, then as a link. The link went too, because the destination is 202 characters long — a name, a title, an email and an "Edit this profile" button. It told a reader less than the SDU link directly above it. If that affiliation is substantive, state the substance; a pointer at an empty profile is not evidence of anything.

**Do not claim partners the group does not have.** The centre's remit is research with industry and that is a fact about the centre; it is not evidence that this group has a company partner, a deployment, or a clinical collaboration of its own. Name a collaboration once it exists, never retrospectively. A member's prior industrial or clinical work belongs on that member's own CV, not in the group's description of itself.

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
| `/publications/` | `publications/index.html` |
| `/people/` | `people/index.html` |
| `/join/` | `join/index.html` |

Five pages and a 404. There is no `/work/` and no `/news/`: the four studies are sections of `/research/`, and news was four items, every one of which restated something already on another page.

The only HTML files at the root are `index.html` and `404.html`. Every other page lives in its own directory.

`work/index.html`, `work/*/index.html` and `news/index.html` are the one exception. They are one-line stubs that meta-refresh to where their content went, and they are kept where the old flat `*.html` stubs were not, because these were real pages linked from the nav on every page of the published site. They are the addresses a search engine actually holds, and GitHub Pages cannot rewrite server-side. Anything arriving on any other old address gets `404.html`, which lists every page in the site's own design.

The check verifies that each stub's refresh target and its fragment exist, so a stub pointing somewhere wrong fails the build. A stub that is deleted fails nothing — it just quietly kills the old URL, which is the trade to weigh before removing one.

### Files

```
assets/
  css/site.css     all styling, one file
  js/theme.js      the light and dark control
  img/             photographs, the mark, the favicons
  img/figures/     paper figures used by the studies on /research/
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

### Writing

**One rhetorical move, used sparingly.** An earlier draft of the site made the same move about forty times in four thousand words: assert what something is not, then supply the corrected version. Five of those were headlines. It is a good sentence shape and it stops working the moment a reader notices it, so there is now a budget: roughly one aphorism per page, and none of them in a heading if a plain declarative would carry the same information.

**Do not write about the page.** No sentence should exist only to say that a page is short, is being completed, follows a template, or is comparable to another page. Four study pages each used to close by explaining their own layout.

**Claims about ourselves have to be checkable.** "Everyone here works on something they can explain end to end" cannot be checked by a reader and cannot be false, so it said nothing. A claim about the group either has a source or comes out.

**A person's line comes from a source.** SDU prints a title; use that title, not a nicer one. Where the portal has no research description and the member has not supplied one, the line is left out. An invented topic line is worse than a short card, and no member's card should use a pronoun, because we do not know anyone's pronouns.

### Still to fill in

Nothing on the live site is a placeholder. `class="todo"` exists for marking one, and a page carrying one should not be merged.

One thing worth confirming with the person concerned rather than with a search: Rebecca De Rosa's role, which no public source states.

On titles: the SDU portal prints "Ph.D.-student" in English and `Ph.d.-stipendiat` in Danish. The site uses **PhD Fellow**, which is the group's own wording and the closer reading of the Danish.
