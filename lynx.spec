Summary:     Text based browser for the world wide web
Summary(de): Text-Browser für das WWW 
Summary(fr): Navigateur en mode texte pour le world wide web
Summary(pl): Przegl±darka WWW w trybie tekstowym
Summary(tr): Metin ekranda WWW tarayýcý
Name:        lynx
Version:     2.8
Release:     5
Copyright:   GPL
Group:       Applications/Networking
Source0:     ftp://www.slcc.edu/pub/lynx/fote/lynx2.8rel.3.tar.gz
Source1:     lynx.wmconfig
Patch0:      lynx-2.8-redhat.patch
Patch1:      lynx2-8-overflow.patch
Requires:    indexhtml
Buildroot:   /tmp/%{name}-%{version}-root

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
Lynx jest przegl±dark± WWW w trybie tekstowym. Dobrze formatuje HTML
w³±cznie z formami i tabelami ale nie pozwala na wy¶wietlanie grafiki.

%description -l tr
Metin ekranda çalýþan bir WWW tarayýcýdýr. Þekil gösteremese de, formlar ve
tablolar için desteði vardýr.

%prep
%setup -q -n lynx2-8
%patch0 -p1 -b .redhat
%patch1 -p1 -b .overflow

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --libdir=/etc \
	--with-screen=slang --enable-warnings \
	--enable-default-colors --enable-externs \
	--enable-internal-links --enable-nsl-fork --with-zlib
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
make install prefix=$RPM_BUILD_ROOT/usr libdir=$RPM_BUILD_ROOT/etc
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/lynx

sed -e "s/HELPFILE:http:\/\/www.crl.com\/\~subir\/lynx\/lynx_help\/lynx_help_main.html/HELPFILE\:file:\/\/localhost\/\/usr\/doc\/%{name}-%{version}\/lynx_help\/lynx_help_main.html/" \
	lynx.cfg > $RPM_BUILD_ROOT/etc/lynx.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc docs README samples test lynx.hlp lynx_help
%config /etc/lynx.cfg
%config(missingok) /etc/X11/wmconfig/lynx
%attr(755, root, root) /usr/bin/*
%attr(755, root,  man) /usr/man/man1/*

%changelog
* Sun Aug 30 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.8-5]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- URL in HELPFILE in /etc/lynx.cfh changed to localhost,
- removed INSTALLATION from %doc,
- added pl translation (Wojtek ¦lusarczyk <wojtek@shadow.eu.org>),
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
