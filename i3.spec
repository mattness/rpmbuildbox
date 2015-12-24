Name: i3
Version: 4.8
Release: 1%{?dist}
Summary: Improved tiling window manager
License: BSD
URL: http://i3wm.org
Source: http://i3wm.org/downloads/%{name}-%{version}.tar.bz2
Patch1: i3-disable-pango.patch

BuildRequires: epel-release
BuildRequires: libev-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: pcre-devel
BuildRequires: startup-notification-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: yajl2-devel

Requires: epel-release

# Recommends: dmenu
# Recommends: i3-status
# Recommends: rxvt-unicode-256color

%description
Key features of i3 are correct implementation of XrandR, horizontal and vertical
columns (think of a table) in tiling. Also, special focus is on writing clean,
readable and well documented code. i3 uses xcb for asynchronous communication
with X11, and has several measures to be very fast.

Please be aware that i3 is primarily targeted at advanced users and developers.

%prep
%setup -q
%patch1 -p1

%build
make YAJL_LIBS='-lyajl_s' \
  XCURSOR_LIBS='-Wl,-Bstatic -lxcb-cursor -Wl,-Bdynamic -lxcb-render-util -lxcb-image -lxcb-render -lxcb-shm -lxcb -lXau' V=1
make -C man V=1

%install
%make_install
mkdir -p %{buildroot}%{_mandir}/man1/
install -Dpm0644 man/*.1 %{buildroot}%{_mandir}/man1/

%files
%{_bindir}/%{name}*
%{_includedir}/%{name}/
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/%{name}/config.keycodes
%{_datadir}/xsessions/%{name}.desktop
%{_datadir}/xsessions/%{name}-with-shmlog.desktop
%{_mandir}/man*/%{name}*
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Dec 24 2015 Matt Gollob <mattness@no-reply.github.com> - 4.8-1
- First build
