Name:		cyber-wallpapers
Version:	1.1.0
Release:	%{?dist}
Summary:	Wallpapers included with the Cyber Desktop Environment
License:	GPL-3.0-or-later
URL:		getcyberos.org
BuildRequires:	cmake
%undefine _disable_source_fetch
Source0:	https://git.omame.tech/CyberOS/cyber-wallpapers/archive/1.1.0.tar.gz
BuildArch:  noarch
BuildRoot: %{_tmppath}/%{name}
%description


%prep
%setup -qn %{name}

%build
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
