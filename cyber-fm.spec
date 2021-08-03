%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name:		cyber-fm
Version:	1.0.0
Release:	1%{?dist}
Summary:	Cyber File Manager
License:	GPLv3+
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:	git
BuildRequires:	qt5-qttools qt5-qtbase-private-devel
Requires:	qt5-qtbase
Requires:	qt5-qtquickcontrols2
Requires:	qt5-qtx11extras
Requires:	taglib
%undefine _disable_source_fetch
Source0:	https://git.omame.tech/CyberOS/cyber-fm/archive/1.0.0.tar.gz
%description
The file manager for Cyber Desktop

%prep
%setup -qn %{name}

%build
%{set_build_flags}
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files 
%license LICENSE
%{_bindir}/cyber-fm
%{_datadir}/cyber-fm/
%{_datadir}/applications/cyber-fm.desktop

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.0.0
- Initial version
