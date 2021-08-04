%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name:		cyber-workspace
Version:	1.0.3
Release:	1%{?dist}
Summary:	Cyber Workspace
License:	GPLv3+
URL:		https://getcyberos.org
BuildRequires:	cmake
BuildRequires:	extra-cmake-modules
BuildRequires:	git
BuildRequires:	pkgconf
BuildRequires:	polkit-devel polkit-qt5-1-devel libSM-devel xcb-util-image-devel libXtst-devel qt5-linguist
BuildRequires:	qt5-qttools qt5-qttools-devel qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel qt5-linguist
BuildRequires:	meuikit-devel
BuildRequires:	QHotkey-devel QHotkey-static cmake(QHotkey)
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
Requires:	QHotkey
Source0:	https://git.omame.tech/CyberOS/cyber-workspace/archive/1.0.3.tar.gz

%description
Applications that build the Cyber Desktop environment

%prep
%setup -qn %{name}

%build
%{set_build_flags}
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .
make %{?_smp_mflags}

%install
%make_install

%files 
%license LICENSE
/etc/xdg/autostart/cyber-polkit-agent.desktop
%{_bindir}/cyber-desktop-daemon
%{_bindir}/cyber-hotkeys
%{_bindir}/cyber-notification-daemon
%{_bindir}/cyber-polkit-agent
%{_bindir}/cyber-screen-brightness
%{_bindir}/cyber-session
%{_bindir}/cyber-settings-daemon
%{_bindir}/cyber-shutdown
%{_bindir}/cyber-xembedsniproxy
%{_datadir}/cyber-desktop-daemon
%{_datadir}/cyber-polkit-agent/
%{_datadir}/cyber-settings-daemon/
%{_datadir}/cyber-shutdown/
%{_datadir}/polkit-1/actions/org.cyber.brightness.pkexec.policy
%{_datadir}/xsessions/cyber-xsession.desktop
%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.0.3
- Initial version
