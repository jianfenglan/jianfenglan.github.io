"""Street-and-water line maps for Plog note previews, from Overture Maps
(OpenStreetMap-derived) data, read straight from the public S3 bucket."""
import math, os, pickle, sys
import pyarrow.dataset as ds
import pyarrow.fs as pafs
import pyarrow.compute as pc
import shapely
from shapely import wkb

REL = "overturemaps-us-west-2/release/2026-09-23.1"
FS = pafs.S3FileSystem(anonymous=True, region="us-west-2")
CACHE = os.path.join(os.path.dirname(__file__), "mapcache")

# name: (lon, lat, width_km)
CITIES = {
    "BNU":       (113.578, 22.268, 6.5),    # Zhuhai, Xiangzhou coast
    "PKUSZ":     (114.058, 22.537, 6.0),    # Shenzhen, Futian
    "ICA2026":   (18.423, -33.922, 6.0),    # Cape Town, City Bowl
    "NCA25":     (-104.990, 39.745, 7.0),   # Denver
    "PCST":      (139.755, 35.682, 6.0),    # Tokyo, around the Imperial Palace
    "HKBU25":    (114.170, 22.292, 6.0),    # Hong Kong, Victoria Harbour
    "AEJMC25":   (-122.418, 37.785, 6.0),   # San Francisco
    "IAMCR2025": (103.852, 1.288, 5.5),     # Singapore, Marina Bay
    "ICA2025":   (-104.985, 39.735, 3.2),   # Denver downtown, closer in
    "NCA":       (-90.068, 29.955, 5.5),    # New Orleans, the river bend
    "ICA2024":   (153.425, -28.000, 6.0),   # Gold Coast, Surfers Paradise
    "SICSS01":   (103.778, 1.298, 5.0),     # Singapore, Kent Ridge (NUS)
    "ICA2302":   (-79.385, 43.648, 6.0),    # Toronto, downtown and lakeshore
}

ROAD_CLASSES = {"motorway": 3, "trunk": 3, "primary": 3, "secondary": 2, "tertiary": 2,
                "residential": 1, "unclassified": 1, "living_street": 1}


def bbox(lon, lat, wkm, aspect=7 / 5):
    dlon = wkm / (111.32 * math.cos(math.radians(lat)))
    dlat = (wkm / aspect) / 110.57
    return lon - dlon / 2, lat - dlat / 2, lon + dlon / 2, lat + dlat / 2


def query(theme, typ, bb, cols):
    d = ds.dataset(f"{REL}/theme={theme}/type={typ}", filesystem=FS, format="parquet")
    x0, y0, x1, y1 = bb
    f = ((pc.field("bbox", "xmin") < x1) & (pc.field("bbox", "xmax") > x0) &
         (pc.field("bbox", "ymin") < y1) & (pc.field("bbox", "ymax") > y0))
    return d.to_table(filter=f, columns=cols).to_pylist()


def fetch(name):
    os.makedirs(CACHE, exist_ok=True)
    p = os.path.join(CACHE, name + ".pkl")
    if os.path.exists(p):
        return pickle.load(open(p, "rb"))
    lon, lat, wkm = CITIES[name]
    bb = bbox(lon, lat, wkm)
    roads = query("transportation", "segment", bb, ["geometry", "subtype", "class"])
    water = query("base", "water", bb, ["geometry", "subtype", "class"])
    land = query("base", "land", bb, ["geometry", "subtype", "class"])
    data = {"bb": bb, "roads": roads, "water": water, "land": land}
    pickle.dump(data, open(p, "wb"))
    return data


if __name__ == "__main__":
    for n in (sys.argv[1:] or CITIES):
        d = fetch(n)
        print(n, len(d["roads"]), len(d["water"]), len(d["land"]), flush=True)
