Name: xcb-util-cursor
Version: 0.1.0
Release: 1%{?dist}
Summary: XCB cursor library (libxcursor port)
License: MIT
URL: http://xcb.freedesktop.org/
Source: http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.gz

BuildRequires: m4
BuildRequires: libxcb-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-image-devel

%description
The XCB util modules provides a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package devel
Summary: XCB cursor library (libxcursor port) - development headers
Requires: %{name}%{?_isa} == %{version}-%{release}

%description devel
Development headers for the xcb-util-cursor library.

%prep
%setup

%build
%configure
make

%install
%make_install

%files
%{_libdir}/libxcb-cursor.a
%{_libdir}/libxcb-cursor.la
%{_libdir}/libxcb-cursor.so
%{_libdir}/libxcb-cursor.so.0
%{_libdir}/libxcb-cursor.so.0.0.0

%files devel
%{_includedir}/xcb/xcb_cursor.h
%{_libdir}/pkgconfig/xcb-cursor.pc

%changelog
* Wed Dec 23 2015 Matt Gollob <mattgollob@gmail.com> 0.1.0
- First build.