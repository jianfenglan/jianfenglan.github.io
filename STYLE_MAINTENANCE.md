# Website Style Maintenance

This file is the maintenance source of truth for the current public site on `main`.
Do not modify the archive branch `0826`.

## 1. Current final visual state

### Shared UI
- Base interface font size for navigation, sidebar identity text, Blog section headings, Blog timeline labels/titles, and travel captions: `1rem` / 16px.
- Normal interface weight: `300`.
- Klein blue: `#002FA7`.
- Standard text tone: `#555a5f`.
- Muted text tone: `#737980`.
- Active navigation item: Klein blue, weight `500`.

### Research
- Publication layout remains the existing two-column year/type + publication-information structure on desktop and single-column on mobile.
- Publication cards remain visually static on hover.
- Publication notes remain 16px, weight 300, Klein blue, indented beneath the formal publication information, and wrapped in curly English quotation marks via CSS.
- Thin separators remain between adjacent publication entries.

### Blog
- Top section title: `Notes`.
- Travel section title: `Footprints`.
- Both section titles are Klein blue and weight `500`.
- Desktop Blog journal uses the current vertical timeline with date/place left of the axis and the image on the right.
- Timeline card thumbnails are always grayscale.
- Cards retain their current subtle lift and shadow on desktop hover and remain static on mobile.
- Modal images keep their original color and the modal retains its flat, shadowless treatment.
- Mobile modal leaves tappable empty space around the content so tapping outside closes it.
- Mobile close button remains a subtle circular control with a geometrically drawn thin X.
- Travel photographs remain grayscale by default and return to color on hover.
- Travel captions remain left aligned, 16px, weight 300.

## 2. Current style architecture

`_includes/head.html` loads styles in this order:

1. `assets/css/main.css` compiled from `assets/css/main.scss`
2. `assets/css/research-refinement.css`
3. `assets/css/blog-refinement.css`
4. `assets/css/ui-unification.css`

`assets/css/v3.4.css` was retired on 2026-08-31 after its surviving rules were migrated to the correct ownership layers.

Ownership:
- `main.scss`: theme/base, global 300 typography, identity rail, About/home layout, and shared structural primitives.
- `research-refinement.css`: current Research interaction, publication-note, marker, DOI, and separator behavior.
- `blog-refinement.css`: current Blog card, timeline, modal, and responsive behavior.
- `ui-unification.css`: final shared interface scale, active navigation state, Blog/Research section-heading treatment, and final Blog image-color behavior.

## 3. Cleanup completed on 2026-08-31

- Removed the redundant custom `.github/workflows/pages.yml` deployment pipeline. GitHub's native `pages build and deployment` is now the single Pages deployment path.
- Removed unused `assets/js/collapse.js` and `assets/css/collapse.css`.
- Removed the unused duplicate `assets/css/academicons.min.css`.
- Changed `assets/js/blog-timeline-meta.js` to load only on `/blog/`.
- Removed superseded base CSS rules that existed only to be overridden later.
- Migrated active global/About rules from `v3.4.css` into `main.scss`.
- Migrated active Research rules from `v3.4.css` into `research-refinement.css`.
- Migrated active Blog rules from `v3.4.css` into `blog-refinement.css`.
- Retired and deleted `assets/css/v3.4.css`.
- Refreshed stylesheet cache-busting query strings after consolidation.

## 4. Remaining duplication to handle cautiously

The main remaining technical debt is page-local CSS that predates the dedicated refinement files.

### Research
Research styling still exists partly in:
- inline `<style>` in `research.md`
- structural rules in `main.scss`
- final rules in `research-refinement.css`
- shared typography in `ui-unification.css`

### Blog
Blog styling still exists partly in:
- inline `<style>` in `blog.md`
- inline `<style>` in `_includes/blog-gallery.html`
- structural rules in `main.scss`
- final rules in `blog-refinement.css`
- shared typography/image rules in `ui-unification.css`

These inline blocks should eventually be migrated, but only after comparing their computed final values against the current live rendering. Do not move them mechanically into the head because their current position in the cascade can affect precedence.

## 5. Next cleanup target

A second, visual-regression-controlled pass may:
1. migrate Research inline CSS into `research-refinement.css`;
2. migrate Blog inline CSS from `blog.md` and `_includes/blog-gallery.html` into `blog-refinement.css`;
3. remove page-specific structural rules from `main.scss` once the dedicated files fully own those pages;
4. reduce unnecessary `!important` and `html body ...` specificity only after the cascade is flattened;
5. optionally move the Blog modal JavaScript from `blog.md` into a Blog-only external script;
6. audit large image assets and add lazy-loading/responsive image handling without changing composition.

## 6. Safe maintenance procedure

1. Fetch every target file immediately before editing.
2. Change one ownership layer at a time.
3. Preserve current visual values exactly during cleanup. Do not redesign while consolidating.
4. Confirm the native Pages deployment succeeds after each structural change.
5. Verify desktop and mobile behavior for About, Research, and Blog before deleting replacement-covered rules.
6. Keep branch `0826` untouched as an archival reference.

## 7. Maintenance rule going forward

- Research visual change -> edit `research-refinement.css` unless the rule is genuinely shared.
- Blog visual change -> edit `blog-refinement.css` unless the rule is genuinely shared.
- Shared navigation/sidebar/interface typography -> edit `ui-unification.css`.
- Theme/base/About/shared layout -> edit `main.scss`.
- Do not add another generic versioned override stylesheet.
- Do not add new inline `<style>` blocks to page content.
