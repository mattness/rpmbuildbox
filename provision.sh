#!/bin/bash

sudo yum install -y rpm-build redhat-rpm-config rpmdevtools
sudo yum groupinstall -y 'Development Tools'
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros
