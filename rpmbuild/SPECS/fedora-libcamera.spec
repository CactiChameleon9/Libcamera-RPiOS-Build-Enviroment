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
/usr

%changelog
* Fri Jun 17 2022 root
- 

