# Useful commands

## Certificates

### Converting `.p12` to `.pem`/`.key`

```bash
openssl pkcs12 -in cert.p12 -out cert.pem -nokeys
openssl pkcs12 -in cert.p12 -out cert.key -nocerts -nodes
```

### Getting info about an x.509 certificate

```bash
openssl x509 -in cert.pem -noout -text
```


## Video

### Making an animated GIF

```bash
ffmpeg -framerate 12 -i frame%04d.png \
  -filter_complex "[1:v] palettegen=reserve_transparent=on:transparency_color=36393F [p]; [0:v][p] paletteuse" \
  -s 85x85 -loop 0 animated.gif
```

### Making an animated WebP

```bash
ffmpeg -framerate 12 -i frame%04d.png -s 85x85 -loop 0 animated.webp
```

### Making an M4V

```bash
ffmpeg -framerate 12 -i frame%04d.png -s 480x258 -crf 18 -pix_fmt yuv420p animated.m4v
```
