%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name:		cyber-workspace
Version:	1.0.3
Release:	0c%{?dist}
Summary:	Cyber Workspace
License:	GPLv3+
URL:		https://getcyberos.org
BuildRequires:	cmake pkgconfig
BuildRequires:	extra-cmake-modules
BuildRequires:	polkit-devel polkit-qt5-1-devel libSM-devel xcb-util-devel xcb-util-image-devel libXtst-devel pulseaudio-libs-devel
BuildRequires:	qt5-qtbase-devel qt5-qtx11extras-devel qt5-qttools-devel qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel qt5-linguist
BuildRequires:	kf5-kwindowsystem-devel kf5-kwayland-devel
BuildRequires:	meuikit-devel
BuildRequires:	QHotkey-devel QHotkey-static
Requires:	xdg-user-dirs
Source0: https://git.omame.tech/CyberOS/cyber-workspace/archive/1.0.3.tar.gz
Patch0: https://github.com/korewaChino/cyberdesktop-fedora/raw/2b17b331be9e1bfd339df00a9a1495dbfd52e9e0/patches/cyber-workspace/0000-hotkeys-fix-cmakelists.patch

%description
Applications that build the Cyber Desktop environment

%prep
%setup -qn %{name}
# patch hotkeys/CMakeLists.txt to properly use QHotkey
patch hotkeys/CMakeLists.txt -i %{PATCH0}

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
