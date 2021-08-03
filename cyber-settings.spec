%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name:		cyber-settings
Version:	1.1.0
Release:	1%{?dist}
Summary:	Cyber Desktop Settings
License:	GPL-3.0-or-later
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:	extra-cmake-modules
BuildRequires:	git
BuildRequires:	qt5-qttools
Requires:	qt5-qtbase
Requires:	qt5-quickcontrols2
Requires:	meuikit
Requires:	freetype2
Requires:	fontconfig
Requires:	networkmanager-qt
Requires:	modemmanager-qt
Requires:	kcoreaddons
Requires:	libcyber-system
Source0:	https://git.omame.tech/CyberOS/cyber-settings/archive/1.1.0.tar.gz
%description
The settings for Cyber Desktop

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
%{_bindir}/cyber-settings
%{_datadir}/applications/cyber-settings.desktop
%{_datadir}/cyber-settings/


%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.1.0
- Initial version
