Name:		cyber-calculator
Version:	1.0.0
Release:	%{?dist}
Summary:	Cyber Calculator
License:	GPL-3.0-or-later
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:	git
BuildRequires:	qt5-qttools
Requires:	qt5-qtbase
Requires:	qt5-qtquickcontrols2
Requires:	meuikit
%undefine _disable_source_fetch
Source0:	https://git.omame.tech/CyberOS/cyber-calculator/archive/1.0.0.tar.gz
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
/usr/share/cyber-calculator/
/usr/bin/cyber-calculator
/usr/share/applications/cyber-calculator.desktop

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.0.0
- Initial version
