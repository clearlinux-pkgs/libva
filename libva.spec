#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : libva
Version  : 2.18.0
Release  : 66
URL      : https://github.com/intel/libva/archive/2.18.0/libva-2.18.0.tar.gz
Source0  : https://github.com/intel/libva/archive/2.18.0/libva-2.18.0.tar.gz
Summary  : Userspace Video Acceleration (VA) core interface
Group    : Development/Tools
License  : MIT
Requires: libva-lib = %{version}-%{release}
Requires: libva-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : doxygen
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(32libdrm)
BuildRequires : pkgconfig(32wayland-client)
BuildRequires : pkgconfig(32wayland-scanner)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32x11-xcb)
BuildRequires : pkgconfig(32xcb)
BuildRequires : pkgconfig(32xcb-dri3)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(32xfixes)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-scanner)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcb-dri3)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xfixes)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Libva Project
Libva is an implementation for VA-API (Video Acceleration API)
VA-API is an open-source library and API specification, which provides access to graphics hardware acceleration capabilities for video processing. It consists of a main library and driver-specific acceleration backends for each supported hardware vendor.

%package dev
Summary: dev components for the libva package.
Group: Development
Requires: libva-lib = %{version}-%{release}
Provides: libva-devel = %{version}-%{release}
Requires: libva = %{version}-%{release}

%description dev
dev components for the libva package.


%package dev32
Summary: dev32 components for the libva package.
Group: Default
Requires: libva-lib32 = %{version}-%{release}
Requires: libva-dev = %{version}-%{release}

%description dev32
dev32 components for the libva package.


%package lib
Summary: lib components for the libva package.
Group: Libraries
Requires: libva-license = %{version}-%{release}

%description lib
lib components for the libva package.


%package lib32
Summary: lib32 components for the libva package.
Group: Default
Requires: libva-license = %{version}-%{release}

%description lib32
lib32 components for the libva package.


%package license
Summary: license components for the libva package.
Group: Default

%description license
license components for the libva package.


%prep
%setup -q -n libva-2.18.0
cd %{_builddir}/libva-2.18.0
pushd ..
cp -a libva-2.18.0 build32
popd
pushd ..
cp -a libva-2.18.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685635419
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dwith_legacy=nvctrl  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dwith_legacy=nvctrl  builddiravx2
ninja -v -C builddiravx2
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
meson --libdir=lib32 --prefix=/usr --buildtype=plain -Dwith_legacy=nvctrl  builddir
ninja -v -C builddir
popd

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libva
cp %{_builddir}/libva-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libva/099b1aff1b937aad419a0cc7cfb474d2d74acf0b || :
pushd ../build32/
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/va/va.h
/usr/include/va/va_backend.h
/usr/include/va/va_backend_prot.h
/usr/include/va/va_backend_vpp.h
/usr/include/va/va_backend_wayland.h
/usr/include/va/va_compat.h
/usr/include/va/va_dec_av1.h
/usr/include/va/va_dec_hevc.h
/usr/include/va/va_dec_jpeg.h
/usr/include/va/va_dec_vp8.h
/usr/include/va/va_dec_vp9.h
/usr/include/va/va_dri2.h
/usr/include/va/va_dricommon.h
/usr/include/va/va_drm.h
/usr/include/va/va_drmcommon.h
/usr/include/va/va_egl.h
/usr/include/va/va_enc_av1.h
/usr/include/va/va_enc_h264.h
/usr/include/va/va_enc_hevc.h
/usr/include/va/va_enc_jpeg.h
/usr/include/va/va_enc_mpeg2.h
/usr/include/va/va_enc_vp8.h
/usr/include/va/va_enc_vp9.h
/usr/include/va/va_fei.h
/usr/include/va/va_fei_h264.h
/usr/include/va/va_fei_hevc.h
/usr/include/va/va_prot.h
/usr/include/va/va_str.h
/usr/include/va/va_tpi.h
/usr/include/va/va_version.h
/usr/include/va/va_vpp.h
/usr/include/va/va_wayland.h
/usr/include/va/va_x11.h
/usr/lib64/libva-drm.so
/usr/lib64/libva-wayland.so
/usr/lib64/libva-x11.so
/usr/lib64/libva.so
/usr/lib64/pkgconfig/libva-drm.pc
/usr/lib64/pkgconfig/libva-wayland.pc
/usr/lib64/pkgconfig/libva-x11.pc
/usr/lib64/pkgconfig/libva.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libva-drm.so
/usr/lib32/libva-wayland.so
/usr/lib32/libva-x11.so
/usr/lib32/libva.so
/usr/lib32/pkgconfig/32libva-drm.pc
/usr/lib32/pkgconfig/32libva-wayland.pc
/usr/lib32/pkgconfig/32libva-x11.pc
/usr/lib32/pkgconfig/32libva.pc
/usr/lib32/pkgconfig/libva-drm.pc
/usr/lib32/pkgconfig/libva-wayland.pc
/usr/lib32/pkgconfig/libva-x11.pc
/usr/lib32/pkgconfig/libva.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libva-drm.so.2.1800.0
/V3/usr/lib64/libva-wayland.so.2.1800.0
/V3/usr/lib64/libva-x11.so.2.1800.0
/V3/usr/lib64/libva.so.2.1800.0
/usr/lib64/libva-drm.so.2
/usr/lib64/libva-drm.so.2.1800.0
/usr/lib64/libva-wayland.so.2
/usr/lib64/libva-wayland.so.2.1800.0
/usr/lib64/libva-x11.so.2
/usr/lib64/libva-x11.so.2.1800.0
/usr/lib64/libva.so.2
/usr/lib64/libva.so.2.1800.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libva-drm.so.2
/usr/lib32/libva-drm.so.2.1800.0
/usr/lib32/libva-wayland.so.2
/usr/lib32/libva-wayland.so.2.1800.0
/usr/lib32/libva-x11.so.2
/usr/lib32/libva-x11.so.2.1800.0
/usr/lib32/libva.so.2
/usr/lib32/libva.so.2.1800.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libva/099b1aff1b937aad419a0cc7cfb474d2d74acf0b
