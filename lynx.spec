Summary:	Text based browser for the world wide web
Summary(de):	Text-Browser für das WWW 
Summary(fr):	Navigateur en mode texte pour le world wide web
Summary(pl):	Przegl±darka WWW pracuj±ca w trybie tekstowym
Summary(tr):	Metin ekranda WWW tarayýcý
Name:		lynx
Version:	2.8.4dev.7
Release:	3
License:	GPL
URL:		http://lynx.browser.org
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source0:	http://lynx.isc.org/current/%{name}%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:		%{name}-pld.patch
Patch1:		%{name}-config.patch
Patch2:		%{name}.cfg.patch
Patch3:		http://www.moxienet.com/lynx/%{name}-283-ssl.patch.bz2
Patch4:		%{name}-overflow.patch
Patch5:		%{name}-po_DESTDIR.patch
Patch6:		%{name}-config.hin.patch
Patch7:		%{name}-autoconf.patch
BuildRequires:	zlib-devel
BuildRequires:	slang-devel
BuildRequires:	gettext-devel
# BuildRequires:	socks5-devel
Provides:	webclient
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This a terminal based WWW browser. While it does not make any attempt
at displaying graphics, it has good support for HTML text formatting,
forms, and tables.

%description -l pl
Lynx jest przegl±dark± WWW dzia³aj±c± w trybie tekstowym. Dobrze
formatuje tekst w HTML, ale nie pozwala na wy¶wietlanie grafiki.

%description -l de
Dies ist ein WWW-Browser auf Terminal-Basis. Während kein Versuch
unternommen wird, Grafiken darzustellen, so bietet er doch guten
Support für HTML-Textformatierung, Formulare und Tabellen.

%description -l fr
Navigateur WWW en mode texte. Bien qu'il n'affiche aucun graphique, il
sait bien gérer le formatage HTML du texte, les formulaires et les
tableaux.

%description -l tr
Metin ekranda çalýþan bir WWW tarayýcýdýr. Þekil gösteremese de,
formlar ve tablolar için desteði vardýr.

%prep
%setup  -q -n %{name}2-8-4
%patch0 -p1 
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
autoconf
LDFLAGS="-lcrypto -lssl"; export LDFLAGS
CFLAGS="-I/usr/include/openssl -DUSE_SSL $RPM_OPT_FLAGS"; export CFLAGS
%configure \
	--with-screen=slang \
	--without-included-gettext \
	--with-zlib \
	--with-ssl \
	--enable-kbd-layout \
	--enable-addrlist-page \
	--enable-cgi-links \
	--enable-default-colors \
	--enable-exec-links \
	--enable-exec-scripts \
	--enable-externs \
	--enable-gzip-help \
	--enable-internal-links \
	--enable-ipv6 \
	--enable-libjs \
	--enable-nls \
	--enable-nsl-fork \
	--enable-persistent-cookies \
	--enable-prettysrc \
	--enable-source-cache \
	--enable-warnings 
#	--with-socks5=%{_prefix} \
#	--enable-color-style \

%{__make} SSL_LIBS="-lssl -lcrypto" \
	SSL_DEFINES="-I%{_includedir}/openssl -DUSE_SSL"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/WWW \
	$RPM_BUILD_ROOT%{_datadir}/lynx/help/keystrokes

%{__make} install install-help \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/WWW

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	C[HO]* PROBLEMS README samples/* test/* docs/README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc C[HO]* PROBLEMS.gz README.gz samples test docs/README*

%config %verify(not size mtime md5) %{_libdir}/lynx.cfg
%{_applnkdir}/Network/WWW/lynx.desktop

%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
%{_datadir}/lynx
