#
# TODO: merge patches (some change the same files in the same places)
#
Summary:	Text based browser for the world wide web
Summary(de.UTF-8):	Text-Browser für das WWW
Summary(es.UTF-8):	Navegador web modo texto
Summary(fr.UTF-8):	Navigateur en mode texte pour le world wide web
Summary(ja.UTF-8):	テキストベースのウェブブラウザ
Summary(pl.UTF-8):	Przeglądarka WWW pracująca w trybie tekstowym
Summary(pt_BR.UTF-8):	Navegador web modo texto
Summary(tr.UTF-8):	Metin ekranda WWW tarayıcı
Name:		lynx
Version:	2.8.7
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://lynx.isc.org/lynx2.8.7/%{name}%{version}.tar.bz2
# Source0-md5:	493af4c77ef6761e3f0157cd1be033a0
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

%define		specflags_ia32	 -fomit-frame-pointer

%description
This a terminal based WWW browser. While it does not make any attempt
at displaying graphics, it has good support for HTML text formatting,
forms, and tables.

%description -l de.UTF-8
Dies ist ein WWW-Browser auf Terminal-Basis. Während kein Versuch
unternommen wird, Grafiken darzustellen, so bietet er doch guten
Support für HTML-Textformatierung, Formulare und Tabellen.

%description -l es.UTF-8
Este es un browser WWW para terminal en modo texto. Mientras no hace
ningún intento de enseñar gráficos, posee un buen soporte para el
formato de texto HTML, formularios y tablas.

%description -l fr.UTF-8
Navigateur WWW en mode texte. Bien qu'il n'affiche aucun graphique, il
sait bien gérer le formatage HTML du texte, les formulaires et les
tableaux.

%description -l ja.UTF-8
lynx はテキストベースのウェブブラウザである。lynx は何のイメージも
表示しないがフレーム、テーブルそして他の HTML タグをサポートする。
グラフィカルなブラウザに対する lynx のアドバンテージはスピードである。
lynx はウェブページを表示するのにすばやく即座に開始したり終了したりする。

この速い、グラフィカルでないブラウザを試したければインストールしなさい。
(その長所のよさがわかるであろう)

%description -l pl.UTF-8
Lynx jest przeglądarką WWW działającą w trybie tekstowym. Dobrze
formatuje tekst w HTML, ale nie pozwala na wyświetlanie grafiki.

%description -l pt_BR.UTF-8
Este é um browser WWW para terminal em modo texto. Enquanto ele não
faz nenhuma tentativa para mostrar gráficos, possui um bom suporte
para o formato de texto HTML, formulários e tabelas.

%description -l tr.UTF-8
Metin ekranda çalışan bir WWW tarayıcıdır. Şekil gösteremese de,
formlar ve tablolar için desteği vardır.

%prep
%setup -q -n %{name}2-8-7
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
	--with-screen=ncursesw \
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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lynx.cfg
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lynx.lss
%attr(755,root,root) %{_bindir}/*
%{_datadir}/lynx
%{_desktopdir}/lynx.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/*
%lang(cs) %{_mandir}/cs/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(pl) %{_mandir}/pl/man1/*
