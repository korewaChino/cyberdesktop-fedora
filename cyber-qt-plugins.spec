Name:		cyber-qt-plugins
Version:	1.0.0
Release:	99%{?dist}
Summary:	Qt Plugins necessary for Cyber Desktop to work
License:	GPLv3+
URL:		https://getcyberos.org
BuildRequires:	cmake pkgconfig
BuildRequires:	extra-cmake-modules 
BuildRequires:	libqtxdg-devel libxcb-devel xcb-util-wm-devel
BuildRequires:	cmake(Qt5Core) cmake(Qt5Widgets) cmake(Qt5DBus) cmake(Qt5X11Extras) cmake(Qt5Gui) cmake(dbusmenu-qt5) cmake(Qt5ThemeSupport)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	qt5-qtbase-static qt5-qtbase-private-devel

Source0:	https://git.omame.tech/CyberOS/cyber-qt-plugins/archive/%{version}.tar.gz 
%description
This package contains the Qt plugins necessary to make Cyber Desktop work

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
%{_libdir}/qt5/plugins/platformthemes/libcyberplatformtheme.so
%{_libdir}/qt5/plugins/styles/libcyberstyle.so

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.0.0
- Initial version
