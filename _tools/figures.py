"""Research figures, redesigned (white ground, one accent #004EA2, grey for depth).

Visual grammar follows the Lieflat/Lupi editorial gallery: hairlines, one repeated
unit, deterministic jitter (rnd), quiet "furniture" (ledger lines, ticks, dashed
guides) and flat grey offset shapes instead of soft shadows.

The figures are shown ~210px wide, so the 600x360 viewBox is drawn at ~0.35x:
stroke widths are in screen px (non-scaling-stroke) and nothing that must be
read is closer than ~9 units (3 screen px) to its neighbour.

    python3 _tools/figures.py images/research [name ...]
"""
import math, sys
import numpy as np

W, H = 600, 360
BLUE = "#004EA2"
G1, G2, G3, G4 = "#F1F2F4", "#E3E6EA", "#C9CED5", "#9AA3AE"   # grey ladder
SH = (5, 6)                                                    # flat shadow offset


def f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def rnd(i, k):
    """Deterministic pseudo-random in [0,1) (same idea as MONO.rnd)."""
    x = math.sin(i * 127.1 + k * 311.7) * 43758.5453
    return x - math.floor(x)


class SVG:
    def __init__(self):
        self.body = []

    def add(self, s):
        self.body.append(s)

    def line(self, pts, w=0.8, c=BLUE, op=1, dash=None, cap="round"):
        d = "M" + "L".join(f"{f(x)},{f(y)}" for x, y in pts)
        da = f' stroke-dasharray="{dash}"' if dash else ""
        o = f' stroke-opacity="{op}"' if op != 1 else ""
        self.add(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}"{o}{da} stroke-linecap="{cap}"/>')

    def poly(self, pts, fill, op=1, stroke=None, w=0.8):
        d = "M" + "L".join(f"{f(x)},{f(y)}" for x, y in pts) + "Z"
        st = f' stroke="{stroke}" stroke-width="{w}"' if stroke else ""
        o = f' fill-opacity="{op}"' if op != 1 else ""
        self.add(f'<path d="{d}" fill="{fill}"{o}{st}/>')

    def circle(self, cx, cy, r, fill="none", stroke=None, w=0.8, op=1):
        st = f' stroke="{stroke}" stroke-width="{w}"' if stroke else ""
        o = f' fill-opacity="{op}"' if op != 1 else ""
        self.add(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{fill}"{o}{st}/>')

    def rect(self, x, y, w, h, fill, op=1):
        o = f' fill-opacity="{op}"' if op != 1 else ""
        self.add(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" fill="{fill}"{o}/>')

    def out(self):
        body = "".join(self.body).replace(" stroke-width=", ' vector-effect="non-scaling-stroke" stroke-width=')
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" aria-hidden="true">'
                f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>'
                f'<g stroke-linejoin="round">{body}</g></svg>\n')


def shift(pts, d=SH):
    return [(x + d[0], y + d[1]) for x, y in pts]


# ---------------------------------------------------------------------------
# Good Night versus Goodbye — a lunar calendar of 30 moons that wax, wane and
# return: the grammar of "good night". The full moon at the centre is made of
# pixels, a few of them drifting loose: the virtual body that went to sleep.

def moon_lit(cx, cy, r, phase, n=36):
    """Lit region for phase in [0,1): 0 new, .5 full; light comes from the right while waxing."""
    k = math.cos(2 * math.pi * phase)
    t = np.linspace(-math.pi / 2, math.pi / 2, n)
    limb = np.c_[np.cos(t), np.sin(t)] * r
    term = np.c_[k * np.cos(t[::-1]), np.sin(t[::-1])] * r
    pts = np.vstack([limb, term])
    if phase >= 0.5:
        pts[:, 0] = -pts[:, 0]
    return pts + [cx, cy]


def good_night():
    s = SVG()
    cols, rows = 10, 3
    dx, dy, r = 52, 92, 17
    x0 = (W - (cols - 1) * dx) / 2
    y0 = (H - (rows - 1) * dy) / 2 - 4
    special = 15                                  # day 15 of the cycle: full moon
    for j in range(rows):                         # ledger lines + day ticks
        y = y0 + j * dy + r + 20
        s.line([(x0 - 30, y), (W - x0 + 30, y)], w=0.6, c=G3)
        for i in range(cols):
            s.line([(x0 + i * dx, y - 5), (x0 + i * dx, y)], w=0.7, c=G4)
    for j in range(rows):
        for i in range(cols):
            n = j * cols + i
            cx, cy = x0 + i * dx, y0 + j * dy
            phase = (n / 29.53) % 1.0
            s.circle(cx + SH[0], cy + SH[1], r, fill=G2)
            if n == special:
                g = 2 * r / 6
                for a in range(6):
                    for b in range(6):
                        px, py = cx - r + (a + .5) * g, cy - r + (b + .5) * g
                        if math.hypot(px - cx, py - cy) > r + 1:
                            continue
                        loose = a >= 4 and b <= 2 and rnd(a, b) > .35
                        if loose:                 # pixels drifting up and out
                            ox, oy = 14 + 22 * rnd(a, b + 7), -10 - 20 * rnd(a + 3, b)
                            s.rect(px - g / 2 + ox, py - g / 2 + oy, g - 1.4, g - 1.4, BLUE, op=.45)
                            s.rect(px - g / 2 + 0.7, py - g / 2 + 0.7, g - 1.4, g - 1.4, G3)
                        else:
                            s.rect(px - g / 2 + 0.7, py - g / 2 + 0.7, g - 1.4, g - 1.4, BLUE)
                continue
            s.circle(cx, cy, r, fill="#FFFFFF", stroke=BLUE, w=0.8)
            if 0.025 < phase < 0.975:
                s.poly(moon_lit(cx, cy, r, phase), BLUE)
    return s.out()


# ---------------------------------------------------------------------------
# Subscribe to Intimacy — a twisting ribbon of twelve strands (the relationship)
# runs through four grey surfaces (payment tiers). Each surface cuts some strands
# off: memory, availability, expressiveness, relational identity. One strand
# makes it through.

def subscribe():
    s = SVG()
    xs = np.linspace(28, 572, 500)
    N = 12
    walls = [200, 300, 400, 500]
    alive_after = [12, 8, 5, 3, 1]                 # strands left in each segment
    order = sorted(range(N), key=lambda i: abs(i - (N - 1) / 2) + 0.01 * i)   # outer strands die first
    mid = 196 - 0.1 * (xs - 28) + 14 * np.sin((xs - 28) / 120)

    def smooth(x, a, b):
        z = np.clip((x - a) / (b - a), 0, 1)
        return z * z * (3 - 2 * z)

    # one full half twist in open air, a second slow one among the paid tiers
    theta = np.pi * smooth(xs, 40, 175) + np.pi * smooth(xs, 300, 470)
    hw = 66

    def wall_geom(k):
        top, bot, bend = 58 + 10 * k, 318 - 10 * k, 16
        return top, bot, bend

    def wall_left(k, y):
        top, bot, bend = wall_geom(k)
        tt = (y - top) / (bot - top)
        return walls[k] - 9 + bend * math.sin(math.pi * tt)

    for idx in range(N):
        u = (idx / (N - 1)) * 2 - 1
        X = xs + u * hw * np.sin(theta) * 0.45      # the edge-on ribbon leans in depth
        Y = mid + u * hw * np.cos(theta)
        rank = order.index(idx)
        seg = max(k for k in range(5) if rank < alive_after[k])   # walls it passes
        if seg < 4:
            m = X <= np.array([wall_left(seg, y) - 7 for y in Y])
            m = np.cumprod(m).astype(bool)
        else:
            m = X <= 572
        s.line(np.c_[X[m], Y[m]], w=0.9 if seg == 4 else 0.75)
        if seg < 4:
            s.circle(X[m][-1], Y[m][-1], 2.6, fill=BLUE)
    # tiers drawn over the strands, translucent, so strands read as passing through
    for k, px in enumerate(walls):
        top, bot, bend = wall_geom(k)
        tt = np.linspace(0, 1, 28)
        left = [(px - 9 + bend * math.sin(math.pi * t_), top + (bot - top) * t_) for t_ in tt]
        P = left + [(x + 18, y) for x, y in left[::-1]]
        s.poly(shift(P), G2, op=.9)
        s.poly(P, [G1, G1, G2, G2][k], op=.82, stroke=G4, w=0.6)
    return s.out()


# ---------------------------------------------------------------------------
# From jishi to jixin — eighteen leaves in a repeat pattern. Read left to right:
# an outline (mere contact), a midrib, veins, veins straightening into circuit
# traces, and finally one solid leaf: meaning taken in.

def leaf(cx, cy, L, wd, ang):
    t = np.linspace(0, 1, 44)
    hw = wd * np.sin(np.pi * t) ** 0.8 * (1 - 0.25 * t)
    P = np.vstack([np.c_[t * L - L / 2, -hw], np.c_[(t * L - L / 2)[::-1], hw[::-1]]])
    c, s_ = math.cos(ang), math.sin(ang)
    R = np.array([[c, -s_], [s_, c]])
    return P @ R.T + [cx, cy], (lambda u, v: np.array([u, v]) @ R.T + [cx, cy])


def leaves():
    s = SVG()
    cols, rows = 6, 3
    dx, dy = 88, 104
    x0 = (W - (cols - 1) * dx - dx / 2) / 2
    y0 = (H - (rows - 1) * dy) / 2
    L, wd = 76, 17
    total = cols * rows

    def hw(u):                                      # leaf half-width at u in [-L/2, L/2]
        t_ = u / L + .5
        return wd * math.sin(math.pi * t_) ** 0.8 * (1 - 0.25 * t_)

    for j in range(rows):
        for i in range(cols):
            n = j * cols + i
            cx, cy = x0 + i * dx + (dx / 2 if j % 2 else 0), y0 + j * dy
            P, T = leaf(cx, cy, L, wd, -math.radians(52))
            last = n == total - 1
            stage = 5 if last else min(4, int(n / (total - 1) * 5))
            s.poly(shift(P), G2)
            s.poly(P, BLUE if last else "#FFFFFF", stroke=BLUE, w=0.9)
            s.line([T(-L / 2, 0), T(-L / 2 - 11, 2)], w=0.9)
            if last or stage == 0:
                continue
            s.line([T(-L / 2, 0), T(L / 2 - 7, 0)], w=0.75)          # midrib
            for u0 in ([-.24, -.02, .2] if stage >= 2 else []):
                u, u1 = u0 * L, (u0 + .15) * L
                for sg in (-1, 1):
                    if stage == 2 or (stage == 3 and u0 > 0):      # organic vein
                        s.line([T(u, 0), T(u + .07 * L, sg * hw(u1) * .5), T(u1, sg * hw(u1) * .78)], w=0.7)
                    else:                                          # circuit trace
                        a, b, c = T(u, 0), T(u, sg * hw(u) * .45), T(u1 - .04 * L, sg * hw(u1) * .72)
                        s.line([a, b, c], w=0.7)
                        if stage == 4:
                            s.circle(c[0], c[1], 2.1, fill=BLUE)
    return s.out()


FIGURES = {
    "good-night-goodbye": good_night,
    "subscribe-to-intimacy": subscribe,
    "jishi-jixin": leaves,
}

if __name__ == "__main__":
    out = sys.argv[1]
    for name in sys.argv[2:] or FIGURES:
        open(f"{out}/{name}.svg", "w").write(FIGURES[name]())
    print("ok")
