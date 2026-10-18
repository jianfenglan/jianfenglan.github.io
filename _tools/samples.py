"""Three design samples for the research figures.

Language (after the Lieflat/Lupi editorial grammar): white ground, hairlines,
one repeated unit, quiet "furniture" (ledger lines, dashed guides, ticks),
flat grey offset shapes for depth, a single accent: #004EA2.
"""
import math, sys
import numpy as np

W, H = 600, 360
BLUE = "#004EA2"
G1, G2, G3 = "#EEF0F3", "#DDE1E6", "#B9C0C9"   # grey ladder (shadow / surfaces)
INK2 = "#8A94A1"                               # secondary hairline


def f(v):
    return f"{v:.2f}"


class SVG:
    def __init__(self):
        self.defs, self.body = [], []
        self.n = 0

    def uid(self, p):
        self.n += 1
        return f"{p}{self.n}"

    def add(self, s):
        self.body.append(s)

    def line(self, pts, w=0.7, c=BLUE, op=1, dash=None):
        d = "M" + " L".join(f"{f(x)},{f(y)}" for x, y in pts)
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-opacity="{op}"{da}/>')

    def poly(self, pts, fill, op=1, stroke=None, w=0.7):
        d = "M" + " L".join(f"{f(x)},{f(y)}" for x, y in pts) + "Z"
        st = f' stroke="{stroke}" stroke-width="{w}"' if stroke else ' stroke="none"'
        self.add(f'<path d="{d}" fill="{fill}" fill-opacity="{op}"{st}/>')

    def circle(self, cx, cy, r, fill="none", stroke=None, w=0.7, op=1):
        st = f' stroke="{stroke}" stroke-width="{w}"' if stroke else ""
        self.add(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{fill}" fill-opacity="{op}"{st}/>')

    def out(self):
        body = "".join(self.body).replace('stroke-width=', 'vector-effect="non-scaling-stroke" stroke-width=')
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
                f'preserveAspectRatio="xMidYMid meet" aria-hidden="true">'
                f'<defs>{"".join(self.defs)}</defs><rect width="{W}" height="{H}" fill="#FFFFFF"/>'
                f'<g stroke-linecap="round" stroke-linejoin="round">{body}</g></svg>\n')


def arc(cx, cy, r, a0, a1, n=48):
    a = np.linspace(a0, a1, n)
    return np.c_[cx + r * np.cos(a), cy + r * np.sin(a)]


# ---------------------------------------------------------------------------
# 1. Good Night versus Goodbye — a lunar calendar. Moons wax and wane and come
#    back: the language of "good night", not "goodbye". One moon is rendered in
#    pixels: the virtual uploader whose "hibernation" was mourned like a death.

def moon_shape(cx, cy, r, phase):
    """Lit region polygon for phase in [0,1): 0 new, .5 full."""
    k = math.cos(2 * math.pi * phase)          # 1 new -> -1 full
    waxing = phase < 0.5
    t = np.linspace(-math.pi / 2, math.pi / 2, 40)
    limb = np.c_[np.cos(t), np.sin(t)] * r      # right limb
    term = np.c_[k * np.cos(t[::-1]), np.sin(t[::-1])] * r   # terminator ellipse
    pts = np.vstack([limb, term])
    if not waxing:
        pts[:, 0] = -pts[:, 0]
    return pts + [cx, cy]


def good_night():
    s = SVG()
    cols, rows = 10, 3
    x0, y0, dx, dy, r = 66, 86, 52, 84, 15
    # furniture: ledger lines and dashed guides
    for j in range(rows):
        y = y0 + j * dy + r + 16
        s.line([(40, y), (W - 40, y)], w=0.5, c=G3)
    for i in (0, 5, 10):
        x = x0 + i * dx - dx / 2
        s.line([(x, 52), (x, H - 44)], w=0.5, c=G3, dash="2 4")
    n = 0
    special = (1, 6)
    for j in range(rows):
        for i in range(cols):
            cx, cy = x0 + i * dx, y0 + j * dy
            phase = (n / 29.5) % 1.0
            n += 1
            # flat grey shadow disc
            s.circle(cx + 3.5, cy + 4, r, fill=G2)
            s.circle(cx, cy, r, fill="#FFFFFF", stroke=BLUE, w=0.7)
            if (j, i) == special:
                # pixel moon: the virtual body
                g = 3.0
                for gy in np.arange(-r, r, g):
                    for gx in np.arange(-r, r, g):
                        px, py = cx + gx + g / 2, cy + gy + g / 2
                        if math.hypot(px - cx, py - cy) > r - 0.5:
                            continue
                        lit = (px - cx) > r * math.cos(2 * math.pi * phase) * math.sqrt(max(0, 1 - ((py - cy) / r) ** 2))
                        if lit:
                            s.add(f'<rect x="{f(cx + gx + 0.35)}" y="{f(cy + gy + 0.35)}" width="{f(g - 0.7)}" '
                                  f'height="{f(g - 0.7)}" fill="{BLUE}"/>')
                # leader line + tick, the editorial side-note (no words)
                s.line([(cx + r + 4, cy - r - 4), (cx + r + 26, cy - r - 26), (cx + r + 56, cy - r - 26)], w=0.6, c=BLUE)
                s.circle(cx + r + 56, cy - r - 26, 1.8, fill=BLUE)
            elif 0.03 < phase < 0.97:
                s.poly(moon_shape(cx, cy, r, phase), BLUE)
            # day tick under each moon
            s.line([(cx, cy + r + 12), (cx, cy + r + 20)], w=0.6, c=INK2)
    return s.out()


# ---------------------------------------------------------------------------
# 2. Subscribe to Intimacy — a bundle of hairline strands (the relationship)
#    passes through curved grey surfaces (payment tiers). At each surface some
#    strands stop: memory, availability, expressiveness, identity, each gated.

def subscribe():
    s = SVG()
    xs = np.linspace(30, 570, 360)
    N = 44
    panels = [170, 270, 370, 470]
    keep = [44, 28, 16, 8, 3]
    # curved grey surfaces (drawn first, strands pass over them)
    for k, px in enumerate(panels):
        top, bot = 46 + k * 10, 314 - k * 10
        bend = 26
        left = [(px - 14 + bend * math.sin(math.pi * t), top + (bot - top) * t) for t in np.linspace(0, 1, 30)]
        right = [(px + 14 + bend * math.sin(math.pi * t), top + (bot - top) * t) for t in np.linspace(1, 0, 30)]
        s.poly([(x + 6, y + 6) for x, y in left + right], G1)          # offset shadow
        s.poly(left + right, [G2, G2, G1, G1][k], stroke=G3, w=0.5)
    # a flat ribbon that twists as it travels: strand i sits at offset u_i
    # across the ribbon; the ribbon's apparent width is |cos| of the twist.
    mid = 182 + 46 * np.sin(xs / 95 - 0.6)
    width = 62 * np.cos(xs / 70 + 0.4)
    for idx in range(N):
        u = (idx / (N - 1)) * 2 - 1
        y = mid + u * width + 6 * np.sin(xs / 40) * (1 - abs(u))
        passed = sum(idx_rank < kk for kk in keep[1:]) if (idx_rank := abs(idx - (N - 1) / 2) * 2) is not None else 0
        full = passed == len(panels)
        end_x = 570 if full else panels[passed] + 2
        m = xs <= end_x
        pts = np.c_[xs[m], y[m]]
        s.line(pts, w=0.6, c=BLUE, op=0.95 if full else 0.5)
        if not full:
            s.circle(pts[-1][0], pts[-1][1], 1.4, fill=BLUE, op=0.75)
    # furniture: baseline ticks under each tier
    for px in [30] + panels + [570]:
        s.line([(px, 330), (px, 338)], w=0.6, c=INK2)
    s.line([(30, 334), (570, 334)], w=0.5, c=G3)
    return s.out()


# ---------------------------------------------------------------------------
# 3. From jishi to jixin — repeated leaves. Left to right the encounter
#    deepens: an outline (mere exposure), a midrib, full veins, veins that turn
#    into circuitry, and finally one solid leaf: meaning taken in.

def leaf_outline(cx, cy, L, wdt, ang):
    t = np.linspace(0, 1, 40)
    half = wdt * np.sin(np.pi * t) ** 0.75 * (1 - 0.3 * t)
    top = np.c_[t * L - L / 2, -half]
    bot = np.c_[(t * L - L / 2)[::-1], half[::-1]]
    P = np.vstack([top, bot])
    c, s_ = math.cos(ang), math.sin(ang)
    R = np.array([[c, -s_], [s_, c]])
    return P @ R.T + [cx, cy], R


def leaves():
    s = SVG()
    cols, rows = 8, 3
    x0, y0, dx, dy = 70, 78, 66, 102
    L, wd = 58, 12.5
    for j in range(rows):
        s.line([(36, y0 + j * dy + 38), (W - 36, y0 + j * dy + 38)], w=0.5, c=G3)
    for j in range(rows):
        for i in range(cols):
            cx, cy = x0 + i * dx, y0 + j * dy
            ang = -math.pi / 4 + (0.12 if (i + j) % 2 else -0.08)
            P, R = leaf_outline(cx, cy, L, wd, ang)
            stage = min(5, int((i + (j * 0.5)) / 1.6))
            last = (i == cols - 1 and j == 1)
            s.poly(P + [3.5, 4.5], G2)                                   # flat shadow
            s.poly(P, BLUE if last else "#FFFFFF", stroke=BLUE, w=0.8)
            # stem
            base = np.array([-L / 2, 0]) @ R.T + [cx, cy]
            stem = np.array([-L / 2 - 9, 2]) @ R.T + [cx, cy]
            s.line([base, stem], w=0.8, c=BLUE)
            if last:
                continue
            col = BLUE
            if stage >= 1:
                a = np.array([-L / 2, 0]) @ R.T + [cx, cy]
                b = np.array([L / 2 - 4, 0]) @ R.T + [cx, cy]
                s.line([a, b], w=0.6, c=col)
            if stage in (2, 3):
                for k in range(1, 6):
                    u = -L / 2 + k * L / 6.5
                    hw = wd * math.sin(math.pi * (u + L / 2) / L) * 0.82
                    for sg in (-1, 1):
                        p0 = np.array([u, 0]) @ R.T + [cx, cy]
                        p1 = np.array([u + 7, sg * hw]) @ R.T + [cx, cy]
                        s.line([p0, p1], w=0.5, c=col, op=0.9)
            if stage >= 4:
                # veins become circuitry: orthogonal runs ending in pads
                for k in range(1, 5):
                    u = -L / 2 + k * L / 5.2
                    hw = wd * math.sin(math.pi * (u + L / 2) / L) * 0.7
                    for sg in (-1, 1):
                        p0 = np.array([u, 0]) @ R.T + [cx, cy]
                        p1 = np.array([u, sg * hw * 0.55]) @ R.T + [cx, cy]
                        p2 = np.array([u + 6, sg * hw]) @ R.T + [cx, cy]
                        s.line([p0, p1, p2], w=0.5, c=col)
                        s.circle(p2[0], p2[1], 1.1, fill=BLUE)
    return s.out()


if __name__ == "__main__":
    out = sys.argv[1]
    for name, fn in (("good-night-goodbye", good_night), ("subscribe-to-intimacy", subscribe),
                     ("jishi-jixin", leaves)):
        open(f"{out}/{name}.svg", "w").write(fn())
    print("ok")
