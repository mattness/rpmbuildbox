Name: i3
Version: 4.8
Release: 1%{?dist}
Summary: Improved tiling window manager
License: BSD
URL: http://i3wm.org
Source0: http://i3wm.org/downloads/%{name}-%{version}.tar.bz2
Source1: http://pkgconfig.freedesktop.org/releases/pkg-config-0.25.tar.gz

BuildRequires: asciidoc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bison
BuildRequires: cmake
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gperf
BuildRequires: libXau-devel
BuildRequires: libffi-devel
BuildRequires: libpng-devel
BuildRequires: libtool
BuildRequires: libxcb-devel
BuildRequires: make
BuildRequires: patch
BuildRequires: pcre-devel
BuildRequires: pixman-devel
BuildRequires: ruby
BuildRequires: startup-notification-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-image-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: zlib-devel

# Recommends: dmenu
# Recommends: epel-release
# Recommends: i3-status
# Recommends: rxvt-unicode-256color

%description
Key features of i3 are correct implementation of XrandR, horizontal and vertical
columns (think of a table) in tiling. Also, special focus is on writing clean,
readable and well documented code. i3 uses xcb for asynchronous communication
with X11, and has several measures to be very fast.

Please be aware that i3 is primarily targeted at advanced users and developers.

# %package        doc
# Summary:        Documentation for %{name}
# BuildRequires:  doxygen
# BuildArch:      noarch
# Requires:       %{name} = %{version}-%{release}

# %description    doc
# Asciidoc and doxygen generated documentations for %{name}.

%prep
cd %_builddir
rm -rf i3wm
mkdir -p i3wm
cd i3wm
gzip -dc %_sourcedir/pkg-config-0.25.tar.gz | tar -xvvf -

%build
cd %_builddir/i3wm/pkg-config-0.25
./configure --prefix=/opt/i3
make V=1

%install
cd %_builddir/i3wm
# %make_install

# %files
# %{_bindir}/%{name}*
# %{_includedir}/%{name}/
# %dir %{_sysconfdir}/%{name}/
# %config(noreplace) %{_sysconfdir}/%{name}/config
# %config(noreplace) %{_sysconfdir}/%{name}/config.keycodes
# %{_datadir}/xsessions/%{name}.desktop
# %{_datadir}/xsessions/%{name}-with-shmlog.desktop
# %{_datadir}/applications/%{name}.desktop

%changelog
* Sat Dec 19 2015 Matt Gollob <mattness@no-reply.github.com> - 4.8.1-1
- First build
