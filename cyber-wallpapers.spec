%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

Name:		cyber-wallpapers
Version:	1.1.0
Release:	%{?dist}
Summary:	Wallpapers included with the Cyber Desktop Environment
License:	GPLv3+
URL:		getcyberos.org
BuildRequires:	cmake gcc
Source0:	https://git.omame.tech/CyberOS/cyber-wallpapers/archive/1.1.0.tar.gz
BuildArch:  noarch
BuildRoot: %{_tmppath}/%{name}
%description
The wallpaper that ships with Cyber Desktop

%prep
%setup -qn %{name}

%build
%{set_build_flags}
#mkdir -p build;
#cd build;
cmake -B .
%make_build

%install
#cd "$srcdir/$pkgname/build";
#make DESTDIR="$pkgdir/" install


%files
# TODO: Add files

%changelog
* Tue Aug 03 2021 korewaChino <crkza1134@gmail.com> - 1.1.0
- Initial version
