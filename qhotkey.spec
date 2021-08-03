Name:		qhotkey
Version:	1.4.2
Release:	%{?dist}
Summary:	A global shortcut/hotkey for Desktop Qt-Applications 
License:	GPL-3.0-or-later
URL:		https://skycoder42.github.io/QHotkey/
BuildRequires:	git qt-devel
Requires:	qt5-qtbase
%define debug_package %{nil}
Source0:	https://github.com/Skycoder42/QHotkey/archive/refs/tags/1.4.2.tar.gz
%description
%define debug_package %{nil}
%define _build_id_links none
%prep
%setup -qn QHotkey-%{version}

%build
#cd "$pkgname-src";
#mkdir -p build;
#cd build;
qmake-qt5 
make

%install
#cd "$pkgname-src/build";
rm -rf $RPM_BUILD_ROOT
sudo make install

%files
# TODO: Add files

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - r111.eb7ddab
- Initial version
