%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name:		cyber-fm
Version:	1.0.0
Release:	99%{?dist}
Summary:	Cyber File Manager
License:	GPLv3+
URL:		https://getcyberos.org
BuildRequires:	cmake extra-cmake-modules
BuildRequires:	qt5-qtbase-devel qt5-qtx11extras-devel qt5-qttools-devel qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel qt5-linguist qt5-qtx11extras-devel qt5-qtbase-private-devel gcc-c++
BuildRequires:	kf5-kio-devel
BuildRequires:	meuikit-devel
Requires:	taglib
Requires: meuikit
Source0:	https://git.omame.tech/CyberOS/cyber-fm/archive/%{version}.tar.gz
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
