Name:		cyber-dock
Version:	1.0.0
Release:	%{?dist}
Summary:	The Cyber Desktop Dock
License:	GPL-3.0-or-later
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
%undefine _disable_source_fetch
Source0:	https://git.omame.tech/CyberOS/cyber-dock/archive/1.0.0.tar.gz
%description
%global debug_package %{nil}

%prep
%setup -qn %{name}

%build
cmake -B .
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install



%files
%license LICENSE
/usr/share/cyber-dock/
/usr/bin/cyber-dock


%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.0.0
- Initial version