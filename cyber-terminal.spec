Name:		cyber-terminal
Version:	1.0.0
Release:	%{?dist}
Summary:	Cyber Terminal
License:	GPL-3.0-or-later
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:	extra-cmake-modules
BuildRequires:	git
BuildRequires:	qt5-qttools
Requires:	qt5-qtbase
Requires:	qt5-qtquickcontrols2
Requires:	qt5-qtgraphicaleffects
Requires:	meuikit
%undefine _disable_source_fetch
Source0:	https://git.omame.tech/CyberOS/cyber-terminal/archive/1.0.0.tar.gz
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
/usr/bin/cyber-terminal
/usr/lib64/qt5/qml/Cyber/TermWidget/
/usr/share/applications/cyber-terminal.desktop
/usr/share/cyber-terminal/

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.0.0
- Initial version
