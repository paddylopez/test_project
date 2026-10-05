# Unseated

Level concept for a mid-size shooter map set inside a damaged gaming PC, scaled against Call of Duty 4's Crash.

- [Crash, to scale](https://claude.ai/artifact/NFAdbkFf7FQWGY3GYxfmdy): how big Crash is and how big the player is in it.
- [Unseated blockout](https://claude.ai/artifact/Thfej2pik3mf2joV3NdVMU): the three-level lane map on a graphics card at 357× scale.

`CLAUDE.md` holds the design numbers, open decisions and next steps, so a Claude Code session started in this
folder picks up where the last one stopped.

## Rebuild the Crash measurements

```sh
git clone --depth 1 https://github.com/ineedbots/cod4x_bot_warfare
python tools/measure_cod4_maps.py cod4x_bot_warfare/scriptdata/waypoints
```
