Name:		cyberos-keyring
Version:	20210301
Release:	%{?dist}
Summary:	CyberOS PGP keyring
License:	GPL
URL:		
Source0:	cyberos.gpg
Source1:	cyberos-trusted

%prep
%setup

%build
%make_build

%install
#install -D -m644 cyberos.gpg "$pkgdir/usr/share/pacman/keyrings/cyberos.gpg";
#install -D -m644 cyberos-trusted "$pkgdir/usr/share/pacman/keyrings/cyberos-trusted"


%files
# TODO: Add files

%changelog
* Tue Aug 03 2021  <> - 20210301
- Initial version
