%define name sunclock
%define version 3.56
%define release %mkrel 4

Summary: The sophisticated clock for the X Window system
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Sciences/Astronomy
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: ftp://ftp.ac-grenoble.fr/ge/geosciences/%{name}-%{version}.tar.bz2
Patch0: sunclock-3.56-fix-str-fmt.patch
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
%setup -q
%patch0 -p0

%build
xmkmf
%make CDEBUGFLAGS="%{optflags}" CXXDEBUGFLAGS="%{optflags}"

%install
make install DESTDIR=$RPM_BUILD_ROOT%{_prefix} BINDIR=/bin MANDIR=/share/man/man1
make install.man DESTDIR=$RPM_BUILD_ROOT%{_prefix} BINDIR=/bin MANDIR=/share/man/man1
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
%{_bindir}/sunclock
%{_mandir}/man1/*
%{_datadir}/icons/sunclock2.xpm
%{_datadir}/applications/mandriva-*.desktop
