Name:		cyber-qt-plugins
Version:	1.0.0
Release:	%{?dist}
Summary:	Qt Plugins necessary for Cyber Desktop to work
License:	GPL-3.0-or-later
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:	extra-cmake-modules libqtxdg-devel qt5-qtbase-devel libxcb-devel xcb-util-wm-devel qt5-qtbase-private-devel
BuildRequires:	git
BuildRequires:	qt5-qttools
Requires:	qt5-qtbase
Requires:	qt5-qtx11extras
Requires:	libqtxdg
Requires:	libdbusmenu-qt5
Requires:	libxcb
%undefine _disable_source_fetch
Source0:	https://git.omame.tech/CyberOS/cyber-qt-plugins/archive/1.0.0.tar.gz 
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
/usr/lib64/qt5/plugins/platformthemes/libcyberplatformtheme.so
/usr/lib64/qt5/plugins/styles/libcyberstyle.so

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.0.0
- Initial version
