# Cross compilation environment for libcamera for the RPi Bullseye OS

This will let you build a cross compilation docker image, and use it to compile libcamera for the RPi, and the package it up in a deb file to send to your RPi. A meson cross file will be automatically generated inside the debian bullseye environment. 

## Setting up your working directory
#### Make the directory
`mkdir libcamera-raspi; cd libcamera-raspi`
#### Download this repo
`git clone https://github.com/CactiChameleon9/Libcamera-RPiOS-Build-Enviroment ./`
#### Clone the libcamera sources
`git clone https://git.libcamera.org/libcamera/libcamera.git`

## Building and installing

### Build your cross compile docker image: (TODO: make a prebuilt image to pull)
`sudo docker build -t libcamera/debian/bullseye-cross-arm64 - < Dockerfile.debian.bullseye.cross-arm64`

### Run a shell in the new docker image in your working directory (containing libcamera and your mountpoint)
`sudo docker run -v "$PWD":"$PWD" -w "$PWD" --rm -it libcamera/debian/bullseye-cross-arm64`

### Enter your libcamera sources directory
`cd libcamera`

### Configure meson to perform the cross build
`meson build/rpi/bullseye --cross-file /usr/share/meson/arm64-cross`

### (Cross-compile) Build libcamera at host compile speeds
`ninja -C ./build/rpi/bullseye/`

### Building the deb package
`sudo DESTDIR=$(readlink -f ../libcamera-raspi-debian) ninja -C ./build/rpi/bullseye install`

`cd ../`

`sudo dpkg -b libcamera-raspi-debian`

## Installing your built deb file
- You should find a libcamera-raspi-debian.deb file in your working directory, you need to transfer this to your raspberry pi and install it
- I personally would use sftp with a graphical file manager such as nautilus, but cloud storage, ftp, transfer.sh etc. could work too
- To install the deb file, simply run `sudo apt install ./libcamera-raspi-debian.deb` in the directory of your transfered deb file
