Summary:	Dame lets you play checkers ala point and click
Summary(de):	Spielen Sie Dame
Summary(fr):	Jouez aux dames
Summary(fi):	Tammi peli
Summary(pl):	Warcaby
Name:		dame
Version:	0.27
Release:	3
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	http://super.tacheles.de/~girbal/dame/%{name}-%{version}.tar.gz
Patch0:		%{name}-am_fix.patch
URL:		http://super.tacheles.de/~girbal/dame/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Dame lets you play at draughts in an X window. It comes with checkers,
a tricky opponent, and simplech, an even harder to beat opponent.

%description -l de
Dame zeichnet ein Damebrett in ein X Fenster. Es kommt mit checkers,
einem leichten, und simplech, einem schweren Gegner.

%description -l fr
Dame vous presente un damier graphique pour jouer aux dames contre
l'ordinateur - en personne de checkers ou simplech.

%description -l pl
Dziêki dame mo¿na graæ w warcaby w X Window. W pakiecie jest
szachownica, sprytny przeciwnik oraz simplech -- przeciwnik, którego
jeszcze trudniej pokonaæ.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing acinclude.m4
gettextize --copy --force
libtoolize --copy --force
aclocal -I macros
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	sysdir=%{_applnkdir}/Games/Board

gzip -9nf AUTHORS README ChangeLog dame.lsm

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/dame.6*
%{_pixmapsdir}/*
%{_applnkdir}/Games/Board/dame.desktop
