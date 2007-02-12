Summary:	X11 Window Manager - Amiga Workbench like environment
Summary(pl.UTF-8):	Zarządca okien X11 - środowisko podobne do Workbencha z Amigi
Name:		amiwm
Version:	0.20pl48
Release:	1
License:	LGPL
Group:		X11/Window Managers
Source0:	ftp://ftp.lysator.liu.se/pub/X11/wm/amiwm/%{name}%{version}.tar.gz
# Source0-md5:	bfe907be9e94f6a47fec5181361176f2
URL:		http://www.lysator.liu.se/~marcus/amiwm.html
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
amiwm is an X window manager that tries to make your display look and
feel like an Amiga(R) Workbench(R) screen. It is fully functional and
can do all the usual window manager stuff, like moving and resizing
windows.

The purpose of amiwm is to make life more pleasant for Amiga-freaks
who has/wants to use UNIX workstations once in a while. It can also be
used on the Amiga with the AmiWin X server, although this part needs
some more work. 

%description -l pl.UTF-8
amiwm to zarządca okien X próbujący uczynić ekran wyglądającym i
zachowującym się jak ekran Amiga(R) Workbencha(R). Jest w pełni
funkcjonalny i może wykonywać wszystkie normalne czynności zarządcy
okien, takie jak przesuwanie czy zmiana rozmiaru okienek.

Celem amiwm jest uprzyjemnienie życia fanom Amigi którzy muszą lub
chcą używać czasem stacji uniksowych. Może być używany także na
Amidze z X serwerem AmiWin, choć ta część wymaga jeszcze trochę
pracy.

%prep
%setup -q -n %{name}%{version}

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/xsessions
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.en
%lang(fr) %doc doc/*.fr
%lang(ja) %doc doc/*.ja
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man?/*
%lang(fr) %{_mandir}/fr/man?/*
%lang(ja) %{_mandir}/ja/man?/*
