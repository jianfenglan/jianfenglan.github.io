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
- Publication cards do not change background color on hover.
- Publication notes:
  - `1rem` / 16px
  - weight `300`
  - Klein blue `#002FA7`
  - indented beneath the formal publication information
  - curly English quotation marks added via CSS
  - remain Klein blue on hover
- Thin separators remain between adjacent publication entries.

### Blog
- Top section title: `Discendo a doctis, mens augetur`.
- Travel section title: `Makati ang paa`.
- Both titles use the same visual treatment as Blog card titles: 16px, weight 300, `#555a5f`.
- Desktop Blog journal uses a vertical timeline:
  - date on the left, first line
  - place on the left, second line
  - axis and node between metadata and card
  - title centered in the text area of the card
  - image remains on the right
- Timeline card thumbnails are always grayscale.
- Modal images keep their original color.
- Mobile modal leaves tappable empty space around the content so tapping outside closes it.
- Mobile close button is a subtle circular control with a geometrically drawn thin X.
- Travel photo cards are square-cornered.
- Travel photographs remain grayscale by default and return to color on hover.
- Travel captions are left aligned, 16px, weight 300.

## 2. Current style load order

`_includes/head.html` currently loads styles in this order:

1. `assets/css/main.css` compiled from `assets/css/main.scss`
2. `assets/css/v3.4.css`
3. `assets/css/research-refinement.css`
4. `assets/css/blog-refinement.css`
5. `assets/css/ui-unification.css`

The last file currently has the highest intended authority for shared typography, active navigation state, and final Blog thumbnail color behavior.

## 3. Current duplication / conflict risks

### Research duplication
Research styles currently exist in all of the following places:
- inline `<style>` block in `research.md`
- Research rules in `assets/css/main.scss`
- Research overrides in `assets/css/v3.4.css`
- separators in `assets/css/research-refinement.css`
- shared typography rules in `assets/css/ui-unification.css`

Known legacy conflict already encountered:
- `main.scss` contains a wildcard publication hover rule that can turn publication descendants white.
- Later styles currently override this for publication notes and DOI icons.

### Blog duplication
Blog styles currently exist in all of the following places:
- inline `<style>` block in `blog.md`
- inline `<style>` block in `_includes/blog-gallery.html`
- Blog rules in `assets/css/main.scss`
- Blog overrides in `assets/css/v3.4.css`
- final timeline/modal rules in `assets/css/blog-refinement.css`
- shared typography and grayscale-thumbnail rules in `assets/css/ui-unification.css`

This is the main reason recent Blog changes required high-specificity selectors and `!important`.

## 4. Cleanup target architecture

The next maintenance refactor should change CSS ownership without changing the visible design.

### Keep
- `assets/css/main.scss`: theme/base and genuinely site-wide structural styles only.
- `assets/css/research-refinement.css`: single source of truth for all Research-specific styles.
- `assets/css/blog-refinement.css`: single source of truth for all Blog-specific styles.
- `assets/css/ui-unification.css`: only shared typography/navigation/sidebar rules that apply across pages.
- `assets/js/blog-timeline-meta.js`: Blog timeline metadata splitting.

### Remove or migrate
1. Move all Research CSS out of `research.md` into `research-refinement.css`.
2. Remove page-specific Research rules from `main.scss` and `v3.4.css` after their final values have been copied into `research-refinement.css`.
3. Move all Blog CSS out of `blog.md` into `blog-refinement.css`.
4. Move all CSS out of `_includes/blog-gallery.html` into `blog-refinement.css`; keep only travel-gallery HTML there.
5. Remove page-specific Blog rules from `main.scss` and `v3.4.css` after their final values have been copied into `blog-refinement.css`.
6. Once page-specific rules are consolidated, reduce unnecessary `!important` declarations and `html body ...` specificity.
7. Keep `ui-unification.css` small. It should own only:
   - fixed 16px shared interface scale
   - 300 normal shared weight
   - active navigation state
   - sidebar identity typography
   - any truly cross-page shared UI token
8. Consider eventually renaming or retiring `v3.4.css` once its surviving global rules have been merged into a clearly named site-level override file.

## 5. JavaScript cleanup target

After CSS consolidation, optionally move the Blog modal JavaScript currently embedded in `blog.md` into a dedicated external file such as `assets/js/blog-modal.js`. This is not required for the visual refactor, but it would leave `blog.md` as content/markup only.

## 6. Safe cleanup procedure

When performing the consolidation:
1. Fetch every target file immediately before editing.
2. Record the current `main` commit as a rollback point.
3. Change one ownership layer at a time.
4. Preserve visual values exactly during the first pass. Do not redesign while consolidating.
5. After each migration, verify desktop and mobile behavior for Research and Blog.
6. Only delete an old rule after the replacement rule is confirmed loaded later in the cascade.
7. Keep branch `0826` untouched.

## 7. Maintenance rule going forward

For future changes:
- Research visual change -> edit `research-refinement.css`.
- Blog visual change -> edit `blog-refinement.css`.
- Shared navigation/sidebar/interface typography -> edit `ui-unification.css`.
- Do not add new inline `<style>` blocks to `research.md`, `blog.md`, or `_includes/blog-gallery.html`.
- Do not add another generic override CSS layer unless the existing ownership model is insufficient.
