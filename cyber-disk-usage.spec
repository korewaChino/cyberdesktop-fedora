%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name:		cyber-disk-usage
Version:	1.0.0
Release:	99%{?dist}
Summary:	Cyber Disk Usage
License:	GPLv3+
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:	udisks2-qt5-devel
BuildRequires:	qt5-qttools qt5-qttools-devel qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel qt5-linguist qt5-qtbase-devel
BuildRequires:	meuikit-devel
Source0:	https://git.omame.tech/CyberOS/cyber-disk-usage/archive/%{version}.tar.gz
%description
Disk usage monitor application for Cyber Desktop

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
%{_datadir}/cyber-disk-usage/
%{_bindir}/cyber-disk-usage
%{_datadir}/applications/cyber-disk-usage.desktop

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.0.0
- Initial version
