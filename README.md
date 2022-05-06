# Build your cross compile docker image:

/usr/bin/docker build -t libcamera/debian/bullseye-cross-arm64 Dockerfile.debian.bullseye.cross-arm64

# Run a shell in the new docker image in the local libcamera directory
docker run \
	-v "$PWD":"$PWD" \
	-v "$HOME":"$HOME" \
	-w "$PWD" --rm -it libcamera/debian/bullseye-cross-arm64

# Configure meson to perform the cross build
meson build/rpi/bullseye --cross-file aarch64-linux-gnu.mesoncross

# (Cross-compile) Build libcamera at host compile speeds
ninja -C ./build/rpi/bullseye/


# Install built components on RPi

TODO: This could be a step to build a debian package (would be nice) or tar/scp built objects to the target...
