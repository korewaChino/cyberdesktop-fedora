%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name:		cyber-dock
Version:	1.0.0
Release:	99%{?dist}
Summary:	The Cyber Desktop Dock
License:	GPLv3+
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:	dbusmenu-qt5-devel
BuildRequires:	qt5-qtbase-devel qt5-qttools qt5-qttools-devel qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel qt5-linguist qt5-qtx11extras-devel
BuildRequires:	kf5-kwindowsystem-devel kf5-kwayland-devel
BuildRequires:	meuikit-devel
Requires:	qt5-qtbase qt5-qtquickcontrols2
Requires:	kf5-kwindowsystem kf5-kwayland
Source0:	https://git.omame.tech/CyberOS/cyber-dock/archive/%{version}.tar.gz
%description
The dock for Cyber Desktop

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
%{_datadir}/cyber-dock/
%{_bindir}/cyber-dock


%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.0.0
- Initial version
