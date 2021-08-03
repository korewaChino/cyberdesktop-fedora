Name:           meuikit
Version:        1.0.0
Release:        1
Summary:        Cyber GUI Library 

License:        GPLv3+
URL:            https://getcyberos.org

BuildRequires:  qt5-qtbase-devel qt5-qtquickcontrols2-devel qt5-qtx11extras-devel kf5-kwindowsystem-devel cmake make extra-cmake-modules
Requires:       qt5-qtbase qt5-qtquickcontrols2 qt5-qtx11extras kf5-kwindowsystem
%undefine _disable_source_fetch
Source0:        https://git.omame.tech/CyberOS/meuikit/archive/1.0.0.tar.gz
BuildRoot: %{_tmppath}/%{name}
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
/usr/lib/cmake/MeuiKit/
/usr/lib64/libMeuiKit.so
/usr/lib64/qt5/qml/MeuiKit/
/usr/lib64/qt5/qml/QtQuick/Controls.2/meui-style/



%changelog
* Tue Aug 03 2021 korewaChino <cappy@cappuchino.xyz>
- init package port
