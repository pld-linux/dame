Summary:	Dame lets you play checkers ala point and click
Summary(de):	Spielen Sie Dame.
Summary(fr):	Jouez aux dames.
Summary(fi):	Tammi peli
Name:		dame
Version:	0.27
Release:	1
License:	GPL
Group:		X11/Games/Strategy
Group(pl):	X11/Gry/Strategiczne
Source0:	http://super.tacheles.de/~girbal/dame/%{name}-%{version}.tar.gz
Requires:	gnome-libs >= 0.30
URL:		http://super.tacheles.de/~girbal/dame/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Dame lets you play at draughts in an X window. It comes with checkers,
a tricky opponent, and simplech, an even harder to beat opponent.

%description -l pl
Dziêki dame mo¿na graæ w warcaby w X Window. W pakiecie jest
szachownica, sprytny przeciwnik oraz simplech -- przeciwnik, którego
jeszcze trudniej pokonaæ.

%description -l de
Dame zeichnet ein Damebrett in ein X Fenster. Es kommt mit checkers,
einem leichten, und simplech, einem schweren Gegner.

%description -l fr
Dame vous presente un damier graphique pour jouer aux dames contre
l'ordinateur - en personne de checkers ou simplech.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure \
	--prefix=%{_prefix} \
	--bindir=%{bindir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} bindir=$RPM_BUILD_ROOT%{bindir} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README COPYING ChangeLog dame.lsm
%{_prefix}/games/dame
%{_prefix}/games/checkers
%{_prefix}/games/simplech
%{_mandir}/man6/dame.6
%{_datadir}/pixmaps/dame.png
%dir %{_datadir}/pixmaps/dame
%{_datadir}/pixmaps/dame/*.png
%{_datadir}/apps/Games/dame.desktop
%{_datadir}/locale/de/LC_MESSAGES/dame.mo
%{_datadir}/locale/fr/LC_MESSAGES/dame.mo
