"""Measure CoD4 multiplayer maps from Bot Warfare waypoint files.

Waypoints are spots a player can stand, recorded in engine units (1 unit = 1 inch).
Their extents give each map's walkable footprint; the wall-to-wall size is a little larger.

Usage:
    git clone --depth 1 https://github.com/ineedbots/cod4x_bot_warfare
    python measure_cod4_maps.py cod4x_bot_warfare/scriptdata/waypoints
    python measure_cod4_maps.py cod4x_bot_warfare/scriptdata/waypoints --export-crash out.json
"""

import argparse
import json
import math
from pathlib import Path

STOCK_MAPS = [
    "shipment", "killhouse", "showdown", "vacant", "bog", "crash", "backlot",
    "carentan", "citystreets", "broadcast", "crossfire", "convoy", "countdown",
    "strike", "bloc", "farm", "overgrown", "pipeline", "cargoship", "creek",
]
INCH_TO_M = 0.0254


def load_waypoints(path):
    """Return (points, edges) from a Bot Warfare CSV: first line is the count."""
    rows = path.read_text().strip().splitlines()[1:]
    points, edges = [], set()
    for i, row in enumerate(rows):
        fields = row.split(",")
        points.append(tuple(float(v) for v in fields[0].split()))
        for j in fields[1].split():
            j = int(j)
            edges.add((min(i, j), max(i, j)))
    return points, sorted(edges)


def extents(points):
    xs, ys, zs = zip(*points)
    return max(xs) - min(xs), max(ys) - min(ys), max(zs) - min(zs)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("waypoint_dir", type=Path)
    ap.add_argument("--export-crash", type=Path, help="write mp_crash points and links, shifted to start at 0")
    args = ap.parse_args()

    print(f"{'map':<12} {'units (x × y)':>15} {'feet':>13} {'metres':>15} {'height ft':>9}")
    for name in STOCK_MAPS:
        path = args.waypoint_dir / f"mp_{name}_wp.csv"
        if not path.exists():
            continue
        dx, dy, dz = extents(load_waypoints(path)[0])
        print(f"{name:<12} {dx:7.0f} × {dy:<5.0f} {dx / 12:5.0f} × {dy / 12:<5.0f} "
              f"{dx * INCH_TO_M:6.1f} × {dy * INCH_TO_M:<6.1f} {dz / 12:9.0f}")

    if args.export_crash:
        points, edges = load_waypoints(args.waypoint_dir / "mp_crash_wp.csv")
        mins = [min(p[k] for p in points) for k in range(3)]
        shifted = [[round(p[k] - mins[k]) for k in range(3)] for p in points]
        args.export_crash.write_text(json.dumps({"pts": shifted, "edges": edges}, separators=(",", ":")))
        longest = max(math.dist(points[a], points[b]) for a, b in edges)
        print(f"wrote {len(points)} points and {len(edges)} links to {args.export_crash} (longest link {longest:.0f} units)")


if __name__ == "__main__":
    main()
