%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name:           meuikit
Version:        1.0.0
Release:        2%{?dist}
Summary:        Cyber GUI Library

License:        GPLv3+
URL:            https://getcyberos.org

BuildRequires:  qt5-qtbase-devel qt5-qtquickcontrols2-devel qt5-qtx11extras-devel kf5-kwindowsystem-devel cmake make extra-cmake-modules
Requires:       qt5-qtbase qt5-qtquickcontrols2 qt5-qtx11extras kf5-kwindowsystem

Source0:        https://git.omame.tech/CyberOS/meuikit/archive/1.0.0.tar.gz

%description
MeuiKit is the UI library for Cyber Desktop

%package devel
Summary: Development headers for MeuiKit
Requires: %{name} = %{version}-%{release}, cmake
Provides: cmake(%{name})
%description devel
This package provides files sufficient to build software against %{name}

%prep
%setup -qn %{name}

%build
%{set_build_flags}
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files devel
/usr/lib/cmake/MeuiKit
%{_libdir}/qt5/qml/MeuiKit/
%{_libdir}/qt5/qml/QtQuick/Controls.2/meui-style/

%files 
%license LICENSE
%{_libdir}/libMeuiKit.so

%changelog
* Wed Aug 04 2021 rmnscnce <rmnscnce@ya.ru>
- specfile overhaul

* Tue Aug 03 2021 korewaChino <cappy@cappuchino.xyz>
- init package port
