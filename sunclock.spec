%define name sunclock
%define version 3.54.1
%define release %mkrel 2

Summary: The sophisticated clock for the X Window system
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Sciences/Astronomy
Source: ftp://ftp.ac-grenoble.fr/ge/geosciences/%{name}-%{version}.tar.bz2
URL: http://freshmeat.net/projects/sunclock/
BuildRequires: imake
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
if [ -f $RPM_BUILD_ROOT%{_prefix}/X11R6/man/man1/sunclock.1x ]; then
find $RPM_BUILD_ROOT%{_prefix}/X11R6/man/man1/sunclock.1x -type f -exec bzip2 -9f {} \;
fi
mkdir -p $RPM_BUILD_ROOT/usr/share/icons
install wm_icons/sunclock2.xpm -m 644 $RPM_BUILD_ROOT/usr/share/icons/sunclock2.xpm

install -d $RPM_BUILD_ROOT%{_menudir}
cat <<EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): \
        needs="X11" \
        section="Amusement/Toys" \
        title="Sunclock" \
        longtitle="Sophisticated clock for the X Window system" \
        command="%{name}" \
        icon="toys_section.png"
EOF

mkdir -p $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/X11/doc/html/
#mv $RPM_BUILD_ROOT%{_prefix}/usr/X11R6/lib/X11/doc/html/* $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/X11/doc/html/.

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc CHANGES coordinates.txt COPYING INSTALL README TODO VMF.txt 
%{_datadir}/sunclock/Sunclockrc
%{_datadir}/sunclock/earthmaps/vmf/*
%{_datadir}/sunclock/i18n/*
%{_datadir}/editkit/README
%{_datadir}/editkit/emxrc
%{_datadir}/editkit/rc.common
%{_prefix}/X11R6/bin/emx
%{_prefix}/X11R6/bin/sunclock
%{_prefix}/X11R6/man/man1/sunclock.1*
%{_prefix}/X11R6/man/man1/emx.1x
%{_prefix}/X11R6/lib/X11/doc/html/*
%{_datadir}/icons/sunclock2.xpm
%_menudir/*


