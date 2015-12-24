#!/bin/bash

repo=/vagrant/yumrepo
srcdir=/tmp/sources
mockconfig=custom-6-x86_64

# Install necessary tools
sudo yum install -y epel-release
sudo yum install -y mock createrepo
sudo usermod -a -G mock $USER

# Create the yum repo that will hold our build RPMs
mkdir -p ${repo}
sudo createrepo ${repo}
cat <<EOH | sudo tee /etc/yum.repos.d/custom.repo &>/dev/null
[custom]
name=custom
baseurl=file://${repo}/
enabled=1
gpgcheck=0
EOH

# Configure mock
cat <<EOH | sudo tee /etc/mock/${mockconfig}.cfg &>/dev/null
config_opts['root'] = '${mockconfig}'
config_opts['target_arch'] = 'x86_64'
config_opts['legal_host_arches'] = ('x86_64',)
config_opts['chroot_setup_cmd'] = 'install @buildsys-build'
config_opts['dist'] = 'el6'  # only useful for --resultdir variable subst
# beware RHEL use 6Server or 6Client
config_opts['releasever'] = '6'

config_opts['yum.conf'] = """
[main]
keepcache=1
debuglevel=2
reposdir=/dev/null
logfile=/var/log/yum.log
retries=20
obsoletes=1
gpgcheck=0
assumeyes=1
syslog_ident=mock
syslog_device=

# repos
[base]
name=BaseOS
enabled=1
mirrorlist=http://mirrorlist.centos.org/?release=6&arch=x86_64&repo=os
failovermethod=priority
gpgkey=file:///etc/pki/mock/RPM-GPG-KEY-CentOS-6
gpgcheck=1

[updates]
name=updates
enabled=1
mirrorlist=http://mirrorlist.centos.org/?release=6&arch=x86_64&repo=updates
failovermethod=priority
gpgkey=file:///etc/pki/mock/RPM-GPG-KEY-CentOS-6
gpgcheck=1

[epel]
name=epel
mirrorlist=http://mirrors.fedoraproject.org/mirrorlist?repo=epel-6&arch=x86_64
failovermethod=priority
gpgkey=file:///etc/pki/mock/RPM-GPG-KEY-EPEL-6
gpgcheck=1

[custom]
name=custom
baseurl=file://${repo}/
enabled=1
gpgcheck=0
failovermethod=priority
"""
EOH

# Get the source code to be built
mkdir -p ${srcdir}
cp /vagrant/*.patch ${srcdir}

sources=('http://xcb.freedesktop.org/dist/xcb-util-cursor-0.1.0.tar.gz')
sources+=('https://github.com/lloyd/yajl/archive/2.0.4.tar.gz')
sources+=('http://i3wm.org/downloads/i3-4.8.tar.bz2')
sources+=('https://github.com/i3/i3status/archive/2.9.tar.gz')

for src in "${sources[@]}"; do
  cd ${srcdir}
  curl -sLO ${src}
done

# Build the RPMs
specs=('/vagrant/xcb-util-cursor.spec')
specs+=('/vagrant/yajl2.spec')
specs+=('/vagrant/i3.spec')
specs+=('/vagrant/i3status.spec')
resultpath=$(mock -r ${mockconfig} -p)../result

for spec in "${specs[@]}"; do
  mock -r ${mockconfig} --buildsrpm --spec=${spec} --sources=${srcdir} \
    && cp ${resultpath}/*.src.rpm ${repo} \
    && mock -r ${mockconfig} ${repo}/$(basename ${spec%.*})-*.src.rpm \
    && cp ${resultpath}/*.rpm ${repo}/ \
    && sudo createrepo --update ${repo}
done
