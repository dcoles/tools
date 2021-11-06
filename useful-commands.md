# Useful commands

## Debugging

### GDB debug symbols

```gdb
# May also require setting `safe-path`
set debug-file-directory /path
```

### GDB backtrace

```gdb
bt; info proc; info sharedlib; info target; info registers; x/16i $pc; info threads; thread apply all bt
```

### Generate coredump

```gdb
generate-core-file
```

### Who sent SIGKILL

```bash
tpoint signal:signal_generate 'sig==9'
```

### Tracing `malloc` calls

```bash
ltrace -w 10 -l libc -e malloc -e free -p PID
```

## Text

### Slicing by timestamp

```bash
sed -n '/2015-04-22 17:21:46/,/2015-04-22 17:21:50/p'
```


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
    -filter_complex "[0:v] fps=12,scale=w=640:h=-1,split [a][b];[a] palettegen=reserve_transparent=on:max_colors=32 [p]; [b][p] paletteuse" \
    -loop 0 animated.gif
```

### Making an animated WebP

```bash
ffmpeg -framerate 12 -i frame%04d.png -s 85x85 -loop 0 animated.webp
```

### Making an M4V

```bash
ffmpeg -framerate 12 -i frame%04d.png -s 480x258 -crf 18 -pix_fmt yuv420p animated.m4v
```


# Linux

## Add URI scheme handler

```bash
# Assuming SCHEME.desktop contains `MimeType=x-scheme-handler/SCHEME`
xdg-mime default SCHEME.desktop x-scheme-handler/SCHEME
```

## Adding new device ID to Linux USB driver

```bash
echo '8086 10f5' > /sys/bus/usb/drivers/NAME/new_id
```

## SATA Secure Erase

```bash
hdparm -I  # Check disk is not frozen
hdparm --user-master u --security-set-pass Eins /dev/sdX
hdparm --user-master u --security-erase Eins /dev/sdX
```

