Name:		cyber-kwin-plugins
Version:	1.0.0
Release:	%{?dist}
Summary:	KWin Plugins for Cyber Desktop
License:	GPL-3.0-or-later
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:  extra-cmake-modules qt5-qtbase qt5-qtdeclarative kf5-kwindowsystem-devel kdecoration-devel
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
%undefine _disable_source_fetch
Source0:	https://git.omame.tech/CyberOS/cyber-kwin-plugins/archive/1.0.0.tar.gz
%description
%define debug_package %{nil}
%define _build_id_links none
%prep
%setup -qn %{name}




%build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install




%files 
%license LICENSE
/etc/xdg/kwinrc
/usr/lib64/qt5/plugins/org.kde.kdecoration2/libcyberdecoration.so
/usr/share/kwin/effects/cyber_squash/
/usr/share/kwin/scripts/cyberlauncher/
/usr/share/kwin/tabbox/cyber_thumbnail/

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.0.0
- Initial version
