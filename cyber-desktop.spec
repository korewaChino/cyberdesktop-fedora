Name:		cyber-desktop
Version:	0.20210520
Release:	99%{?dist}
BuildArch: noarch
Summary:	Metapackage for the Cyber Desktop Environment
License:	GPL
Group:	Metapackages

#BuildRequires: scl-utils-build
Requires:	xorg-x11-server-Xorg
Requires:	cyber-qt-plugins
Requires:	cyber-kwin-plugins
Requires:	cyber-workspace
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

%prep

%build

%install

%files

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 2021.05.20
- Initial version
