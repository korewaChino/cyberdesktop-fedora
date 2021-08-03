%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name:		qhotkey
Version:	1.4.2
Release:	%{?dist}
Summary:	A global shortcut/hotkey for Desktop Qt-Applications 
License:	GPLv3+
URL:		https://skycoder42.github.io/QHotkey/
BuildRequires:	git qt-devel
Requires:	qt5-qtbase
%define debug_package %{nil}
Source0:	https://github.com/Skycoder42/QHotkey/archive/refs/tags/1.4.2.tar.gz
%description
A global shortcut/hotkey for Desktop Qt-Applications

%prep
%setup -qn QHotkey-%{version}

%build
%{set_build_flags}
#cd "$pkgname-src";
#mkdir -p build;
#cd build;
qmake-qt5 
make %{?_smp_mflags}

%install
#cd "$pkgname-src/build";
rm -rf $RPM_BUILD_ROOT
make install

%files
# TODO: Add files

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - r111.eb7ddab
- Initial version
