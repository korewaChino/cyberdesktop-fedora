%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name:		cyber-terminal
Version:	1.0.0
Release:	99%{?dist}
Summary:	Cyber Terminal
License:	GPLv3+
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:	extra-cmake-modules
BuildRequires:	qt5-qtbase-devel qt5-qttools-devel qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel qt5-linguist
BuildRequires:	meuikit-devel
Requires: meuikit
Source0:	https://git.omame.tech/CyberOS/cyber-terminal/archive/%{version}.tar.gz
%description
The terminal for Cyber Desktop

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
%{_bindir}/cyber-terminal
%{_libdir}/qt5/qml/Cyber/TermWidget/
%{_datadir}/applications/cyber-terminal.desktop
%{_datadir}/cyber-terminal/

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.0.0
- Initial version
