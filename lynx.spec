Summary:	Text based browser for the world wide web
Summary(de):	Text-Browser f�r das WWW 
Summary(fr):	Navigateur en mode texte pour le world wide web
Summary(pl):	Przegl�darka WWW pracuj�ca w trybie tekstowym
Summary(tr):	Metin ekranda WWW taray�c�
Name:		lynx
Version:	2.8.3dev.18
Release:	5
License:	GPL
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source0:	http://sol.slcc.edu/lynx/current/%{name}%{version}.tar.bz2
Source1:	lynx.desktop
Patch0:		lynx-pld.patch
Patch1:		lynx-overflow.patch
Patch2:		lynx-config.patch
Patch3:		lynx.cfg.patch
Patch4:		lynx-helpdir.patch
Patch5:		lynx-DESTDIR.patch
Patch6:		lynx-283d16-ssl.patch
Patch7:		lynx2-8-3-ipv6-20-02-00.patch.gz   
URL:		http://lynx.browser.org/
BuildRequires:	zlib-devel
BuildRequires:	ncurses-devel >= 5.0
Provides:	webclient
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		%{_datadir}/lynx

%description
This a terminal based WWW browser. While it does not make any attempt at
displaying graphics, it has good support for HTML text formatting, forms,
and tables.

%description -l de
Dies ist ein WWW-Browser auf Terminal-Basis. W�hrend kein Versuch
unternommen wird, Grafiken darzustellen, so bietet er doch guten  Support
f�r HTML-Textformatierung, Formulare und Tabellen.

%description -l fr
Navigateur WWW en mode texte. Bien qu'il n'affiche aucun graphique, il sait
bien g�rer le formatage HTML du texte, les formulaires et les tableaux.

%description -l pl
Lynx jest przegl�dark� WWW dzia�aj�c� w trybie tekstowym. Dobrze formatuje
tekst w HTML, ale nie pozwala na wy�wietlanie grafiki.

%description -l tr
Metin ekranda �al��an bir WWW taray�c�d�r. �ekil g�steremese de, formlar ve
tablolar i�in deste�i vard�r.

%prep
%setup  -q -n %{name}2-8-3
%patch0 -p1 
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
CFLAGS="-w -I/usr/include/ncurses"; export CFLAGS
LDFLAGS="-s"; export LDFLAGS
%configure \
	--with-screen=ncurses \
	--enable-nls \
	--without-included-gettext \
	--enable-charset-choice \
	--enable-cjk        \
	--enable-default-colors \
	--enable-file-upload \
	--enable-justify-elts \
	--enable-kbd-layout \
	--enable-read-eta \
	--enable-scrollbar \
	--enable-warnings \
	--enable-default-colors \
	--enable-externs \
	--enable-internal-links \
	--enable-nsl-fork \
	--enable-persistent-cookies \
	--enable-gzip-help \
	--enable-libjs \
	--enable-addrlist-page \
	--enable-prettysrc \
	--enable-source-cache \
	--enable-color-style \
	--enable-cgi-links \
	--enable-exec-links \
	--enable-exec-scripts \
	--disable-cjk \
	--with-zlib \
	--without-socks \
	--without-socks5 \
	--with-ssl

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/WWW

make install install-help \
	DESTDIR=$RPM_BUILD_ROOT \
	helpdir=%{_libdir}/help

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/WWW/lynx.desktop

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	C[HO]* PROBLEMS README samples/* test/* docs/README*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc C[HO]* PROBLEMS.gz README.gz samples test docs/README*

%{_applnkdir}/Network/WWW/lynx.desktop

%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
%{_datadir}/lynx
