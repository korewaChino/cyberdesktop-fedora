Name:		cyber-desktop
Version:	2021.05.20
Release:	1%{?dist}
BuildArch: noarch
Summary:	Metapackage for the Cyber Desktop Environment
License:	GPL
Group:	Metapackages

#BuildRequires: scl-utils-build
Requires:	xorg-x11-server-Xorg
Requires:	libcyber-system
Requires:	meuikit
Requires:	cyber-qt-plugins
Requires:	cyber-kwin-plugins
Requires:	cyber-workspace
Requires:	cyber-wallpapers
Requires:	cyber-settings
Requires:	cyber-icon-theme
Requires:	cyber-dock
Requires:	cyber-launcher
Requires:	cyber-terminal
Requires:	cyber-recorder
Requires:	cyber-fm
Requires:	cyber-disk-usage
Requires:	cyber-calculator
Requires:	cyber-edit
%description
A metapackage that install the Cyber Desktop Environment

%install
exit 0

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 2021.05.20
- Initial version
