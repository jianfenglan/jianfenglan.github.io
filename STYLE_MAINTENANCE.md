# Website Style Maintenance

This file is the maintenance source of truth for the current public site on `main`.
Do not modify the archive branch `0826`.

## 1. Visual baseline

The cleanup completed on 2026-08-31 is architecture-only. Existing public layout, typography, spacing, hover behavior, modal behavior, timeline composition, grayscale treatment, and mobile behavior are the visual baseline.

Shared UI:
- Klein blue: `#002FA7`
- normal interface weight: `300`
- active navigation weight: `500`
- standard text tone: `#555a5f`
- muted text tone: `#737980`

Research:
- section titles are Klein blue, 16px, weight 500
- desktop publications use the existing two-column layout; mobile uses one column
- publication cards remain visually static on hover
- publication notes remain Klein blue, 16px, weight 300, indented, with CSS curly quotation marks
- separators remain between adjacent publication entries

Blog:
- section titles are `Notes` and `Footprints`, Klein blue, weight 500
- desktop journal remains a vertical timeline with metadata left of the axis and image thumbnails on the right
- timeline thumbnails remain grayscale
- desktop cards retain their subtle lift/shadow; mobile cards remain static
- modal images remain in color and the modal remains flat/shadowless
- mobile outside-tap close behavior and circular close control remain unchanged
- Footprints images remain grayscale until hover and captions remain left aligned

## 2. Final asset architecture

Global assets loaded on every page:
1. `assets/css/main.css` compiled from `assets/css/main.scss`
2. `assets/css/ui-unification.css`

Research only:
- `assets/css/research-refinement.css`

Blog only:
- `assets/css/blog-refinement.css`
- `assets/js/blog-timeline-meta.js`
- `assets/js/blog-modal.js`

Ownership:
- `main.scss`: theme/base, global typography, navigation-independent shared layout, sidebar, About/home, Elsewhere/gallery primitives
- `ui-unification.css`: navigation and sidebar interface normalization only
- `research-refinement.css`: all Research-specific layout, typography, publication interaction, notes, DOI icons, conference items, and responsive rules
- `blog-refinement.css`: all Blog-specific cards, timeline, modal, Footprints gallery, and responsive rules
- `research.md`: Research content/markup only
- `blog.md`: Blog journal content/markup only
- `_includes/blog-gallery.html`: Footprints markup only

## 3. Cleanup completed on 2026-08-31

- removed the redundant failing custom Pages workflow; GitHub native Pages deployment is the single deployment path
- retired and deleted `assets/css/v3.4.css`
- removed duplicate/superseded Research and Blog rules from `main.scss`
- moved all Research inline CSS into `research-refinement.css`
- moved all Blog inline CSS from `blog.md` and `_includes/blog-gallery.html` into `blog-refinement.css`
- reduced `ui-unification.css` to genuinely shared navigation/sidebar rules
- extracted Blog modal JavaScript to `assets/js/blog-modal.js`
- made Blog CSS and JS load only on `/blog/`
- made Research CSS load only on `/research/`
- removed unused collapse JS/CSS
- removed unused Academicons CSS and font assets
- removed unused global MathJax/polyfill loading
- refreshed cache-busting query strings

## 4. Maintenance rules

- Research visual changes -> `assets/css/research-refinement.css`
- Blog visual changes -> `assets/css/blog-refinement.css`
- navigation/sidebar interface changes -> `assets/css/ui-unification.css`
- shared theme, About, Elsewhere, or global layout changes -> `assets/css/main.scss`
- Research content changes -> `research.md`
- Blog journal content changes -> `blog.md`
- Footprints content changes -> `_includes/blog-gallery.html`
- Blog modal behavior -> `assets/js/blog-modal.js`
- Blog timeline metadata transformation -> `assets/js/blog-timeline-meta.js`

Do not add page-local `<style>` or `<script>` blocks. Do not add generic versioned override stylesheets. Prefer changing the owning file directly.

## 5. Deployment

The site uses GitHub's native `pages build and deployment` workflow. A push to `main` should produce one Pages deployment path. Any future persistent second deployment workflow should be treated as unintended configuration drift.
