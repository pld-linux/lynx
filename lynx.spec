Summary:	Text based browser for the world wide web
Summary(de):	Text-Browser für das WWW 
Summary(fr):	Navigateur en mode texte pour le world wide web
Summary(pl):	Przegl±darka WWW pracuj±ca w trybie tekstowym
Summary(tr):	Metin ekranda WWW tarayýcý
Name:		lynx
Version:	2.8.2rel.1
Release:	1
Copyright:	GPL
Group:		Networking
Group(pl):	Sieciowe
Source0:	http://sol.slcc.edu/lynx/current/%{name}%{version}.tar.bz2
Source1:	lynx.wmconfig
Patch0:		lynx-pld.patch
Patch1:		lynx-overflow.patch
Patch2:		lynx-config.patch
Patch4:		lynx.cfg.patch
Patch5:		lynx-noroot.patch
URL:		http://lynx.browser.org/
BuildPrereq:	zlib-devel
BuildPrereq:	ncurses-devel
#Requires:	indexhtml
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This a terminal based WWW browser. While it does not make any attempt
at displaying graphics, it has good support for HTML text formatting,
forms, and tables.

%description -l de
Dies ist ein WWW-Browser auf Terminal-Basis. Während kein Versuch 
unternommen wird, Grafiken darzustellen, so bietet er doch guten 
Support für HTML-Textformatierung, Formulare und Tabellen. 

%description -l fr
Navigateur WWW en mode texte. Bien qu'il n'affiche aucun graphique, il
sait bien gérer le formatage HTML du texte, les formulaires et les tableaux.

%description -l pl
Lynx jest przegl±dark± WWW dzia³aj±c± w trybie tekstowym. Dobrze
formatuje tekst w HTML ale nie pozwala na wy¶wietlanie grafiki.

%description -l tr
Metin ekranda çalýþan bir WWW tarayýcýdýr. Þekil gösteremese de, formlar ve
tablolar için desteði vardýr.

%prep
%setup  -q -n %{name}2-8-2
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1

%build
CFLAGS="-w" LDFLAGS="-s" \
    ./configure \
	--prefix=%{_prefix} \
	--libdir=%{_datadir}/lynx \
	--mandir=%{_mandir} \
	--with-screen=ncurses \
	--enable-nls \
	--without-included-gettext \
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
	--with-zlib \
	--without-socks \
	--without-socks5 \
	--without-ssl \
	%{_target_platform}
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/X11/wmconfig \
	$RPM_BUILD_ROOT%{_datadir}/lynx/help/keystrokes 

make	DESTDIR=$RPM_BUILD_ROOT \
	helpdir=%{_datadir}/%{name}/help \
	install \
	install-help

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/lynx

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man1/* \
	C[HO]* PROBLEMS README samples/* test/* docs/README*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc C[HO]* PROBLEMS.gz README.gz samples test docs/README*

/etc/X11/wmconfig/lynx

%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*

%dir %{_datadir}/lynx
%{_datadir}/lynx/help

%{_datadir}/lynx/lynx.lss
%{_datadir}/lynx/lynx.cfg

%changelog
* Fri May 28 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.8.2pre.8-1]
- update to 2.8.2pre.8,
- some fixes for correct build,
- antiroot patch,
- removed %config from %{_datadir}/lynx/lynx.*,

* Tue May 18 1999 Artur Frysiak <wiget@pld.org.pl>
  [2.8.2pre.4-1]
- based on Red Hat lynx 2.8-4 (but many changes)
- pl translation by Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- de, fr and tr translations by Prospector System <bugs@redhat.com>
