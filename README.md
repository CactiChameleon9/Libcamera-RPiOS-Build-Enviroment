# Build environment for libcamera for fedora

This is a simple way to build testing libcamera rpm's on non fedora distros. The generated rpm files should not be used for production.

## Setting up your working directory
#### Make the directory
`mkdir libcamera-fedora; cd libcamera-fedora`
#### Download this repo
`git clone https://github.com/CactiChameleon9/Libcamera-RPiOS-Build-Enviroment ./`
`git checkout fedora`
#### Clone the libcamera sources
`git clone https://git.libcamera.org/libcamera/libcamera.git`

## Building and installing

### Build your cross compile docker image: (TODO: make a prebuilt image to pull)
`sudo docker build -t libcamera/fedora/fedora - < Dockerfile`

### Run a shell in the new docker image in your working directory (containing libcamera and your mountpoint)
`sudo docker run -v "$PWD":"$PWD" -w "$PWD" --rm -it libcamera/fedora/fedora`

### Enter your libcamera sources directory
`cd libcamera`

### Configure meson to perform the cross build
`meson build`

### (Cross-compile) Build libcamera at host compile speeds
`ninja -C ./build`

## Build the rpm
```
mkdir ../libcamera-0.0.0
DESTDIR=$(readlink -f ../libcamera-0.0.0) ninja -C ./build install
cd ../
tar --create --file libcamera-fedora.tar.xz libcamera-0.0.0
mv libcamera-fedora.tar.xz rpmbuild/SOURCES/
rm -r libcamera-0.0.0
HOME=$(readlink -f ./) rpmbuild -bb rpmbuild/SPECS/fedora-libcamera.spec
```

You should now have a built rpm file at `rpmbuild/RPMS/x86_64/libcamera-0.0.0-0.fc36.x86_64.rpm`
