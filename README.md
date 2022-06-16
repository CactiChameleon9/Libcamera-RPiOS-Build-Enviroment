# Cross compilation environment for libcamera for the RPi Bullseye OS

This will let you build a cross compilation docker image, and use it to compile libcamera for the RPi.
These commands are expected to be run in a working directory containing the checked out libcamera source and a mountpoint for the raspberry pi rootfs (using `sshfs` for example). You will also need to save Dockerfile file locally. A meson cross file will be automatically generated inside the debian bullseye environment.

### Build your cross compile docker image: (TODO: make a prebuilt image to pull)

`/usr/bin/docker build -t libcamera/debian/bullseye-cross-arm64 - < Dockerfile.debian.bullseye.cross-arm64`

### Run a shell in the new docker image in your working directory (containing libcamera and your mountpoint)
`docker run -v "$PWD":"$PWD" -w "$PWD" --rm -it libcamera/debian/bullseye-cross-arm64`

### Enter your libcamera sources directory
`cd libcamera`

### Configure meson to perform the cross build
`meson build/rpi/bullseye --cross-file /usr/share/meson/arm64-cross`

### (Cross-compile) Build libcamera at host compile speeds
`ninja -C ./build/rpi/bullseye/`

### Install built components on RPi
`RPI_MOUNT_POINT=$(readlink -f ../mountpoint)` 
`DESTDIR=$RPI_MOUNT_POINT ninja -C ./build/rpi/bullseye install`