Name:		cyber-launcher
Version:	1.0.0
Release:	%{?dist}
Summary:	The Cyber Desktop Launcher
License:	GPL-3.0-or-later
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:	git
BuildRequires:	qt5-qttools
Requires:	qt5-base
Requires:	qt5-quickcontrols2
Requires:	meuikit
%undefine _disable_source_fetch
Source0:	https://git.omame.tech/CyberOS/cyber-launcher/archive/1.0.0.tar.gz
BuildRoot: %{_tmppath}/%{name}
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
/usr/bin/cyber-launcher
/usr/share/cyber-launcher/

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.0.0
- Initial version
