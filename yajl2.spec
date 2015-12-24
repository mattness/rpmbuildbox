Name: yajl2
Version: 2.0.4
Release: 1%{?dist}
Summary: A fast streaming JSON parsing library in C.
License: ISC
URL: http://lloyd.github.io/yajl/
Source: https://github.com/lloyd/yajl/archive/%{version}.tar.gz

BuildRequires: cmake
BuildRequires: ruby
# This package conflicts with the yajl package provided by base
Conflicts: yajl

%description
Yet Another JSON Library. YAJL is a small event-driven (SAX-style) JSON
parser written in ANSI C, and a small validating JSON generator. YAJL is
released under the ISC license.

%package devel
Summary: A fast streaming JSON parsing library in C - development headers
Group: Development/Languages
Requires: %{name}%{?_isa} == %{version}-%{release}

%description devel
Development headers for the yajl 2.x library.

%prep
%setup -q -n yajl-%{version}

%build
./configure --prefix=%{_prefix}
make

%install
%make_install

%files
%{_bindir}/json_reformat
%{_bindir}/json_verify
%{_exec_prefix}/lib/libyajl.so
%{_exec_prefix}/lib/libyajl.so.2
%{_exec_prefix}/lib/libyajl.so.2.0.4
%{_exec_prefix}/lib/libyajl_s.a

%files devel
%{_includedir}/yajl/yajl_common.h
%{_includedir}/yajl/yajl_gen.h
%{_includedir}/yajl/yajl_parse.h
%{_includedir}/yajl/yajl_tree.h
%{_includedir}/yajl/yajl_version.h
%{_datadir}/pkgconfig/yajl.pc

%changelog
* Wed Dec 23 2015 Matt Gollob <mattgollob@gmail.com> 2.0.4
- First build.