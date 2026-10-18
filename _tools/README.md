# Illustration tools (not published: Jekyll skips `_`-prefixed folders)

- `citymap.py` + `maprender.py` — Plog note previews. `citymap.py` reads roads/water/land
  for each city's bounding box from the public Overture Maps S3 bucket (OSM-derived) and caches
  them; `maprender.py <outdir>` draws the street-and-water SVGs now in `images/news/previews/`.
  Needs `pip install pyarrow shapely`. Data © OpenStreetMap contributors (credit is on /plog/).
- `research_lines.py` + `sketch.py` — the current Research figures (white lines on #004EA2).
  The owner is not satisfied with these; they are being redesigned.
- `samples.py` — three design samples for the redesign (lunar calendar, ribbon through tiers,
  leaves turning into circuitry): white ground, #004EA2 hairlines, flat grey offset shadows.
