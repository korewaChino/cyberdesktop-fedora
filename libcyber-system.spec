%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name:		libcyber-system
Version:	1.0.0
Release:	1%{?dist}
Summary:	CyberOS Libraries
License:	GPLv3+
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:	git qt5-qtquickcontrols2-devel kf5-networkmanager-qt-devel kf5-modemmanager-qt-devel libkscreen-qt5-devel kf5-kio-devel qt5-qtsensors-devel
Requires:	qt5-qtbase
Requires:	kf5-networkmanager-qt
Requires:	kf5-modemmanager-qt
Requires:	kscreen
Source0:	https://git.omame.tech/CyberOS/libcyber-system/archive/1.0.0.tar.gz

%description
Libraries for CyberOS applications

%prep
%setup -qn %{name}

%build
%{set_build_flags}
cmake -B .
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%{_libdir}/qt5/qml/Cyber/

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.0.0
- Initial version
