Name: i3status
Version: 2.9
Release: 1%{?dist}
Summary: Generates status bar to use with i3bar, dzen2 or xmobar
License: BSD
URL: http://i3wm.org
Source: https://github.com/i3/%{name}/archive/%{version}.tar.gz

BuildRequires: asciidoc
BuildRequires: alsa-lib-devel
BuildRequires: epel-release
BuildRequires: libconfuse-devel
BuildRequires: wireless-tools-devel
BuildRequires: yajl2-devel

Requires: epel-release

%description
i3status is a small program (about 1500 SLOC) for generating a status bar for
i3bar, dzen2, xmobar or similar programs. It is designed to be very efficient
by issuing a very small number of system calls, as one generally wants to
update such a status line every second. This ensures that even under high
load, your status bar is updated correctly. Also, it saves a bit of energy by
not hogging your CPU as much as spawning the corresponding amount of shell
commands would.

%prep
%setup -q -n %{name}-%{version}
sed -i 's/LIBS+=-lyajl/LIBS+=-lyajl_s/' Makefile

%build
make

%install
%make_install

%files
%{_bindir}/%{name}*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/man*/%{name}*

%changelog
* Sun Dec 24 2015 Matt Gollob <mattness@no-reply.github.com> - 2.9-1
- First build
