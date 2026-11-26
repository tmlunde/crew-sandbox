"""Winch drum for the camera winch (PHO-21).

A plain barrel with a flange at each end and a through bore.
The flanges sit outside the barrel ends, so the overall length is
BARREL_LENGTH + 2 * FLANGE_THICKNESS.

Run:  python cad/winch_drum.py
Writes out/winch_drum.step, out/winch_drum.stl and out/winch_drum_drawing.svg.
"""

import math
from pathlib import Path

import cadquery as cq

# ---- sizes (mm) -------------------------------------------------------------
BARREL_DIAMETER = 40.0
BARREL_LENGTH = 60.0
FLANGE_DIAMETER = 64.0
FLANGE_THICKNESS = 4.0
BORE_DIAMETER = 10.0

# ---- material ---------------------------------------------------------------
MATERIAL = "6061 aluminium"
DENSITY_KG_M3 = 2700.0

# ---- output -----------------------------------------------------------------
OUT_DIR = Path(__file__).resolve().parent.parent / "out"
NAME = "winch_drum"
STL_TOLERANCE = 0.05  # mm chord deviation
STL_ANGULAR_TOLERANCE = 0.1  # rad

OVERALL_LENGTH = BARREL_LENGTH + 2 * FLANGE_THICKNESS


def build() -> cq.Workplane:
    """Drum along +Z, starting at Z=0."""
    flange_a = cq.Workplane("XY").circle(FLANGE_DIAMETER / 2).extrude(FLANGE_THICKNESS)
    barrel = (
        cq.Workplane("XY")
        .workplane(offset=FLANGE_THICKNESS)
        .circle(BARREL_DIAMETER / 2)
        .extrude(BARREL_LENGTH)
    )
    flange_b = (
        cq.Workplane("XY")
        .workplane(offset=FLANGE_THICKNESS + BARREL_LENGTH)
        .circle(FLANGE_DIAMETER / 2)
        .extrude(FLANGE_THICKNESS)
    )
    bore = cq.Workplane("XY").circle(BORE_DIAMETER / 2).extrude(OVERALL_LENGTH)
    return flange_a.union(barrel).union(flange_b).cut(bore)


def mass_g(part: cq.Workplane) -> tuple[float, float]:
    """(volume mm^3, mass g) from the solid itself."""
    volume_mm3 = part.val().Volume()
    return volume_mm3, volume_mm3 * 1e-9 * DENSITY_KG_M3 * 1000.0


def drawing_svg(volume_mm3: float, mass: float) -> str:
    """Side section and end view, scale 2:1, on a 420 x 297 sheet (A3, mm)."""
    s = 2.0  # drawing scale
    W, H = 420, 297
    rb, rf, rh = BARREL_DIAMETER / 2, FLANGE_DIAMETER / 2, BORE_DIAMETER / 2
    L, t = OVERALL_LENGTH, FLANGE_THICKNESS

    # side view (half section above the axis), axis horizontal
    x0, cy = 40, 130  # left end of the part, axis line
    X = lambda z: x0 + z * s  # noqa: E731
    Y = lambda r: cy - r * s  # noqa: E731

    def outline(sign):
        r0 = rh if sign > 0 else 0.0  # section cuts at the bore; plain view runs to the axis
        pts = [(0, r0), (0, rf), (t, rf), (t, rb), (t + BARREL_LENGTH, rb),
               (t + BARREL_LENGTH, rf), (L, rf), (L, r0)]
        return " ".join(f"{X(z):.2f},{cy - sign * r * s:.2f}" for z, r in pts)

    hatch_id = "hatch"
    parts = []
    a = parts.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" '
      f'viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif">')
    a('<defs>'
      f'<pattern id="{hatch_id}" width="3" height="3" patternUnits="userSpaceOnUse" '
      'patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="3" stroke="#444" stroke-width="0.3"/></pattern>'
      '<marker id="ar" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="4" markerHeight="4" '
      'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#000"/></marker>'
      '</defs>')
    a(f'<rect width="{W}" height="{H}" fill="#fff"/>')
    a(f'<rect x="10" y="10" width="{W-20}" height="{H-20}" fill="none" stroke="#000" stroke-width="0.7"/>')

    line = 'stroke="#000" stroke-width="0.5" fill="none"'
    thin = 'stroke="#000" stroke-width="0.25" fill="none"'
    centre = 'stroke="#000" stroke-width="0.25" stroke-dasharray="8,2,1,2" fill="none"'

    # upper half: section (hatched), lower half: plain view
    a(f'<polygon points="{outline(+1)}" fill="url(#{hatch_id})" stroke="#000" stroke-width="0.5"/>')
    a(f'<polyline points="{outline(-1)}" {line}/>')
    # lower half view edges: bore hidden lines and flange faces
    a(f'<line x1="{X(0)}" y1="{cy + rh*s}" x2="{X(L)}" y2="{cy + rh*s}" stroke="#000" '
      'stroke-width="0.3" stroke-dasharray="3,1.5"/>')
    for z in (t, t + BARREL_LENGTH):
        a(f'<line x1="{X(z)}" y1="{cy + rb*s}" x2="{X(z)}" y2="{cy + rf*s}" {line}/>')
    a(f'<line x1="{X(0)}" y1="{cy - rh*s}" x2="{X(L)}" y2="{cy - rh*s}" {line}/>')
    a(f'<line x1="{X(-6)}" y1="{cy}" x2="{X(L+6)}" y2="{cy}" {centre}/>')
    a(f'<text x="{X(L/2)}" y="{Y(rf)-48}" font-size="5" text-anchor="middle">SIDE VIEW — upper half in section</text>')

    def hdim(z1, z2, yy, label, ext_from):
        a(f'<line x1="{X(z1)}" y1="{ext_from}" x2="{X(z1)}" y2="{yy-2 if yy < ext_from else yy+2}" {thin}/>')
        a(f'<line x1="{X(z2)}" y1="{ext_from}" x2="{X(z2)}" y2="{yy-2 if yy < ext_from else yy+2}" {thin}/>')
        a(f'<line x1="{X(z1)}" y1="{yy}" x2="{X(z2)}" y2="{yy}" {thin} '
          'marker-start="url(#ar)" marker-end="url(#ar)"/>')
        a(f'<text x="{(X(z1)+X(z2))/2}" y="{yy-1.5}" font-size="4.5" text-anchor="middle">{label}</text>')

    def vdim(xx, r1, r2, label, ext_from):
        a(f'<line x1="{ext_from}" y1="{Y(r1)}" x2="{xx+2}" y2="{Y(r1)}" {thin}/>')
        a(f'<line x1="{ext_from}" y1="{Y(r2)}" x2="{xx+2}" y2="{Y(r2)}" {thin}/>')
        a(f'<line x1="{xx}" y1="{Y(r1)}" x2="{xx}" y2="{Y(r2)}" {thin} '
          'marker-start="url(#ar)" marker-end="url(#ar)"/>')
        ym = (Y(r1) + Y(r2)) / 2
        a(f'<text x="{xx-1.5}" y="{ym}" font-size="4.5" text-anchor="middle" '
          f'transform="rotate(-90 {xx-1.5} {ym})">{label}</text>')

    # horizontal dims above
    top = Y(rf)
    hdim(0, t, top - 10, f"{FLANGE_THICKNESS:g}", top)
    hdim(L - t, L, top - 10, f"{FLANGE_THICKNESS:g}", top)
    hdim(t, t + BARREL_LENGTH, Y(rb) - 8, f"{BARREL_LENGTH:g} barrel", Y(rb))
    hdim(0, L, top - 24, f"{OVERALL_LENGTH:g} overall", top)
    # diameters to the right
    right = X(L)
    vdim(right + 16, -rb, rb, f"Ø{BARREL_DIAMETER:g} barrel", X(t + BARREL_LENGTH))
    vdim(right + 32, -rf, rf, f"Ø{FLANGE_DIAMETER:g} flange", right)

    # end view
    ex, ey = 330, cy
    a(f'<circle cx="{ex}" cy="{ey}" r="{rf*s}" {line}/>')
    a(f'<circle cx="{ex}" cy="{ey}" r="{rb*s}" stroke="#000" stroke-width="0.3" '
      'stroke-dasharray="3,1.5" fill="none"/>')
    a(f'<circle cx="{ex}" cy="{ey}" r="{rh*s}" {line}/>')
    a(f'<line x1="{ex-rf*s-6}" y1="{ey}" x2="{ex+rf*s+6}" y2="{ey}" {centre}/>')
    a(f'<line x1="{ex}" y1="{ey-rf*s-6}" x2="{ex}" y2="{ey+rf*s+6}" {centre}/>')
    a(f'<text x="{ex}" y="{Y(rf)-48}" font-size="5" text-anchor="middle">END VIEW</text>')
    # bore callout with a leader at 45 degrees
    c45 = math.cos(math.radians(45))
    lx0, ly0 = ex - rh * s * c45, ey + rh * s * c45  # lower-left, clear of the frame
    lx1, ly1 = ex - (rf + 5) * s * c45, ey + (rf + 5) * s * c45
    a(f'<line x1="{lx1}" y1="{ly1}" x2="{lx0}" y2="{ly0}" {thin} marker-end="url(#ar)"/>')
    a(f'<line x1="{lx1}" y1="{ly1}" x2="{lx1-38}" y2="{ly1}" {thin}/>')
    a(f'<text x="{lx1-1}" y="{ly1-1.5}" font-size="4.5" text-anchor="end">'
      f'Ø{BORE_DIAMETER:g} bore through</text>')

    # notes and title block
    notes = [
        f"Barrel Ø{BARREL_DIAMETER:g} × {BARREL_LENGTH:g} long",
        f"Flanges Ø{FLANGE_DIAMETER:g} × {FLANGE_THICKNESS:g} thick, one at each barrel end",
        f"Bore Ø{BORE_DIAMETER:g} through, full {OVERALL_LENGTH:g} length",
        f"Overall length {OVERALL_LENGTH:g}",
        "All dimensions in mm. Scale 2:1. Sharp edges: break 0.2 (not modelled).",
    ]
    for i, n in enumerate(notes):
        a(f'<text x="20" y="{222 + i*7}" font-size="4.5">{n}</text>')

    bx, by, bw, bh = 250, 222, 160, 65
    a(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" fill="none" stroke="#000" stroke-width="0.5"/>')
    rows = [
        ("Part", "Winch drum — camera winch"),
        ("Task", "PHO-21"),
        ("Material", MATERIAL),
        ("Density", f"{DENSITY_KG_M3:g} kg/m³"),
        ("Volume", f"{volume_mm3/1000:.2f} cm³"),
        ("Mass", f"{mass:.1f} g"),
        ("File", f"cad/{NAME}.py"),
    ]
    rh_ = bh / len(rows)
    for i, (k, v) in enumerate(rows):
        yy = by + i * rh_
        if i:
            a(f'<line x1="{bx}" y1="{yy}" x2="{bx+bw}" y2="{yy}" {thin}/>')
        a(f'<text x="{bx+3}" y="{yy+rh_*0.68}" font-size="4.2" fill="#555">{k}</text>')
        weight = ' font-weight="bold"' if k in ("Part", "Mass") else ""
        a(f'<text x="{bx+32}" y="{yy+rh_*0.68}" font-size="4.6"{weight}>{v}</text>')
    a(f'<line x1="{bx+29}" y1="{by}" x2="{bx+29}" y2="{by+bh}" {thin}/>')
    a('</svg>')
    return "\n".join(parts)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    drum = build()
    volume, mass = mass_g(drum)

    step = OUT_DIR / f"{NAME}.step"
    stl = OUT_DIR / f"{NAME}.stl"
    svg = OUT_DIR / f"{NAME}_drawing.svg"
    cq.exporters.export(drum, str(step))
    cq.exporters.export(drum, str(stl), tolerance=STL_TOLERANCE,
                        angularTolerance=STL_ANGULAR_TOLERANCE)
    svg.write_text(drawing_svg(volume, mass), encoding="utf-8")

    # analytic check of the solid's volume
    expected = math.pi * (
        (BARREL_DIAMETER**2 - BORE_DIAMETER**2) / 4 * BARREL_LENGTH
        + 2 * (FLANGE_DIAMETER**2 - BORE_DIAMETER**2) / 4 * FLANGE_THICKNESS
    )
    assert abs(volume - expected) < 1e-3 * expected, (volume, expected)

    bb = drum.val().BoundingBox()
    print(f"bbox: {bb.xlen:.2f} x {bb.ylen:.2f} x {bb.zlen:.2f} mm")
    print(f"volume: {volume:.1f} mm^3  mass: {mass:.1f} g ({MATERIAL}, {DENSITY_KG_M3:g} kg/m^3)")
    for p in (step, stl, svg):
        print(f"wrote {p.relative_to(OUT_DIR.parent)}")


if __name__ == "__main__":
    main()
