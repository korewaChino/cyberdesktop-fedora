%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name:		cyber-launcher
Version:	1.0.0
Release:	1%{?dist}
Summary:	Cyber Desktop Launcher
License:	GPLv3+
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:	git
BuildRequires:	qt5-qttools qt5-qttools-devel qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel qt5-linguist
Requires:	qt5-base
Requires:	qt5-quickcontrols2
Requires:	meuikit
Source0:	https://git.omame.tech/CyberOS/cyber-launcher/archive/1.0.0.tar.gz
BuildRoot: %{_tmppath}/%{name}
%description
The launcher for Cyber Desktop

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
%license LICENSE
%{_bindir}/cyber-launcher
%{_datadir}/cyber-launcher/

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.0.0
- Initial version
