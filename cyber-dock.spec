%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name:		cyber-dock
Version:	1.0.0
Release:	1%{?dist}
Summary:	The Cyber Desktop Dock
License:	GPLv3+
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:	git
BuildRequires:	qt5-qttools dbusmenu-qt5-devel kf5-kwindowsystem-devel
Requires:	kwayland
Requires:	qt5-qtbase
Requires:	qt5-qtquickcontrols2
Requires:	kf5-kwindowsystem
Requires:	meuikit
Requires:	libcyber-system
Source0:	https://git.omame.tech/CyberOS/cyber-dock/archive/1.0.0.tar.gz
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
