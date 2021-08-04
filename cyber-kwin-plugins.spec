%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name:		cyber-kwin-plugins
Version:	1.0.0
Release:	1%{?dist}
Summary:	KWin Plugins for Cyber Desktop
License:	GPLv3+
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:  extra-cmake-modules qt5-qtbase qt5-qtdeclarative kf5-kwindowsystem-devel kdecoration-devel qt5-linguist
Requires:	kwayland
Requires:	qt5-qtbase
Requires:	qt5-qtdeclarative
Requires:	kf5-kwindowsystem
Requires:	kf5-kwayland kwayland-integration
Requires:	kwin
Requires:	kconfigwidgets
Requires:	kf5-kcoreaddons
Requires:	kf5-kguiaddons
Requires:	kdecoration
Requires:	kf5-kconfig
Source0:	https://git.omame.tech/CyberOS/cyber-kwin-plugins/archive/1.0.0.tar.gz
%description
KWin Plugins for the Cyber Desktop

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
/etc/xdg/kwinrc
%{_libdir}/qt5/plugins/org.kde.kdecoration2/libcyberdecoration.so
%{_datadir}/kwin/effects/cyber_squash/
%{_datadir}/kwin/scripts/cyberlauncher/
%{_datadir}/kwin/tabbox/cyber_thumbnail/

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.0.0
- Initial version
