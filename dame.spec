Summary:	Dame lets you play checkers ala point and click
Summary(de):	Spielen Sie Dame.
Summary(fr):	Jouez aux dames.
Summary(fi):	Tammi peli
Name:		dame
Version:	0.27
Release:	1
Copyright:	GPL
Group:		X11/Games/Strategy
Source:		http://super.tacheles.de/~girbal/dame/dame-%{ver}.tar.gz
Requires:	gnome-libs >= 0.30
URL:		http://super.tacheles.de/~girbal/dame/
BuildRoot:	/var/tmp/dame-root

%description
Dame lets you play at draughts in an X window. It comes with checkers, a
tricky opponent, and simplech, an even harder to beat opponent.

%description -l de
Dame zeichnet ein Damebrett in ein X Fenster. Es kommt mit checkers, einem
leichten, und simplech, einem schweren Gegner.

%description -l fr
Dame vous presente un damier graphique pour jouer aux dames contre
l'ordinateur - en personne de checkers ou simplech.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure \
	--prefix=%{prefix} \
	--bindir=%{bindir}
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{prefix} bindir=$RPM_BUILD_ROOT%{bindir} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README COPYING ChangeLog dame.lsm
%{prefix}/games/dame
%{prefix}/games/checkers
%{prefix}/games/simplech
%{prefix}/man/man6/dame.6
%{prefix}/share/pixmaps/dame.png
%dir %{prefix}/share/pixmaps/dame
%{prefix}/share/pixmaps/dame/*.png
%{prefix}/share/apps/Games/dame.desktop
%{prefix}/share/locale/de/LC_MESSAGES/dame.mo
%{prefix}/share/locale/fr/LC_MESSAGES/dame.mo
