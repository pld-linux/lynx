Summary:	Text based browser for the world wide web
Summary(de):	Text-Browser für das WWW
Summary(es):	Navegador web modo texto
Summary(fr):	Navigateur en mode texte pour le world wide web
Summary(ja):	¥Æ¥­¥¹¥È¥Ù¡¼¥¹¤Î¥¦¥§¥Ö¥Ö¥é¥¦¥¶
Summary(pl):	Przegl±darka WWW pracuj±ca w trybie tekstowym
Summary(pt_BR):	Navegador web modo texto
Summary(tr):	Metin ekranda WWW tarayýcý
Name:		lynx
Version:	2.8.5rel.1
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://lynx.isc.org/current/%{name}%{version}.tar.bz2
# Source0-md5:	d1e5134e5d175f913c16cb6768bc30eb
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source3-md5:	b5e02f86a8ee7bce4d8b97e4b6491714
Patch0:		%{name}-pld.patch
Patch1:		%{name}.cfg.patch
Patch2:		%{name}-po_DESTDIR.patch
Patch3:		%{name}-config.hin.patch
Patch4:		%{name}-autoconf.patch
Patch5:		%{name}-config.patch
Patch6:		%{name}-acfix.patch
Patch7:		%{name}-gzip_fallback.patch
Patch8:		%{name}-etc_dir.patch
URL:		http://lynx.browser.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel >= 0.9.7d
#BuildRequires:	socks5-devel
BuildRequires:	zlib-devel
Provides:	webclient
Obsoletes:	lynx-ssl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	"-fomit-frame-pointer"

%description
This a terminal based WWW browser. While it does not make any attempt
at displaying graphics, it has good support for HTML text formatting,
forms, and tables.

%description -l de
Dies ist ein WWW-Browser auf Terminal-Basis. Während kein Versuch
unternommen wird, Grafiken darzustellen, so bietet er doch guten
Support für HTML-Textformatierung, Formulare und Tabellen.

%description -l es
Este es un browser WWW para terminal en modo texto. Mientras no hace
ningún intento de enseñar gráficos, posee un buen soporte para el
formato de texto HTML, formularios y tablas.

%description -l fr
Navigateur WWW en mode texte. Bien qu'il n'affiche aucun graphique, il
sait bien gérer le formatage HTML du texte, les formulaires et les
tableaux.

%description -l ja
lynx ¤Ï¥Æ¥­¥¹¥È¥Ù¡¼¥¹¤Î¥¦¥§¥Ö¥Ö¥é¥¦¥¶¤Ç¤¢¤ë¡£lynx ¤Ï²¿¤Î¥¤¥á¡¼¥¸¤â
É½¼¨¤·¤Ê¤¤¤¬¥Õ¥ì¡¼¥à¡¢¥Æ¡¼¥Ö¥ë¤½¤·¤ÆÂ¾¤Î HTML ¥¿¥°¤ò¥µ¥Ý¡¼¥È¤¹¤ë¡£
¥°¥é¥Õ¥£¥«¥ë¤Ê¥Ö¥é¥¦¥¶¤ËÂÐ¤¹¤ë lynx ¤Î¥¢¥É¥Ð¥ó¥Æ¡¼¥¸¤Ï¥¹¥Ô¡¼¥É¤Ç¤¢¤ë¡£
lynx ¤Ï¥¦¥§¥Ö¥Ú¡¼¥¸¤òÉ½¼¨¤¹¤ë¤Î¤Ë¤¹¤Ð¤ä¤¯Â¨ºÂ¤Ë³«»Ï¤·¤¿¤ê½ªÎ»¤·¤¿¤ê¤¹¤ë¡£

¤³¤ÎÂ®¤¤¡¢¥°¥é¥Õ¥£¥«¥ë¤Ç¤Ê¤¤¥Ö¥é¥¦¥¶¤ò»î¤·¤¿¤±¤ì¤Ð¥¤¥ó¥¹¥È¡¼¥ë¤·¤Ê¤µ¤¤¡£
(¤½¤ÎÄ¹½ê¤Î¤è¤µ¤¬¤ï¤«¤ë¤Ç¤¢¤í¤¦)

%description -l pl
Lynx jest przegl±dark± WWW dzia³aj±c± w trybie tekstowym. Dobrze
formatuje tekst w HTML, ale nie pozwala na wy¶wietlanie grafiki.

%description -l pt_BR
Este é um browser WWW para terminal em modo texto. Enquanto ele não
faz nenhuma tentativa para mostrar gráficos, possui um bom suporte
para o formato de texto HTML, formulários e tabelas.

%description -l tr
Metin ekranda çalýþan bir WWW tarayýcýdýr. Þekil gösteremese de,
formlar ve tablolar için desteði vardýr.

%prep
%setup  -q -n %{name}2-8-5
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
cp /usr/share/automake/config.sub .
%{__autoconf}
%configure \
	--with-screen=ncurses \
	--without-included-gettext \
	--with-bzlib \
	--with-zlib \
	--with-ssl \
	--enable-justify-elts \
	--enable-nested-tables \
	--enable-read-eta \
	--enable-kbd-layout \
	--enable-addrlist-page \
	--enable-cgi-links \
	--enable-default-colors \
	--enable-file-upload \
	--enable-exec-links \
	--enable-exec-scripts \
	--enable-externs \
	--enable-gzip-help \
	--enable-internal-links \
	--enable-ipv6 \
	--enable-nls \
	--enable-nsl-fork \
	--enable-persistent-cookies \
	--enable-prettysrc \
	--enable-source-cache \
	--enable-warnings
#	--with-socks5=%{_prefix} \
#	--enable-color-style \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/lynx/help

%{__make} install install-help \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

bzip2 -dc %{SOURCE3} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGES COPYHEADER PROBLEMS README samples test docs/README*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/lynx.cfg
%attr(755,root,root) %{_bindir}/*
%{_datadir}/lynx
%{_desktopdir}/lynx.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/*
%lang(cs) %{_mandir}/cs/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(pl) %{_mandir}/pl/man1/*
