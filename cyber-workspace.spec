Name:		cyber-workspace
Version:	1.0.3
Release:	%{?dist}
Summary:	Cyber Workspace
License:	GPL-3.0-or-later
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:	extra-cmake-modules
BuildRequires:	git
BuildRequires:	pkgconf
BuildRequires:	qt5-qttools polkit-devel polkit-qt5-1-devel libSM-devel xcb-util-image-devel libXtst-devel
Requires:	kwayland
Requires:	kwindowsystem
Requires:	kwin
Requires:	qt5-base
Requires:	qt5-quickcontrols2
Requires:	polkit
Requires:	polkit-qt5
Requires:	meuikit
Requires:	cyber-wallpapers
Requires:	xdg-user-dirs
#Requires:	qhotkey
%undefine _disable_source_fetch
Source0:	https://git.omame.tech/CyberOS/cyber-workspace/archive/1.0.3.tar.gz
%description
%define debug_package %{nil}
%define _build_id_links none
%prep
%setup -qn %{name}




%build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install




%files 
%license LICENSE
/etc/xdg/autostart/cyber-polkit-agent.desktop
/usr/bin/cyber-desktop-daemon
/usr/bin/cyber-hotkeys
/usr/bin/cyber-notification-daemon
/usr/bin/cyber-polkit-agent
/usr/bin/cyber-screen-brightness
/usr/bin/cyber-session
/usr/bin/cyber-settings-daemon
/usr/bin/cyber-shutdown
/usr/bin/cyber-xembedsniproxy
/usr/share/cyber-desktop-daemon
/usr/share/cyber-polkit-agent/
/usr/share/cyber-settings-daemon/
/usr/share/cyber-shutdown/
/usr/share/polkit-1/actions/org.cyber.brightness.pkexec.policy
/usr/share/xsessions/cyber-xsession.desktop
%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.0.3
- Initial version
