Name:		cyber-qt-plugins
Version:	1.0.0
Release:	1%{?dist}
Summary:	Qt Plugins necessary for Cyber Desktop to work
License:	GPLv3+
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:	extra-cmake-modules libqtxdg-devel qt5-qtbase-devel libxcb-devel xcb-util-wm-devel qt5-qtbase-private-devel
BuildRequires:	git
BuildRequires:	qt5-qttools qt5-qttools-devel qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel qt5-linguist
Requires:	qt5-qtbase
Requires:	qt5-qtx11extras
Requires:	libqtxdg
Requires:	libdbusmenu-qt5
Requires:	libxcb
Source0:	https://git.omame.tech/CyberOS/cyber-qt-plugins/archive/1.0.0.tar.gz 
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
