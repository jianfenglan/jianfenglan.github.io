"""Research illustrations: a navy block with soft white hand-drawn lines."""
import math, sys
import numpy as np
from scipy.spatial import Voronoi
from sketch import Sketch, NAVY, INK_LIGHT, f

W, H = 600, 360
GOLD = (1 + 5 ** 0.5) / 2
GA = math.pi * (3 - 5 ** 0.5)
BG = (f'<rect width="{W}" height="{H}" fill="{NAVY}"/>'
      f'<rect width="{W}" height="{H}" fill="url(#glow)"/>')
GLOW = ('<radialGradient id="glow" cx="0.5" cy="0.45" r="0.7">'
        '<stop offset="0" stop-color="#2F74C4" stop-opacity="0.5"/>'
        '<stop offset="1" stop-color="#004EA2" stop-opacity="0"/></radialGradient>')


def new(seed):
    s = Sketch(W, H, INK_LIGHT, seed, wobble=0.6)
    s.defs.append(GLOW)
    return s


def ideal_other():
    # Four quadrants of a Fibonacci sunflower, each installed separately,
    # around a hollow centre.
    s = new(1)
    cx, cy, R, n = 300, 180, 132, 520
    for k in range(n):
        r = R * math.sqrt((k + 0.5) / n)
        a = k * GA
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        u, v = (x - cx + y - cy) / 1.414, (x - cx - (y - cy)) / 1.414
        if r < 34 or abs(u) < 8 or abs(v) < 8:
            continue
        q = (u > 0) * 2 + (v > 0)
        s.dot(x, y, 0.8 + 1.5 * r / R, op=[0.9, 0.7, 0.55, 0.42][q])
    for k in range(4):
        a0 = -math.pi / 2 + k * math.pi / 2 + 0.1
        off = [0, 6, -4, 3][k]
        s.line(s.arcpts(cx, cy, R + 16 + off, a0, a0 + math.pi / 2 - 0.2), w=1.4, op=0.85)
    s.circle(cx, cy, 22, w=0.8, op=0.4, dash="2 4")
    return s


def subscribe():
    # Golden-ratio strata of intimacy; one slice of every stratum pulled out:
    # the paid tier.
    s = new(2)
    cx, cy = 280, 182
    radii = [150 / GOLD ** k for k in range(7)]
    a0, a1 = -1.15, -0.25
    mid = (a0 + a1) / 2
    ox, oy = 40 * math.cos(mid), 40 * math.sin(mid)
    for i, R in enumerate(radii):
        op = 0.35 + 0.08 * i
        s.line(s.arcpts(cx, cy, R, a1, a0 + 2 * math.pi), w=1.0 + 0.1 * i, op=min(op, 0.9))
        s.line(s.arcpts(cx + ox, cy + oy, R, a0 + 0.03, a1 - 0.03), w=1.2, op=0.9)
    for a in (a0 + 0.03, a1 - 0.03):
        s.line([(cx + ox, cy + oy), (cx + ox + 150 * math.cos(a), cy + oy + 150 * math.sin(a))], w=1.1, op=0.8)
    for a in (a0, a1):
        s.line([(cx, cy), (cx + 150 * math.cos(a), cy + 150 * math.sin(a))], w=0.8, op=0.4, dash="3 5")
    s.dot(cx + ox * 1.0 + 6 * math.cos(mid), cy + oy + 6 * math.sin(mid), 4, op=0.9)
    return s


def vulnerability():
    # Voronoi cells, the systems a life rests on; a seam opens where they no
    # longer fit, and the cells along it are drawn hardest.
    s = new(3)
    r = np.random.default_rng(3)
    seeds = np.c_[r.random(110) * W, r.random(110) * H]
    fault = np.array([(0, 78), (110, 112), (190, 96), (262, 168), (330, 156),
                      (402, 236), (470, 226), (600, 292)], float)

    def dfault(p):
        d = 1e9
        for a, b in zip(fault, fault[1:]):
            ab = b - a
            t = np.clip(((p - a) @ ab) / (ab @ ab), 0, 1)
            d = min(d, float(np.hypot(*(p - (a + t * ab)))))
        return d
    m = np.vstack([seeds, seeds * [-1, 1], seeds * [1, -1], np.c_[2 * W - seeds[:, 0], seeds[:, 1]],
                   np.c_[seeds[:, 0], 2 * H - seeds[:, 1]]])
    vor = Voronoi(m)
    for (i, j), rv in zip(vor.ridge_points, vor.ridge_vertices):
        if -1 in rv or (i >= len(seeds) and j >= len(seeds)):
            continue
        a, b = vor.vertices[rv[0]], vor.vertices[rv[1]]
        d = dfault((a + b) / 2)
        op = 0.85 if d < 40 else 0.55 if d < 90 else 0.25
        s.line([a, b], w=1.0 if d < 40 else 0.8, op=op)
    s.line(fault + [0, -3], w=1.6, op=0.95)
    s.line(fault + [0, 3], w=1.6, op=0.95)
    for k in range(len(fault) - 1):
        a, b = fault[k], fault[k + 1]
        for t in np.linspace(0.15, 0.85, 4):
            p = a + (b - a) * t
            s.line([p + [0, -3], p + [0, 3]], w=0.7, op=0.6, amp=0)
    return s


def civic():
    # The golden spiral laid on its side: Fibonacci squares, each act of
    # participation built on the last.
    s = new(4)
    sizes = [1, 1, 2, 3, 5, 8, 13, 21, 34]
    rects = [(0, 0, 1)]
    bx0, by0, bx1, by1 = 0, 0, 1, 1
    for i, n in enumerate(sizes[1:], 1):
        d = i % 4
        if d == 1:   rects.append((bx1, by0, n)); bx1 += n
        elif d == 2: rects.append((bx0, by1, n)); by1 += n
        elif d == 3: rects.append((bx0 - n, by1 - n, n)); bx0 -= n
        else:        rects.append((bx1 - n, by0 - n, n)); by0 -= n
    # transpose so the long side is horizontal
    wu, hu = by1 - by0, bx1 - bx0
    sc = min(520 / wu, 300 / hu)
    ox, oy = W / 2 - wu * sc / 2, H / 2 - hu * sc / 2
    for i, (rx, ry, n) in enumerate(rects):
        d = i % 4
        cxu, cyu = {0: (rx + n, ry + n), 1: (rx, ry + n), 2: (rx, ry), 3: (rx + n, ry)}[d]
        # transposed coordinates
        x0, y0, L = ox + (ry - by0) * sc, oy + (rx - bx0) * sc, n * sc
        qx, qy = ox + (cyu - by0) * sc, oy + (cxu - bx0) * sc
        s.poly([(x0, y0), (x0 + L, y0), (x0 + L, y0 + L), (x0, y0 + L)], w=0.8, op=0.4)
        sx = 1 if abs(qx - x0) < 1e-6 else -1
        sy = 1 if abs(qy - y0) < 1e-6 else -1
        a0 = math.atan2(0, sx) if sy == 0 else None
        base = {(1, 1): 0, (-1, 1): math.pi / 2, (-1, -1): math.pi, (1, -1): 1.5 * math.pi}[(sx, sy)]
        s.line(s.arcpts(qx, qy, L, base, base + math.pi / 2), w=1.6, op=0.92)
        if L > 40:
            for k in range(1, 4):
                s.line(s.arcpts(qx, qy, L * (1 - k * 0.07), base + 0.05, base + math.pi / 2 - 0.05),
                       w=0.6, op=0.3)
    return s


def personality():
    # Vesica piscis: the overlap (the relationship) is cross-hatched; the
    # machine's circle is a broken, fading line.
    s = new(5)
    R, ax, bx, cy = 108, 248, 352, 180
    s.raw("")
    clip = (f'<circle cx="{ax}" cy="{cy}" r="{R}"/>')
    s.hatch(clip, 45, 9, 0.7, 0.35)
    inter = s.uid("i")
    s.defs.append(f'<clipPath id="{inter}"><circle cx="{bx}" cy="{cy}" r="{R}"/></clipPath>')
    s.items.append(f'<g clip-path="url(#{inter})">')
    s.hatch(clip, -45, 5, 0.8, 0.75)
    s.items.append("</g>")
    s.circle(ax, cy, R, w=1.5, op=0.92)
    s.line(s.arcpts(bx, cy, R, -math.pi * 0.95, math.pi * 0.95), w=1.1, op=0.5, dash="10 7")
    return s


def jixin():
    # Scattered encounters gather into a sunflower: the same points, given
    # order, form Fibonacci spirals of meaning.
    s = new(6)
    cx, cy, R, n = 405, 180, 140, 560
    for k in range(n):
        r = R * math.sqrt((k + 0.5) / n)
        a = k * GA
        s.dot(cx + r * math.cos(a), cy + r * math.sin(a), 0.7 + 1.8 * (1 - r / R) + 0.3, op=0.45 + 0.45 * (1 - r / R))
    for fam, cnt in ((13, 13),):
        for j in range(cnt):
            pts = []
            for k in range(j, n, fam):
                r = R * math.sqrt((k + 0.5) / n)
                pts.append((cx + r * math.cos(k * GA), cy + r * math.sin(k * GA)))
            s.line(pts, w=0.6, op=0.3, amp=0.2)
    rr = np.random.default_rng(6)
    for _ in range(60):
        x, y = rr.uniform(20, 240), rr.uniform(30, 330)
        s.dot(x, y, rr.uniform(0.8, 2.0), op=rr.uniform(0.25, 0.6))
    return s


def performing():
    # Nested five-petal roses (the self that is shown) above a horizon, and
    # their dashed reflection below.
    s = new(7)
    cx, cy, base = 300, 112, 196
    a = np.linspace(0, 2 * math.pi, 400)
    for i, R in enumerate((92, 74, 56, 38)):
        rr = R * (0.62 + 0.38 * np.cos(5 * a - math.pi / 2))
        s.line(np.c_[cx + rr * np.cos(a), cy + rr * np.sin(a)], w=1.4 - i * 0.15, op=0.92 - i * 0.12)
        my = 2 * base - cy
        s.line(np.c_[cx + rr * np.cos(a), my - rr * np.sin(a)], w=0.8, op=0.32 - i * 0.04, dash="3 5")
    s.dot(cx, cy, 4, op=0.9)
    s.line([(60, base), (540, base)], w=0.9, op=0.55)
    return s


def goodnight():
    # Five moons along a sine arc, waning from a full disc to an empty trace.
    s = new(8)
    R = 36
    xs = np.linspace(95, 505, 5)
    ys = 196 - 84 * np.sin(np.linspace(0.18, math.pi - 0.18, 5))
    shifts = [None, 1.5, 1.0, 0.5, 0.1]
    for i, (x, y) in enumerate(zip(xs, ys)):
        mid = s.uid("m")
        cut = "" if shifts[i] is None else f'<circle cx="{f(x + shifts[i] * R)}" cy="{f(y)}" r="{R}" fill="black"/>'
        s.defs.append(f'<mask id="{mid}"><rect width="{W}" height="{H}" fill="black"/>'
                      f'<circle cx="{f(x)}" cy="{f(y)}" r="{R}" fill="white"/>{cut}</mask>')
        s.items.append(f'<g mask="url(#{mid})">')
        s.hatch(f'<rect width="{W}" height="{H}"/>', 0, 4.2, 0.7, 0.75 - i * 0.08, box=(x - R, y - R, x + R, y + R))
        s.items.append("</g>")
        s.circle(x, y, R, w=1.2, op=0.9 - i * 0.1, dash=None if i < 4 else "4 4")
    for k in range(5):
        y = 300 + k * 10
        s.line([(80 + k * 22, y), (520 - k * 22, y)], w=0.7, op=0.4 - k * 0.06, dash="14 9")
    return s


def gunkel():
    # Two stones dropped into still water: their ripples cross and a moiré of
    # relation appears between them.
    s = new(9)
    for (cx, cy, op0) in ((238, 180, 0.8), (372, 180, 0.65)):
        for k in range(1, 30):
            r = k * 9
            s.circle(cx, cy, r, w=0.75, op=max(0.08, op0 - k * 0.024), amp=0.25)
        s.dot(cx, cy, 3.5, op=0.95)
    return s


def person_thing():
    # Sengai's circle, triangle and square, each hatched in its own direction:
    # where the circle crosses the old categories, the hatching crosses too.
    s = new(10)
    sq = (110, 100, 270, 260)
    tri = [(228, 260), (322, 92), (416, 260)]
    cc, cr = (440, 180), 84
    s.hatch(f'<rect x="{sq[0]}" y="{sq[1]}" width="{sq[2] - sq[0]}" height="{sq[3] - sq[1]}"/>', 45, 8, 0.7, 0.45)
    s.hatch(f'<polygon points="{" ".join(f"{x},{y}" for x, y in tri)}"/>', -45, 8, 0.7, 0.45)
    s.hatch(f'<circle cx="{cc[0]}" cy="{cc[1]}" r="{cr}"/>', 90, 6, 0.7, 0.5)
    s.poly([(sq[0], sq[1]), (sq[2], sq[1]), (sq[2], sq[3]), (sq[0], sq[3])], w=1.3, op=0.9)
    s.poly(tri, w=1.3, op=0.9)
    s.circle(*cc, cr, w=1.6, op=0.95)
    return s


def methods():
    # Scattered rays gather through a narrow lens and leave as an ordered
    # field: the instrument has become part of the laboratory.
    s = new(11)
    cx, cy = 300, 180
    rr = np.random.default_rng(11)
    for i in range(19):
        y0 = 30 + i * 16.5 + rr.uniform(-9, 9)
        x0 = 30 + rr.uniform(0, 90)
        s.dot(x0, y0, 1.8, op=0.7)
        s.line([(x0, y0), (cx - 4, cy + (i - 9) * 1.1)], w=0.8, op=0.55)
        yt = 30 + i * 16.5
        s.line([(cx + 4, cy + (i - 9) * 1.1), (410, yt), (570, yt)], w=0.8, op=0.75)
    s.line(s.arcpts(cx, cy + 74, 86, -math.pi * 0.66, -math.pi * 0.34), w=1.6, op=0.95)
    s.line(s.arcpts(cx, cy - 74, 86, math.pi * 0.34, math.pi * 0.66), w=1.6, op=0.95)
    s.dot(cx, cy, 5, op=0.95)
    return s


def stereotype():
    # A single point branches level by level into a widening fractal fan.
    s = new(12)

    def grow(x, y, ang, L, depth):
        if depth == 0:
            s.dot(x, y, 1.4, op=0.7)
            return
        x2, y2 = x + L * math.cos(ang), y + L * math.sin(ang)
        s.line([(x, y), (x2, y2)], w=0.6 + 0.22 * (7 - depth), op=0.45 + 0.07 * (7 - depth) if depth < 7 else 0.9)
        sp = 0.3 - 0.012 * (7 - depth)
        grow(x2, y2, ang - sp, L * 0.74, depth - 1)
        grow(x2, y2, ang + sp, L * 0.74, depth - 1)
    s.dot(50, 180, 3.5, op=0.95)
    grow(60, 180, 0, 112, 7)
    return s


PIECES = {
    "ideal-other": ideal_other, "subscribe-to-intimacy": subscribe,
    "provincializing-vulnerability": vulnerability, "civic-engagement": civic,
    "personality-machine": personality, "jishi-jixin": jixin,
    "performing-intimacy": performing, "good-night-goodbye": goodnight,
    "gunkel-interview": gunkel, "person-thing-robot": person_thing,
    "ai-research-methods": methods, "gender-machine-writing": stereotype,
}

if __name__ == "__main__":
    for name, fn in PIECES.items():
        svg = fn().svg(BG).replace('stroke-width=', 'vector-effect="non-scaling-stroke" stroke-width=')
        open(f"{sys.argv[1]}/{name}.svg", "w").write(svg)
    print("ok")
