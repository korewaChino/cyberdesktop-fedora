%define debug_package %{nil}
%define _disable_source_fetch 0
%define _build_id_links none

Name:           cyber-icon-theme
Version:        1.0.0
Release:        99%{?dist}
Summary:        Cyber icon Theme

License:        GPLv3+
URL:            https://getcyberos.org
Source0:        https://git.omame.tech/CyberOS/cyber-icon-theme/archive/1.0.0.tar.gz

BuildRequires:  cmake make
Provides:				crule-icon-theme = 0.0.%{version}-%{release}

%description
Icon theme made for the Cyber Desktop Environment

%prep
%autosetup -n %{name}

%build
cmake .
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%license LICENSE
%{_datadir}/icons/Crule
%{_datadir}/icons/Crule-dark

%changelog
* Wed Aug 04 2021 korewaChino <crkza1134@gmail.com>
- 
