# Cross compilation environment for libcamera for the RPi Bullseye OS

This will let you build a cross compilation docker image, and use it to compile libcamera for the RPi.
These commands are expected to be run in a working directory containing the checked out libcamera source and a mountpoint for the raspberry pi rootfs (using `sshfs` for example). You will also need to save Dockerfile file locally. A meson cross file will be automatically generated inside the debian bullseye environment.

## Setting up your working directory
Key information: I needed sshfs to be mounted as root for `ninja install` to work
#### Make the directory
`mkdir libcamera-raspi; cd libcamera-raspi`
#### Download the dockerfile
`git clone https://gist.github.com/CactiChameleon9/1ce1bcf828e9937beb9c60fd1ebc0118 ./`
#### Clone the sources
`git clone https://git.libcamera.org/libcamera/libcamera.git`
#### Make your mountpoint as a root user
`sudo mkdir mountpoint`
#### Install sshfs using your package manager
`sudo apt-get install sshfs -y`
#### Mount the pi's filesystem using as root sshfs. Use your pi's ip address and user account name here.
`sudo sshfs pi@192.168.1.10:/ ./mountpoint`

## Building and installing

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
`DESTDIR=$(readlink -f ../mountpoint)`
`ninja -C ./build/rpi/bullseye install`