Summary:	Text based browser for the world wide web
Summary(de):	Text-Browser für das WWW 
Summary(fr):	Navigateur en mode texte pour le world wide web
Summary(pl):	Przegl±darka WWW pracuj±ca w trybie tekstowym
Summary(tr):	Metin ekranda WWW tarayýcý
Name:		lynx
Version:	2.8.2dev.20
Release:	1
Copyright:	GPL
URL:		http://lynx.browser.org
Group:		Networking
Group(pl):	Sieciowe
Source0:	http://sol.slcc.edu/lynx/current/%{name}%{version}.tar.bz2
Source1:	%{name}.wmconfig
Patch0:		lynx-pld.patch
Patch1:		lynx-overflow.patch
Patch2:		lynx-config.patch
Patch4:		lynx.cfg.patch
Patch6:		lynx-dev.19.patch
Requires:	indexhtml
Requires:	zlib >= 1.1.3-5
Requires:	ncurses >= 4.2-12
Buildroot:	/tmp/%{name}-%{version}-%{release}-root

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
%patch6 -p1

%build
CFLAGS="-w" LDFLAGS="-s" \
./configure \
	--prefix=/usr \
	--libdir=/etc \
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
	--with-zlib 
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
install -d $RPM_BUILD_ROOT/usr/share/lynx/help/keystrokes

make	prefix=$RPM_BUILD_ROOT/usr \
	libdir=$RPM_BUILD_ROOT/etc \
	helpdir=$RPM_BUILD_ROOT/usr/share/lynx/help \
	install \
	install-help
	

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/lynx

gzip -9fn $RPM_BUILD_ROOT/usr/man/man1/*
gzip -9fn C[HO]* PROBLEMS README samples/* test/* docs/README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc C[HO]* PROBLEMS.gz README.gz samples test docs/README*

%config %verify(not size mtime md5) /etc/lynx.cfg
%config(missingok) /etc/X11/wmconfig/lynx

%attr(755,root,root) /usr/bin/*

/usr/man/man1/*
/usr/share/lynx

%lang(de) /usr/share/locale/de/LC_MESSAGES/lynx.mo
%lang(es) /usr/share/locale/es/LC_MESSAGES/lynx.mo
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/lynx.mo
%lang(it) /usr/share/locale/it/LC_MESSAGES/lynx.mo
%lang(ko) /usr/share/locale/ko/LC_MESSAGES/lynx.mo
%lang(nl) /usr/share/locale/nl/LC_MESSAGES/lynx.mo
%lang(no) /usr/share/locale/no/LC_MESSAGES/lynx.mo
%lang(pl) /usr/share/locale/pl/LC_MESSAGES/lynx.mo
%lang(pt) /usr/share/locale/pt/LC_MESSAGES/lynx.mo
%lang(sl) /usr/share/locale/sl/LC_MESSAGES/lynx.mo
%lang(sv) /usr/share/locale/sv/LC_MESSAGES/lynx.mo

%changelog
* Thu Mar  4 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.8.2dev.19-1]
- added /usr/share/locale/*/LC_MESSAGES/lynx.mo files fo %files,
- added requiring ncurses >= 4.2-12 and zlib >= 1.1.3-5
  for installing lynx in proper enviroment.

* Thu Mar  4 1999 Artur Frysiak <wiget@usa.net> 
- added new configure option: --enable-nls --without-included-gettext 
  --enable-addrlist-page  --enable-libjs
- added lynx-dev.19.patch (correct typo, included in next release)  
  
* Wed Feb 17 1999 Artur Frysiak <wiget@usa.net>
  [2.8.2dev.17-1d]
- gziped help files
- change install metod

* Tue Feb 16 1999 Artur Frysiak <wiget@usa.net>
  [2.8.2dev.16-1d]
- moved help and test files to /usr/share/lynx
- changed default color scheme

* Fri Feb 05 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.8.2dev15-2d]
- changed group,
- compressed documentation.

* Sun Jan 10 1999 Artur Frysiak <wiget@usa.net>
  [2.8.2dev.12-1d]
- added URL and Group(pl) tags

* Mon Sep 01 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.8-5d]
- build against glibc-2.1,
- changed Buildroot to /var/tmp/%%{name}-%%{version}-%%{release}-root,
- changed permission of lynx to 711,
- translation modified for pl.

* Sun Aug 30 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.8-5]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- URL in HELPFILE in /etc/lynx.cfh changed to localhost,
- removed INSTALLATION from %doc,
- added %attr and %defattr macros in %files (allow build package from
  non-root account).

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon May 04 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 2.8rel3
- fixed mailto: buffer overflow (used Alan's patch)

* Fri Mar 20 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.8
- added buildroot

* Tue Jan 13 1998 Erik Troan <ewt@redhat.com>
- updated to 2.7.2
- enabled lynxcgi

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- updated from 2.6 to 2.7.1
- moved /usr/lib/lynx.cfg to /etc/lynx.cfg
- build with slang instead of ncurses
- made default startup file be file:/usr/doc/HTML/index.html
