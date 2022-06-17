Name:		libcamera
Version:	0.0.0
Release:	0%{?dist}
Summary:	A library to support complex camera ISPs
# Library is LGPLv2.1+ and the cam tool is GPLv2
License:	LGPLv2+ and GPLv2
URL:		https://libcamera.org/
Source0:	libcamera-fedora.tar.xz


%description

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
cp -a usr/ $RPM_BUILD_ROOT/

%files
/usr/share/doc/libcamera-0.0.0/
/usr/include/libcamera/
/usr/lib64/libcamera/
/usr/lib64/pkgconfig/libcamera-base.pc
/usr/lib64/pkgconfig/libcamera.pc
/usr/libexec/libcamera/
/usr/share/libcamera/
/usr/bin/cam
/usr/bin/lc-compliance
/usr/bin/qcam
/usr/lib64/gstreamer-1.0/libgstlibcamera.so
/usr/lib64/libcamera-base.so
/usr/lib64/libcamera-base.so.0
/usr/lib64/libcamera-base.so.0.0.0
/usr/lib64/libcamera.so
/usr/lib64/libcamera.so.0
/usr/lib64/libcamera.so.0.0.0


%changelog
* Fri Jun 17 2022 root
- 

