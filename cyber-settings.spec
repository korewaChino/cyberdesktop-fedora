%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name:		cyber-settings
Version:	1.1.0
Release:	0a%{?dist}
Summary:	Cyber Desktop Settings
License:	GPL-3.0-or-later
URL:		https://getcyberos.org
BuildRequires:	cmake pkgconfig
BuildRequires:	extra-cmake-modules
BuildRequires:	git
BuildRequires:	qt5-qtbase-devel qt5-qttools-devel qt5-qttools-devel qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel qt5-linguist
BuildRequires:	kf5-kcoreaddons-devel kf5-networkmanager-qt-devel kf5-modemmanager-qt-devel
BuildRequires:	meuikit-devel
BuildRequires:	libicu-devel
BuildRequires:	freetype-devel
BuildRequires:	fontconfig-devel
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
