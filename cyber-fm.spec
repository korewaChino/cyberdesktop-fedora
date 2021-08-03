Name:		cyber-fm
Version:	1.0.0
Release:	%{?dist}
Summary:	Cyber File Manager
License:	GPL-3.0-or-later
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:	git
BuildRequires:	qt5-qttools qt5-qtbase-private-devel
Requires:	qt5-qtbase
Requires:	qt5-qtquickcontrols2
Requires:	qt5-qtx11extras
Requires:	taglib
%undefine _disable_source_fetch
Source0:	https://git.omame.tech/CyberOS/cyber-fm/archive/1.0.0.tar.gz
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
/usr/bin/cyber-fm
/usr/share/cyber-fm/
/usr/share/applications/cyber-fm.desktop

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.0.0
- Initial version
