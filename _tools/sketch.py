"""Hand-drawn line library: wobbly strokes, curves, hatching."""
import math
import numpy as np

NAVY = "#004EA2"
NAVY_LIGHT = "#2A4069"
INK_LIGHT = "#EEF1F6"


def f(v):
    return f"{v:.1f}"


class Sketch:
    def __init__(self, W, H, ink, seed=0, wobble=0.7):
        self.W, self.H, self.ink = W, H, ink
        self.r = np.random.default_rng(seed)
        self.wob = wobble
        self.items = []
        self.defs = []
        self._id = 0

    def uid(self, p="c"):
        self._id += 1
        return f"{p}{self._id}"

    # ---- geometry to point lists
    @staticmethod
    def bez(p0, p1, p2, p3, n=40):
        t = np.linspace(0, 1, n)[:, None]
        p0, p1, p2, p3 = map(np.array, (p0, p1, p2, p3))
        return ((1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3)

    @staticmethod
    def arcpts(cx, cy, r, a0, a1, n=None, ry=None):
        ry = r if ry is None else ry
        n = n or max(8, int(abs(a1 - a0) * max(r, ry) / 3))
        a = np.linspace(a0, a1, n)
        return np.c_[cx + r * np.cos(a), cy + ry * np.sin(a)]

    def resample(self, pts, step=3.0):
        pts = np.asarray(pts, float)
        if len(pts) < 2:
            return pts
        seg = np.hypot(*np.diff(pts, axis=0).T)
        L = np.r_[0, np.cumsum(seg)]
        if L[-1] == 0:
            return pts
        n = max(2, int(L[-1] / step))
        s = np.linspace(0, L[-1], n)
        return np.c_[np.interp(s, L, pts[:, 0]), np.interp(s, L, pts[:, 1])]

    def wobble(self, pts, amp=None):
        amp = self.wob if amp is None else amp
        p = self.resample(pts)
        if amp <= 0 or len(p) < 3:
            return p
        n = len(p)
        noise = self.r.normal(0, 1, (n, 2))
        k = min(7, n)
        ker = np.ones(k) / k
        noise = np.c_[np.convolve(noise[:, 0], ker, "same"), np.convolve(noise[:, 1], ker, "same")]
        return p + noise * amp * 1.6

    # ---- drawing
    def line(self, pts, w=1.0, op=1.0, dash=None, amp=None, color=None, double=False):
        for k in range(2 if double else 1):
            p = self.wobble(pts, amp)
            d = "M" + " L".join(f"{f(x)},{f(y)}" for x, y in p)
            da = f' stroke-dasharray="{dash}"' if dash else ""
            o = op if k == 0 else op * 0.45
            self.items.append(f'<path d="{d}" fill="none" stroke="{color or self.ink}" '
                              f'stroke-width="{w if k == 0 else w * 0.7}" stroke-opacity="{o:.2f}"{da}/>')

    def poly(self, pts, closed=True, **kw):
        pts = list(map(tuple, np.asarray(pts, float)))
        if closed:
            pts = pts + [pts[0]]
        self.line(pts, **kw)

    def circle(self, cx, cy, r, **kw):
        self.line(self.arcpts(cx, cy, r, 0, 2 * math.pi + 0.15), **kw)

    def dot(self, cx, cy, r, op=1.0, color=None):
        self.items.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{color or self.ink}" fill-opacity="{op:.2f}"/>')

    def fill(self, pts, op=1.0, color=None):
        p = " ".join(f"{f(x)},{f(y)}" for x, y in pts)
        self.items.append(f'<polygon points="{p}" fill="{color or self.ink}" fill-opacity="{op:.2f}"/>')

    def hatch(self, clip_svg, angle=45, gap=5, w=0.6, op=0.5, box=None, color=None):
        """Parallel hatching clipped to an SVG shape string (in local coords)."""
        cid = self.uid("h")
        self.defs.append(f'<clipPath id="{cid}">{clip_svg}</clipPath>')
        x0, y0, x1, y1 = box or (0, 0, self.W, self.H)
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        R = math.hypot(x1 - x0, y1 - y0) / 2 + 2
        a = math.radians(angle)
        dx, dy = math.cos(a), math.sin(a)
        nx, ny = -dy, dx
        out = []
        k = -R
        while k <= R:
            px, py = cx + nx * k, cy + ny * k
            pts = [(px - dx * R, py - dy * R), (px + dx * R, py + dy * R)]
            p = self.wobble(pts, 0.35)
            out.append("M" + " L".join(f"{f(x)},{f(y)}" for x, y in p))
            k += gap
        self.items.append(f'<g clip-path="url(#{cid})"><path d="{" ".join(out)}" fill="none" '
                          f'stroke="{color or self.ink}" stroke-width="{w}" stroke-opacity="{op}"/></g>')

    def raw(self, s):
        self.items.append(s)

    def svg(self, bg):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.W} {self.H}" '
                f'preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
                f'<defs>{"".join(self.defs)}</defs>{bg}'
                f'<g stroke-linecap="round" stroke-linejoin="round">' + "".join(self.items) + "</g></svg>\n")
