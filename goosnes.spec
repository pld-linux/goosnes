%define		fversion	%(echo %{version} |tr r -)
Summary:	Graphical frontend for the snes9x Super NES emulator
Summary(pl):	Graficzna nak�adka na emulator Super NES snes9x
Name:		goosnes
Version:	0.5.2r1
Release:	1
Source0:	http://bard.sytes.net/debian/dists/unstable/main/source/%{name}_%{fversion}.tar.gz
# Source0-md5:	032cb84df865f4b9e76973f8c0195804
License:	GPL
Group:		Application/Emulators
URL:		http://bard.sytes.net/goosnes/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
Requires:	snes9x
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GooSNES is a little GTK+ frontend for SNES9x. It allows users to set
SNES9x options without typing a pageful of command line options at a
prompt. It also allows users to select a SNES image and launch SNES9x
at a click.

%description -l pl
GooSNES jest ma�� nak�adk� w GTK+ na SNES9x. Pozwala u�ytkownikom
ustawia� opcje SNES9x bez wpisywania stron komand z lini polece�.
Pozwala te� wybra� obraz SNES i uruchomi� SNES9x jednym klikni�ciem.

%prep
%setup -q -n %{name}-%(echo %{version} |cut -c -5)

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-gtk-version=2.0
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
