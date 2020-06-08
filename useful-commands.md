# Useful commands

## Video

## Making an animated GIF

```bash
ffmpeg -framerate 12 -i frame%04d.png \
  -filter_complex "[1:v] palettegen=reserve_transparent=on:transparency_color=36393F [p]; [0:v][p] paletteuse" \
  -s 85x85 -loop 0 animated.gif
```

## Making an animated WebP

```bash
ffmpeg -framerate 12 -i frame%04d.png -s 85x85 -loop 0 animated.webp
```
