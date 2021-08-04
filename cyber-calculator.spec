%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name:		cyber-calculator
Version:	1.0.0
Release:	0a%{?dist}
Summary:	Cyber Calculator
License:	GPLv3+
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:	git
BuildRequires:	qt5-qttools qt5-qttools-devel qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel qt5-linguist
BuildRequires:	meuikit-devel
Source0:	https://git.omame.tech/CyberOS/cyber-calculator/archive/1.0.0.tar.gz
%description
Cyber Calculator

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
%{_datadir}/cyber-calculator/
%{_bindir}/cyber-calculator
%{_datadir}/applications/cyber-calculator.desktop

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.0.0
- Initial version
