Name:		libcyber-system
Version:	1.0.0
Release:	%{?dist}
Summary:	CyberOS Libraries
License:	GPL-3.0-or-later
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:	git kf5-networkmanager-qt-devel kf5-modemmanager-qt-devel libkscreen-qt5-devel kf5-kio-devel qt5-qtsensors-devel qt5-qtquickcontrols2-devel
Requires:	qt5-qtbase
Requires:	kf5-networkmanager-qt
Requires:	kf5-modemmanager-qt
Requires:	kscreen
%undefine _disable_source_fetch
Source0:	https://git.omame.tech/CyberOS/libcyber-system/archive/1.0.0.tar.gz
%description
%global debug_package %{nil}
%define _build_id_links none
%prep
%setup -qn %{name}




%build
cmake -B .
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
/usr/lib64/qt5/qml/Cyber/

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.0.0
- Initial version
