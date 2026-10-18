"""Render cached Overture data as a quiet street-and-water line map (SVG)."""
import math, os, pickle, sys
import shapely
from shapely import wkb
from shapely.geometry import box as sbox
from citymap import CITIES, CACHE

W, H = 420, 300
INK = "#004EA2"
WATER = "#D5E3F4"
WATER_LINE = "#9DBBE3"

ROAD = {  # class: (tier)
    "motorway": 3, "trunk": 3, "primary": 3,
    "secondary": 2, "tertiary": 2,
    "residential": 1, "unclassified": 1, "living_street": 1, "pedestrian": 1,
}
STYLE = {3: (1.6, 0.88), 2: (1.0, 0.7), 1: (0.5, 0.42)}
WATER_AREA = {"ocean", "lake", "river", "water", "bay", "reservoir", "canal", "pond",
              "basin", "lagoon", "strait", "dock", "harbour", "moat", "oxbow", "fishpond"}
WATER_LINE_CLS = {"river", "stream", "canal"}


def project(bb):
    x0, y0, x1, y1 = bb
    def f(x, y):
        return (x - x0) / (x1 - x0) * W, (y1 - y) / (y1 - y0) * H
    return f


def path_d(geom, f, closed=False):
    out = []
    def ring(coords):
        pts = [f(x, y) for x, y in coords]
        s = "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in pts)
        out.append(s + ("Z" if closed else ""))
    g = geom
    if g.is_empty:
        return ""
    if g.geom_type in ("LineString", "LinearRing"):
        ring(g.coords)
    elif g.geom_type == "Polygon":
        ring(g.exterior.coords)
        for i in g.interiors:
            ring(i.coords)
    elif hasattr(g, "geoms"):
        for p in g.geoms:
            out.append(path_d(p, f, closed))
    return " ".join(x for x in out if x)


def render(name):
    d = pickle.load(open(os.path.join(CACHE, name + ".pkl"), "rb"))
    bb = d["bb"]
    clip = sbox(*bb)
    f = project(bb)
    tol = (bb[2] - bb[0]) / W * 0.6  # ~0.6px simplification
    water_polys, water_lines = [], []
    for r in d["water"]:
        g = wkb.loads(r["geometry"])
        cls, sub = r["class"], r["subtype"]
        if g.geom_type in ("Polygon", "MultiPolygon") and (cls in WATER_AREA or sub in WATER_AREA):
            if cls in ("swimming_pool", "reflecting_pool", "fountain"):
                continue
            g = shapely.make_valid(g).intersection(clip)
            if not g.is_empty and g.area > (bb[2] - bb[0]) * (bb[3] - bb[1]) * 0.0004:
                water_polys.append(g.simplify(tol))
        elif g.geom_type in ("LineString", "MultiLineString") and sub in WATER_LINE_CLS:
            g = g.intersection(clip)
            if not g.is_empty:
                water_lines.append(g.simplify(tol))
    # sea: whatever the coastline-derived land polygons leave uncovered
    lands = [shapely.make_valid(wkb.loads(r["geometry"])) for r in d["land"]
             if r["subtype"] == "land" and wkb.loads(r["geometry"]).geom_type in ("Polygon", "MultiPolygon")]
    if lands:
        land = shapely.union_all([g.intersection(clip) for g in lands])
        if 0 < land.area < clip.area * 0.995:
            sea = clip.difference(land)
            if sea.area > clip.area * 0.002:
                water_polys.append(sea.simplify(tol))
    tiers = {1: [], 2: [], 3: []}
    for r in d["roads"]:
        if r["subtype"] != "road":
            continue
        t = ROAD.get(r["class"])
        if not t:
            continue
        g = wkb.loads(r["geometry"]).intersection(clip)
        if not g.is_empty:
            tiers[t].append(g.simplify(tol))
    parts = [f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>']
    if water_polys:
        merged = shapely.union_all([shapely.make_valid(g) for g in water_polys])
        merged = shapely.make_valid(merged.buffer(0)).simplify(tol)
        polys = [g for g in getattr(merged, "geoms", [merged]) if g.geom_type in ("Polygon", "MultiPolygon")]
        dd = " ".join(path_d(g, f, True) for g in polys)
        parts.append(f'<path d="{dd}" fill="{WATER}" fill-rule="evenodd" stroke="none"/>')
    if water_lines:
        dd = " ".join(path_d(g, f) for g in water_lines)
        parts.append(f'<path d="{dd}" fill="none" stroke="{WATER_LINE}" stroke-width="1.2"/>')
    for t in (1, 2, 3):
        w, op = STYLE[t]
        dd = " ".join(path_d(g, f) for g in tiers[t])
        if dd:
            parts.append(f'<path d="{dd}" fill="none" stroke="{INK}" stroke-opacity="{op}" stroke-width="{w}"/>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
           f'preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
           f'<g stroke-linecap="round" stroke-linejoin="round">' + "".join(parts) + "</g></svg>\n")
    return svg.replace('stroke-width=', 'vector-effect="non-scaling-stroke" stroke-width=')


if __name__ == "__main__":
    out = sys.argv[1]
    names = sys.argv[2:] or [n for n in CITIES if os.path.exists(os.path.join(CACHE, n + ".pkl"))]
    for n in names:
        s = render(n)
        open(f"{out}/{n}.svg", "w").write(s)
        print(n, len(s) // 1024, "KB")
