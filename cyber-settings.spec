%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name:		cyber-settings
Version:	1.1.0
Release:	100%{?dist}
Summary:	Cyber Desktop Settings
License:	GPLv3+
URL:		https://getcyberos.org
BuildRequires:	cmake pkgconfig
BuildRequires:	extra-cmake-modules
BuildRequires:	qt5-qtbase-devel qt5-qttools-devel qt5-qttools-devel qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel qt5-linguist
BuildRequires:	kf5-kcoreaddons-devel kf5-networkmanager-qt-devel kf5-modemmanager-qt-devel
BuildRequires:	meuikit-devel
BuildRequires:	libicu-devel
BuildRequires:	freetype-devel
BuildRequires:	fontconfig-devel
Requires: meuikit
Requires:	libcyber-system
Source0:	https://git.omame.tech/CyberOS/%{name}/archive/%{version}.tar.gz
%define patch0_refspec 6a3850cc3c7b301ab2a5db631ad757d01ffd0a72
Patch0: https://github.com/korewaChino/cyberdesktop-fedora/raw/%{patch0_refspec}/patches/%{name}/0000-about-external_resource_logo.patch
%description
The settings for Cyber Desktop

%prep
%setup -qn %{name}
patch -p1 -i %{PATCH0}

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
