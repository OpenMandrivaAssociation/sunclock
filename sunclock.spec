%define name sunclock
%define version 3.56
%define release %mkrel 3

Summary: The sophisticated clock for the X Window system
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Sciences/Astronomy
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: ftp://ftp.ac-grenoble.fr/ge/geosciences/%{name}-%{version}.tar.bz2
URL: http://freshmeat.net/projects/sunclock/
BuildRequires: imake X11-devel jpeg-devel png-devel
Conflicts:   xrmap

%description
Sunclock displays a map of the Earth and shows which portion is illuminated
by the sun. It can commute between two states, the "clock window" and
the "map window". The clock window displays a small map of the Earth
and therefore occupies little space on the screen, while the "map window" 
displays a large map and offers more advanced functions. 

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
xmkmf
%make CDEBUGFLAGS="$RPM_OPT_FLAGS" CXXDEBUGFLAGS="$RPM_OPT_FLAGS"

# %install
make install DESTDIR=$RPM_BUILD_ROOT%{_prefix}
make install.man DESTDIR=$RPM_BUILD_ROOT%{_prefix}
mkdir -p $RPM_BUILD_ROOT/usr/share/icons
install wm_icons/sunclock2.xpm -m 644 $RPM_BUILD_ROOT/usr/share/icons/sunclock2.xpm

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Categories=Amusement;
Name=Sunclock
Comment=Sophisticated clock for the X Window system
Exec=%{name}
Icon=toys_section
EOF

mkdir -p $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/X11/doc/html/
#mv $RPM_BUILD_ROOT%{_prefix}/usr/X11R6/lib/X11/doc/html/* $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/X11/doc/html/.

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc CHANGES coordinates.txt COPYING INSTALL README TODO VMF.txt
%{_datadir}/%name
%{_prefix}/X11R6/bin/sunclock
%{_prefix}/X11R6/man/man1/*
%{_datadir}/icons/sunclock2.xpm
%{_datadir}/applications/mandriva-*.desktop
