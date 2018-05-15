Name:           tigeros-repos
Version:        28.1
Release:        1%{?dist}
Summary:        TigerOS package repository

Group:          System Environment/Base
License:        MIT
URL:            https://github.com/RITlug/tigeros-repos
Source:         %{name}-%{version}-%{release}.tar.gz
BuildArch:      noarch

%global vers 28

%description
TigerOS package repository files for yum
and dnf along with gpg public keys

%prep
%setup -q

%install
# Install the keys
install -d -m 755 %{buildroot}/etc/pki/rpm-gpg
install -m 644 RPM-GPG-KEY-TigerOS-%{vers} %{buildroot}/etc/pki/rpm-gpg/

# and add symlink for compat generic location
ln -s RPM-GPG-KEY-TigerOS-%{vers} RPM-GPG-KEY-%{version}-TigerOS

install -d -m 755 %{buildroot}/etc/yum.repos.d
install -m 644 tigeros.repo %{buildroot}/etc/yum.repos.d/

%files
%defattr(-,root,root,-)
/etc/yum.repos.d/tigeros.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-TigerOS-%{vers}

%changelog
* Tue May 15 2018 Christian Martin <tigeros@ritlug.com> - 28.1
- Updated to F28

* Wed Apr 04 2018 Tim Zabel <tjz8659@rit.edu> - 1.0-1
- Updated spec file
