FROM fedora:36

ENV LANG='C.UTF-8' LC_ALL='C.UTF-8'

RUN dnf update -y

RUN dnf install -y sudo

RUN dnf install -y \
	gcc-aarch64-linux-gnu gcc-c++-aarch64-linux-gnu \
	meson ninja-build pkg-config \
	python3-yaml python3-ply python3-jinja2 \
	openssl \
	python3-sphinx doxygen ghostscript graphviz texlive-latex \
	lttng-ust-devel python3-jinja2 lttng-tools-devel
	

RUN dnf install -y \
	qt5-qtbase-devel qt5-qttools-devel\
	libjpeg-turbo-devel boost-devel libyaml-devel \
	libtiff-devel libexif-devel \
	gstreamer1-devel gstreamer1-plugins-base-devel \
	gnutls-devel libatomic

# Create a custom user to operate in the container
RUN adduser libcamera
RUN usermod -aG root libcamera
RUN echo '%root ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

WORKDIR /home/libcamera
USER libcamera
