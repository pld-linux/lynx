Summary:     Text based browser for the world wide web
Name:        lynx
Version:     2.8.2dev.14
Release:     1d
Copyright:   GPL
URL:         http://lynx.browser.org
Group:       Applications/Networking
Group(pl):   Aplikacje/Sieæ
Source:      ftp://www.slcc.edu/pub/lynx/current/%{name}%{version}.tar.bz2
Source1:     %{name}.wmconfig
Patch:       %{name}-pld.patch
Patch1:      %{name}-overflow.patch
Buildroot:   /tmp/%{name}-%{version}-root
Summary(de): Text-Browser für das WWW 
Summary(fr): Navigateur en mode texte pour le world wide web
Summary(pl): Przegl±darka WWW pracuj±ca w trybie tekstowym
Summary(tr): Metin ekranda WWW tarayýcý

%description
This a terminal based WWW browser. While it does not make any attempt
at displaying graphics, it has good support for HTML text formatting,
forms, and tables.

%description -l pl
Lynx jest przegl±dark± WWW dzia³aj±c± w trybie tekstowym. Dobrze 
formatuje tekst w HTML ale nie pozwala na wy¶wietlanie grafiki.

%description -l de
Dies ist ein WWW-Browser auf Terminal-Basis. Während kein Versuch 
unternommen wird, Grafiken darzustellen, so bietet er doch guten 
Support für HTML-Textformatierung, Formulare und Tabellen. 

%description -l fr
Navigateur WWW en mode texte. Bien qu'il n'affiche aucun graphique, il
sait bien gérer le formatage HTML du texte, les formulaires et les tableaux.

%description -l tr
Metin ekranda çalýþan bir WWW tarayýcýdýr. Þekil gösteremese de, formlar ve
tablolar için desteði vardýr.

%prep
%setup -q -n %{name}2-8-2
%patch  -p1 
%patch1 -p1

%build
CFLAGS="-w" LDFLAGS=-s ./configure --prefix=/usr --libdir=/etc \
	--with-screen=slang --enable-warnings \
	--enable-default-colors --enable-externs \
	--enable-internal-links --enable-nsl-fork \
	--enable-persistent-cookies --with-zlib 
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

make install prefix=$RPM_BUILD_ROOT/usr libdir=$RPM_BUILD_ROOT/etc

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/lynx

strip $RPM_BUILD_ROOT/usr/bin/lynx

bzip2 -9 $RPM_BUILD_ROOT/usr/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs README samples
%doc test lynx.hlp lynx_help

%config %verify(not size mtime md5) /etc/lynx.cfg
%config(missingok) /etc/X11/wmconfig/lynx

%attr(711,root,root) /usr/bin/*
%attr(644,root, man) /usr/man/man1/*

%changelog
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
