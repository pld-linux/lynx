Summary:	Text based browser for the world wide web
Summary(de):	Text-Browser für das WWW 
Summary(fr):	Navigateur en mode texte pour le world wide web
Summary(pl):	Przegl±darka WWW pracuj±ca w trybie tekstowym
Summary(tr):	Metin ekranda WWW tarayýcý
Name:		lynx
Version:	2.8.4dev.3
Release:	1
License:	GPL
URL:		http://lynx.browser.org
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source0:	http://lynx.isc.org/current/%{name}%{version}.tar.bz2
Source1:	lynx.wmconfig
Patch0:		lynx-pld.patch
Patch1:		lynx-config.patch
Patch2:		lynx.cfg.patch
Patch3:		http://www.moxienet.com/lynx/lynx-283-ssl.patch.bz2
Patch4:		lynx-overflow.patch
Patch5:		lynx-po_DESTDIR.patch
BuildRequires:	zlib-devel
BuildRequires:	slang-devel
# BuildRequires:	socks5-devel
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

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--with-screen=slang \
	--without-included-gettext \
	--with-zlib \
	--with-ssl \
	--enable-addrlist-page \
	--enable-cgi-links \
	--enable-default-colors \
	--enable-exec-links \
	--enable-exec-scripts \
	--enable-externs \
	--enable-gzip-help \
	--enable-internal-links \
	--enable-libjs \
	--enable-nls \
	--enable-nsl-fork \
	--enable-persistent-cookies \
	--enable-prettysrc \
	--enable-source-cache \
	--enable-warnings 
#	--with-socks5=%{_prefix} \
#	--enable-color-style \

%{__make} 	SSL_LIBS= "-lssl -lsslcrypto " \
	SSL_DEFINES= "-I%{_includedir}/ssl -DUSE_SSL"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig \
	$RPM_BUILD_ROOT%{_datadir}/lynx/help/keystrokes

%{__make} install install-help \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/lynx

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	C[HO]* PROBLEMS README samples/* test/* docs/README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc C[HO]* PROBLEMS.gz README.gz samples test docs/README*

%config %verify(not size mtime md5) %{_libdir}/lynx.cfg
%config(missingok) %{_sysconfdir}/X11/wmconfig/lynx

%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
%{_datadir}/lynx
