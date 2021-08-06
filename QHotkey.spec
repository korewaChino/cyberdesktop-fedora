# This spec file is largely derived from the one found here:
## https://build.opensuse.org/package/view_file/home:mnhauke/QHotkey/QHotkey.spec
# Copyright (c) SUSE Linux GmbH, all rights reserved
#
## # All modifications and additions to the file contributed by third parties
## # remain the property of their copyright owners, unless otherwise agreed
## # upon. The license for this file, and modifications and additions to the
## # file, is the same license as for the pristine package itself (unless the
## # license for the pristine package is not an Open Source License, in which
## # case the license is the MIT License). An "Open Source License" is a
## # license that conforms to the Open Source Definition (Version 1.9)
## # published by the Open Source Initiative.

%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name: QHotkey
Version: 1.4.2
Release: 100%{?dist}
Summary: A global shortcut/hotkey for Desktop Qt-Applications
License: BSD-3-Clause
URL: https://github.com/Skycoder42/QHotkey
Source: https://github.com/Skycoder42/%{name}/archive/refs/tags/%{version}.tar.gz
BuildRequires: cmake pkgconfig
BuildRequires: pkgconfig(Qt5Core) pkgconfig(Qt5Widgets) pkgconfig(Qt5X11Extras) pkgconfig(x11)

%description
The QHotkey is a class that can be used to create hotkeys/global shortcuts,
aka shortcuts that work everywhere, independent of the application state.
This means your application can be active, inactive, minimized or not
visible at all and still receive the shortcuts.

%package static
Summary: Static libraries for %{name}
Requires: %{name} = %{version}

%description static
Static libraries for %{name}

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Development files for %{name} including headers and libraries

%prep
%setup -q

%build
%{set_build_flags}
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .
%make_build

%install
%make_install

%post static -p /sbin/ldconfig
%postun static -p /sbin/ldconfig

%files
%license LICENSE

%files static
%{_libdir}/libqhotkey.a

%files devel
%doc README.md
%{_libdir}/cmake/%{name}
%{_includedir}/%{name}
%{_includedir}/qhotkey.h
