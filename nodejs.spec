Name: nodejs
Version: 0.12.7
Release: 1%{?dist}
Summary: JavaScript runtime
License: MIT and ASL 2.0 and ISC and BSD
Group: Development/Languages
URL: http://nodejs.org/

ExclusiveArch: x86_64

Source0: node-v%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++

#virtual provides for automatic depedency generation
Provides: nodejs(engine) = %{version}

#we need ABI virtual provides where SONAMEs aren't enough/not present so deps
#break when binary compatibility is broken
%global nodejs_abi 0.12
Provides: nodejs(abi) = %{nodejs_abi}

#this corresponds to the "engine" requirement in package.json
Provides: nodejs(engine) = %{version}


%description
Node.js is a platform built on Chrome's JavaScript runtime
for easily building fast, scalable network applications.
Node.js uses an event-driven, non-blocking I/O model that
makes it lightweight and efficient, perfect for data-intensive
real-time applications that run across distributed devices.

%package devel
Summary: JavaScript runtime - development headers
Group: Development/Languages
Requires: %{name}%{?_isa} == %{version}-%{release}

%description devel
Development headers for the Node.js JavaScript runtime.

%package docs
Summary: Node.js API documentation
Group: Documentation
BuildArch: noarch

%description docs
The API documentation for the Node.js JavaScript runtime.

%prep
%setup -q -n node-v%{version}

%build
./configure --prefix=%{_prefix} \
           --without-dtrace

# Setting BUILDTYPE=Debug builds both release and debug binaries
make BUILDTYPE=Debug %{?_smp_mflags}

%install
rm -rf %{buildroot}

./tools/install.py install %{buildroot} %{_prefix}

# and remove dtrace file again
rm -rf %{buildroot}/%{_prefix}/lib/dtrace

# Set the binary permissions properly
chmod 0755 %{buildroot}/%{_bindir}/node

# Install the debug binary and set its permissions
install -Dpm0755 out/Debug/node %{buildroot}/%{_bindir}/node_g

# own the sitelib directory
mkdir -p %{buildroot}%{_prefix}/lib/node_modules

# ensure Requires are added to every native module that match the Provides from
# the nodejs build in the buildroot
mkdir -p %{buildroot}%{_rpmconfigdir}
cat << EOF > %{buildroot}%{_rpmconfigdir}/nodejs_native.req
nodejs(abi) = %nodejs_abi
EOF

#install documentation
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}-docs-%{version}/html
cp -pr doc/* %{buildroot}%{_defaultdocdir}/%{name}-docs-%{version}/html
rm -f %{_defaultdocdir}/%{name}-docs-%{version}/html/nodejs.1
cp -p LICENSE %{buildroot}%{_defaultdocdir}/%{name}-docs-%{version}/

#node-gyp needs common.gypi too
mkdir -p %{buildroot}%{_datadir}/node
cp -p common.gypi %{buildroot}%{_datadir}/node

%files
%doc ChangeLog LICENSE README.md AUTHORS
%{_bindir}/node
%{_bindir}/npm
%{_mandir}/man1/node.*
%{_prefix}/lib/node_modules
%{_datadir}/node
%{_rpmconfigdir}/nodejs_native.req

%files devel
%{_bindir}/node_g
%{_includedir}/node
%{_datadir}/node/common.gypi
%{_datadir}/systemtap/tapset/node.stp

%files docs
%{_defaultdocdir}/%{name}-docs-%{version}

%changelog
* Sat Nov 21 2015 Matt Gollob <mattgollob@gmail.com> 0.12.7
- First build.
