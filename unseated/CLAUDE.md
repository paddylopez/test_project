# Unseated (working title)

A mid-size multiplayer map set inside a damaged gaming PC. The graphics card is torn out of its
slot and lies fans-up on the PSU shroud; the player is millimetres tall. Sized against Call of
Duty 4's Crash (2007), which the owner considers the reference for flow and scale.

## Where things stand

- `reference/crash-scale.html`: Crash measured from in-game coordinates. Live: https://claude.ai/artifact/NFAdbkFf7FQWGY3GYxfmdy
- `reference/unseated-blockout.html`: plan, sections, lanes, off-limits, scale table. Live: https://claude.ai/artifact/Thfej2pik3mf2joV3NdVMU
- `data/mp_crash_waypoints.json`: Crash's 224 bot waypoints and 351 links, units shifted to start at 0.
- `tools/measure_cod4_maps.py`: reproduces every CoD4 map measurement from the Bot Warfare CSVs.

The `.html` files are artifact sources (no `<html>`/`<head>` wrapper). They still open in a browser.

## Fixed numbers

- CoD4 player: hull 30 × 30 × 70 units, eyes at 60, jump 39, run 190 units/s, sprint 1.5× for 4 s.
  1 unit = 1 inch, so 1.78 m tall, 4.8 m/s run, 7.2 m/s sprint. Source: CoD4x server defaults.
- Crash walkable footprint: 2,730 × 4,276 units = 69 × 109 m. Highest standing spot 47 ft (14.3 m).
- Blockout scale: 357×, so the card's length matches Crash's long side and the player is 5 mm tall.

## Blockout layout (metres, from `unseated-blockout.html`)

X runs along the card (rear of case and Team A at 0); Y runs across (motherboard at 0, side glass at 68).

| Element | Geometry |
|---|---|
| Card (FE-size, 304 × 137 × 40 mm) | x 0–108.6, y 9–57.9 |
| Cable alley, floor 0 m | y 0–9, full length |
| Glass lane, floor 0 m | y 57.9–68, full length |
| Spawns | A: x −10–0, B: x 108.6–118.6 |
| Board crater, 1.8 m | x 38–70.6, y 9–57.9 |
| GPU package / die | 18 × 18 m (+0.7 m) / 10 × 10 m (+0.3 m), centred x 54.3, y 33.45 |
| Fan decks, 14.3 m | x 0–38 and 70.6–108.6; pit r 16 at x 19 and 89.6, y 33.45; hub r 5.5 |
| Heatpipe bridges, 14.3 m | 2.9 m wide at y 20 and y 46.9, spanning the crater |
| Heatpipe ramps | 24 × 2.9 m from the board up to each deck (alley side to rear, glass side to front) |
| Spawn ramps | A: bracket ramp, rect x −7, y 16, 3 × 34 m. B: power-cable ramp, its mirror |

The layout is rotationally symmetric: (x, y) maps to (108.6 − x, 66.9 − y).
Off-limits: fin stacks, fan pits, fan hubs, under the shroud, outside the case.

## Open decisions

1. **Card size.** The owner wants a big flagship, about 358 × 149 × 76 mm (ROG Astral RTX 5090 class).
   Proposed: drop to 304× so the card stays Crash-sized (109 × 45 m, player 5.85 mm). Decks then sit
   about 23 m up, so add a middle level around 12 m. Not yet confirmed.
2. **Engine.** Recommended Unreal 5 with baked lighting; Godot 4 as the simpler fallback. Not yet confirmed.

## Next steps

1. Build the greybox in Blender by script (`bpy`), modelled in metres, one object per walkable piece.
   Use `UCX_` prefixed hulls for Unreal custom collision. Export FBX or glTF.
2. Write an Unreal Python script that imports it, sets collision, and places player starts and lights.
3. Walk it at the CoD4 speeds above and check the timings in the blockout page (spawn to die about 11–12 s).
4. Art pass: hard-surface parts first (they suit scripting), then materials, then damage and lighting.

## Target hardware

- Dev PC: Radeon RX 9070 XT (16 GB), Ryzen 7 5800X3D, 64 GB RAM.
- Goal: looks good at 4K without flagship hardware. That card is well above the target, so profile with
  the internal resolution and settings a mid-range card would use. AMD has no DLSS: use Unreal's TSR or FSR.
- Keep it cheap: enclosed space with no sky, so bake the lighting; instance repeated parts; Nanite for fin stacks.
