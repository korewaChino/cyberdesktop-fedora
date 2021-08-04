%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name:		cyber-edit
Version:	1.0.0
Release:	99%{?dist}
Summary:	Cyber Text Editor
License:	GPLv3+
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:	meuikit-devel qt5-qttools qt5-qttools-devel qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel qt5-linguist qt5-qtx11extras-devel
Source0:	https://git.omame.tech/CyberOS/cyber-edit/archive/%{version}.tar.gz
%description
Text editor for Cyber Desktop

%prep
%setup -n %{name}

%build
%{set_build_flags}
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files 
%license LICENSE
/usr/bin/cyber-edit
/usr/share/applications/cyber-edit.desktop
/usr/share/cyber-edit/translations/

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.0.0
- Initial version
