Summary:	Dame lets you play checkers ala point and click
Summary(cs.UTF-8):	Plán dáma
Summary(de.UTF-8):	Spielen Sie Dame
Summary(fi.UTF-8):	Tammi peli
Summary(fr.UTF-8):	Jouez aux dames
Summary(it.UTF-8):	Gioco di dama
Summary(pl.UTF-8):	Warcaby
Name:		dame
Version:	0.27
Release:	6
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	http://super.tacheles.de/~girbal/dame/%{name}-%{version}.tar.gz
# Source0-md5:	80b3f49a32a34719e5448fa99086c739
Patch0:		%{name}-am_fix.patch
Patch1:		%{name}-desktop.patch
URL:		http://super.tacheles.de/~girbal/dame/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dame lets you play at draughts in an X window. It comes with checkers,
a tricky opponent, and simplech, an even harder to beat opponent.

%description -l de.UTF-8
Dame zeichnet ein Damebrett in ein X Fenster. Es kommt mit checkers,
einem leichten, und simplech, einem schweren Gegner.

%description -l fr.UTF-8
Dame vous presente un damier graphique pour jouer aux dames contre
l'ordinateur - en personne de checkers ou simplech.

%description -l pl.UTF-8
Dzięki dame można grać w warcaby w X Window. W pakiecie jest
szachownica, sprytny przeciwnik oraz simplech -- przeciwnik, którego
jeszcze trudniej pokonać.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing acinclude.m4
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	sysdir=%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog dame.lsm
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/dame.6*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
