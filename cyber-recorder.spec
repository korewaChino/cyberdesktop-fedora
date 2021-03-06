%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name:		cyber-recorder
Version:	1.0.0
Release:	99%{?dist}
Summary:	Cyber Recorder
License:	GPLv3+
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:	qt5-qtbase-devel qt5-qttools qt5-qttools-devel qt5-qtdeclarative-devel qt5-qtmultimedia-devel qt5-qtquickcontrols2-devel qt5-linguist
Requires: meuikit
Source0:	https://git.omame.tech/CyberOS/cyber-recorder/archive/%{version}.tar.gz
%description
The recorder application for Cyber Desktop

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
%{_bindir}/cyber-recorder
%{_datadir}/applications/cyber-recorder.desktop
%{_datadir}/cyber-recorder

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.0.0
- Initial version
