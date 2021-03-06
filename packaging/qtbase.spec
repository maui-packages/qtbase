# Conditional building of X11 related things
%bcond_with X11

# libQtPlatformSupport is not built as a shared library, only as a
# static .a lib-archive. By default the OBS build removes all discovered
# libFOO.a files and as such rpmlint never complains about
# installed-but-unpackaged static libs.
# This flag tells rpmbuild to behave.
%define keepstatic 1

# Pick which OpenGL implementation we need, on ARM it should alwas be
# GLES2 and desktop GL on x86 PCs but the latter breaks qtwayland so we
# temporarily pick GLES2 for x86 too.
#%ifarch %{ix86} x86_64
#%define opengl desktop
#%endif
#%ifarch %{arm}
#%define opengl es2
#%endif
%define opengl es2

# Version is the date of latest commit in qtbase, followed by 'g' + few
# characters of the last git commit ID.
# NOTE: tarball's prefix is 'qt5-base' until version number starts to
# make sense. This allows to update spec contents easily as snapshots
# evolve.

Name:       qtbase
Summary:    Cross-platform application and UI framework
Version:    5.3.2
Release:    1
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.io
Source0:    %{name}-%{version}.tar.xz
Source1:    macros.qt5-default
Source100:  qtbase-rpmlintrc
Patch1:     fix-build-qreal.patch
Patch2:     qtbase-opensource-src-5.3.0-no_xkbcommon-x11.patch
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(freetype2)
%if "%{opengl}" == "desktop"
BuildRequires:  pkgconfig(gl)
%endif
%if "%{opengl}" == "es2"
BuildRequires:  pkgconfig(glesv2)
%endif
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(libsystemd-journal)
BuildRequires:  cups-devel
BuildRequires:  fdupes
BuildRequires:  flex
# Package not available but installed in OBS?
#BuildRequires:  gcc-g++
BuildRequires:  libjpeg-devel
#BuildRequires:  libtiff-devel
BuildRequires:  pam-devel
BuildRequires:  readline-devel
BuildRequires:  sharutils
#BuildRequires:  gdb
BuildRequires:  python
BuildRequires:  pkgconfig(fontconfig)

%if %{with X11}
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xv)
BuildRequires: pkgconfig(xcb-xkb) >= 1.10
# Handle xkbcommon
%global xkbcommon -system-xkbcommon
BuildRequires: pkgconfig(xkbcommon) >= 0.4.1
BuildRequires: pkgconfig(xkbcommon-x11) >= 0.4.1
%endif

BuildRequires:  pkgconfig(gbm)

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.


%package -n qt5-tools
Summary:    Development tools for qtbase
Group:      Qt/Qt
Requires:   qtchooser

%description -n qt5-tools
This package contains useful tools for Qt development


%package -n qt5-qtcore
Summary:    The QtCore library
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig
Requires:   xdg-utils

%description -n qt5-qtcore
This package contains the QtCore library


%package -n qt5-qtcore-devel
Summary:    Development files for QtCore
Group:      Qt/Qt
Requires:   %{name}-qmake
Requires:   %{name}-tools
Requires:   %{name}-qtcore = %{version}-%{release}
Requires:   fontconfig-devel
Requires:   qtchooser

%description -n qt5-qtcore-devel
This package contains the files necessary to develop applications
that use the QtCore


%package -n qt5-qmake
Summary:    QMake
Group:      Qt/Qt
Requires:   qtchooser

%description -n qt5-qmake
This package contains qmake


%package -n qt5-plugin-bearer-connman
Summary:    Connman bearer plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description -n qt5-plugin-bearer-connman
This package contains the connman bearer plugin


%package -n qt5-plugin-bearer-generic
Summary:    Connman generic plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description -n qt5-plugin-bearer-generic
This package contains the connman generic bearer plugin


%package -n qt5-plugin-bearer-nm
Summary:    Connman generic plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description -n qt5-plugin-bearer-nm
This package contains the connman NetworkManager bearer plugin


%package -n qt5-plugin-imageformat-gif
Summary:    Gif image format plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description -n qt5-plugin-imageformat-gif
This package contains the gif imageformat plugin


%package -n qt5-plugin-imageformat-ico
Summary:    Ico image format plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description -n qt5-plugin-imageformat-ico
This package contains the ico imageformat plugin


%package -n qt5-plugin-imageformat-jpeg
Summary:    JPEG image format plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description -n qt5-plugin-imageformat-jpeg
This package contains the JPEG imageformat plugin


%package -n qt5-plugin-platform-minimal
Summary:    Minimal platform plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description -n qt5-plugin-platform-minimal
This package contains the minimal platform plugin


%package -n qt5-plugin-platform-offscreen
Summary:    Offscreen platform plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description -n qt5-plugin-platform-offscreen
This package contains the offscreen platform plugin


%if %{with X11}
%package -n qt5-plugin-platform-inputcontext-compose
Summary:    compose input context platform plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description -n qt5-plugin-platform-inputcontext-compose
This package contains compose platform inputcontext plugin
%endif


%package -n qt5-plugin-platform-eglfs
Summary:    Eglfs platform plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description -n qt5-plugin-platform-eglfs
This package contains the eglfs platform plugin


%package -n qt5-plugin-platform-minimalegl
Summary:    Minimalegl platform plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description -n qt5-plugin-platform-minimalegl
This package contains the minimalegl platform plugin


%if %{with X11}
%package -n qt5-plugin-platform-xcb
Summary:    XCB platform plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description -n qt5-plugin-platform-xcb
This package contains the XCB platform plugin
%endif


%package -n qt5-plugin-platform-linuxfb
Summary:    Linux framebuffer platform plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description -n qt5-plugin-platform-linuxfb
This package contains the linuxfb platform plugin for Qt


%package -n qt5-plugin-platform-kms
Summary:    KMS platform plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description -n qt5-plugin-platform-kms
This package contains the kms platform plugin for Qt


%package -n qt5-plugin-printsupport-cups
Summary:    CUPS print support plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description -n qt5-plugin-printsupport-cups
This package contains the CUPS print support plugin


%package -n qt5-plugin-accessible-widgets
Summary:     Accessible widgets plugin
Group:       Qt/Qt
Requires:    %{name}-qtcore = %{version}-%{release}

%description -n qt5-plugin-accessible-widgets
This package contains the access widgets plugin


%package -n qt5-plugin-sqldriver-sqlite
Summary:    Sqlite sql driver plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description -n qt5-plugin-sqldriver-sqlite
This package contains the sqlite sql driver plugin


%package -n qt5-plugin-platforminputcontext-ibus
Summary:    ibus platform import context plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description -n qt5-plugin-platforminputcontext-ibus
This package contains the ibus platform input context plugin


%package -n qt5-plugin-generic-evdev
Summary:    evdev generic plugin
Group:      Qt/Qt
Requires:   %{name}-qtcore = %{version}-%{release}

%description -n qt5-plugin-generic-evdev
This package contains evdev plugins


%package -n qt5-qtdbus
Summary:    The QtDBus library
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-qtdbus
This package contains the QtDBus library


%package -n qt5-qtdbus-devel
Summary:    Development files for QtDBus
Group:      Qt/Qt
Requires:   %{name}-qtdbus = %{version}-%{release}
Requires:   pkgconfig(dbus-1)

%description -n qt5-qtdbus-devel
This package contains the files necessary to develop
applications that use QtDBus


%package -n qt5-qtgui
Summary:    The QtGui Library
Group:      Qt/Qt
%if "%{desktop}" == "desktop"
Requires:   libGL
%endif
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-qtgui
This package contains the QtGui library


%package -n qt5-qtgui-devel
Summary:    Development files for QtGui
Group:      Qt/Qt
%if "%{desktop}" == "desktop"
Requires:   libGL-devel
%endif
Requires:   %{name}-qtgui = %{version}-%{release}
Requires:   %{name}-qtopengl-devel

%description -n qt5-qtgui-devel
This package contains the files necessary to develop
applications that use QtGui


%package -n qt5-qtnetwork
Summary:    The QtNetwork library
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-qtnetwork
This package contains the QtNetwork library


%package -n qt5-qtnetwork-devel
Summary:    Development files for QtNetwork
Group:      Qt/Qt
Requires:   %{name}-qtnetwork = %{version}-%{release}

%description -n qt5-qtnetwork-devel
This package contains the files necessary to develop
applications that use QtNetwork


%package -n qt5-qtopengl
Summary:    The QtOpenGL library
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-qtopengl
This package contains the QtOpenGL library


%package -n qt5-qtopengl-devel
Summary:    Development files for QtOpenGL
Group:      Qt/Qt
Requires:   %{name}-qtopengl = %{version}-%{release}
Requires:   libGLESv2-devel
Requires:   libEGL-devel

%description -n qt5-qtopengl-devel
This package contains the files necessary to develop
applications that use QtOpenGL


%package -n qt5-qtsql
Summary:    The QtSql library
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-qtsql
This package contains the QtSql library


%package -n qt5-qtsql-devel
Summary:    Development files for QtSql
Group:      Qt/Qt
Requires:   %{name}-qtsql = %{version}-%{release}

%description -n qt5-qtsql-devel
This package contains the files necessary to develop
applications that use QtSql


%package -n qt5-qttest
Summary:    The QtTest library
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-qttest
This package contains the QtTest library


%package -n qt5-qttest-devel
Summary:    Development files for QtTest
Group:      Qt/Qt
Requires:   %{name}-qttest = %{version}-%{release}

%description -n qt5-qttest-devel
This package contains the files necessary to develop
applications that use QtTest


%package -n qt5-qtxml
Summary:    The QtXml library
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-qtxml
This package contains the QtXml library


%package -n qt5-qtxml-devel
Summary:    Development files for QtXml
Group:      Qt/Qt
Requires:   %{name}-qtxml = %{version}-%{release}

%description -n qt5-qtxml-devel
This package contains the files necessary to develop
applications that use QtXml


%package -n qt5-qtwidgets
Summary:    The QtWidgets library
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-qtwidgets
This package contains the QtWidgets library


%package -n qt5-qtwidgets-devel
Summary:    Development files for QtWidgets
Group:      Qt/Qt
Requires:   %{name}-qtwidgets = %{version}-%{release}
Requires:   qt5-plugin-accessible-widgets = %{version}-%{release}

%description -n qt5-qtwidgets-devel
This package contains the files necessary to develop
applications that use QtWidgets


%package -n qt5-qtplatformsupport-devel
Summary:    Development files for QtPlatformSupport
Group:      Qt/Qt

%description -n qt5-qtplatformsupport-devel
This package contains the files necessary to develop
applications that use QtPlatformSupport


%package -n qt5-qtbootstrap-devel
Summary:    Development files for QtBootstrap
Group:      Qt/Qt

%description -n qt5-qtbootstrap-devel
This package contains the files necessary to develop
applications that use QtBootstrap


%package -n qt5-qtprintsupport
Summary:    The QtPrintSupport
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-qtprintsupport
This package contains the QtPrintSupport library


%package -n qt5-qtprintsupport-devel
Summary:    Development files for QtPrintSupport
Group:      Qt/Qt
Requires:   %{name}-qtprintsupport = %{version}-%{release}

%description -n qt5-qtprintsupport-devel
This package contains the files necessary to develop
applications that use QtPrintSupport


%package -n qt5-qtconcurrent
Summary:    QtConcurrent library
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-qtconcurrent
This package contains the QtConcurrent library


%package -n qt5-qtconcurrent-devel
Summary:    Development files for QtConcurrent
Group:      Qt/Qt
Requires:   %{name}-qtconcurrent = %{version}-%{release}

%description -n qt5-qtconcurrent-devel
This package contains the files necessary to develop
applications that use QtConcurrent


%package -n qt5-default
Summary:    Qt5 development defaults packafge
Group:      Development/Libraries
Requires:   qtchooser
Provides:   qt-default
Conflicts:   qt4-default

%description -n qt5-default
Qt is a cross-platform application and UI framework. Using Qt, you can write
web-enabled applications once and deploy them across desktop, mobile and
embedded operating systems without rewriting the source code.

This package contains the Qt5 development defaults package


%prep
%setup -q -n %{name}-%{version}/upstream

%patch1 -p1 -b .fixqreal

%if 0%{?no_xkbcommon_x11}
%patch2 -p1 -b .xkbcommon
%endif

%build
touch .git

MAKEFLAGS=%{?_smp_mflags} \
./configure --disable-static \
    -confirm-license \
%if ! 0%{?qt5_release_build}
    -developer-build \
    -no-warnings-are-errors \
%endif
    -platform linux-g++ \
    -prefix "%{_prefix}" \
    -bindir "%{_libdir}/qt5/bin" \
    -libdir "%{_libdir}" \
    -docdir "%{_docdir}/qt5/" \
    -headerdir "%{_includedir}/qt5" \
    -datadir "%{_datadir}/qt5" \
    -plugindir "%{_libdir}/qt5/plugins" \
    -importdir "%{_libdir}/qt5/imports" \
    -translationdir "%{_datadir}/qt5/translations" \
    -sysconfdir "%{_sysconfdir}/xdg" \
    -examplesdir "%{_libdir}/qt5/examples" \
    -archdatadir "%{_datadir}/qt5" \
    -testsdir "%{_libdir}/qt5/tests" \
    -qmldir "%{_libdir}/qt5/qml" \
    -libexecdir "%{_libdir}/qt5/libexec" \
    -opensource \
    -no-sql-ibase \
    -no-sql-mysql \
    -no-sql-odbc \
    -no-sql-psql \
    -plugin-sql-sqlite \
    -no-sql-sqlite2 \
    -no-sql-tds \
    -system-sqlite \
    -audio-backend \
    -system-zlib \
    -system-libpng \
    -system-libjpeg \
    %{?xkbcommon} \
    -no-rpath \
    -optimized-qmake \
    -dbus-linked \
    -no-strip \
    -no-separate-debug-info \
%ifarch %{ix86} x86_64
    -reduce-relocations \
%endif
    -verbose \
    -no-gtkstyle \
    -opengl %{opengl} \
    -no-openvg \
    -openssl-linked \
    -lfontconfig \
    -I/usr/include/freetype2 \
    -nomake tests \
    -nomake examples \
%if %{with X11}
    -xcb \
%else
    -no-xcb \
%endif
    -no-xinput2 \
    -kms \
%ifnarch %{ix86} x86_64
    -qreal float \
%endif
    -journald

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install

# We don't need qt5/Qt/
rm -rf %{buildroot}/%{_includedir}/qt5/Qt

# Fix wrong path in pkgconfig files
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
    -exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
    -exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;

# these manage to really royally screw up cmake
find %{buildroot}%{_libdir} -type f -name "*_*Plugin.cmake" \
    -exec rm {} \;

find %{buildroot}%{_docdir}/qt5/ -type f -exec chmod ugo-x {} \;

# Make sure these are around
mkdir -p %{buildroot}%{_includedir}/qt5/
mkdir -p %{buildroot}%{_datadir}/qt5/
mkdir -p %{buildroot}%{_libdir}/qt5/plugins/
mkdir -p %{buildroot}%{_libdir}/qt5/imports/
mkdir -p %{buildroot}%{_libdir}/qt5/translations/
mkdir -p %{buildroot}%{_libdir}/qt5/examples/

# Install qmake rpm macros
install -D -p -m 0644 %{_sourcedir}/macros.qt5-default \
%{buildroot}/%{_sysconfdir}/rpm/macros.qt5-default

# Add a configuration link for qtchooser - the 5.conf is installed by qtchooser
mkdir -p %{buildroot}/etc/xdg/qtchooser
ln -s %{_sysconfdir}/xdg/qtchooser/5.conf %{buildroot}%{_sysconfdir}/xdg/qtchooser/default.conf

%fdupes %{buildroot}/%{_libdir}
%fdupes %{buildroot}/%{_includedir}
%fdupes %{buildroot}/%{_datadir}


%post -n qt5-qtcore -p /sbin/ldconfig
%postun -n qt5-qtcore -p /sbin/ldconfig

%post -n qt5-qtdbus -p /sbin/ldconfig
%postun -n qt5-qtdbus -p /sbin/ldconfig

%post -n qt5-qtsql -p /sbin/ldconfig
%postun -n qt5-qtsql -p /sbin/ldconfig

%post -n qt5-qtnetwork -p /sbin/ldconfig
%postun -n qt5-qtnetwork -p /sbin/ldconfig

%post -n qt5-qtgui -p /sbin/ldconfig
%postun -n qt5-qtgui -p /sbin/ldconfig

%post -n qt5-qttest -p /sbin/ldconfig
%postun -n qt5-qttest -p /sbin/ldconfig

%post -n qt5-qtopengl -p /sbin/ldconfig
%postun -n qt5-qtopengl -p /sbin/ldconfig

%post -n qt5-qtxml -p /sbin/ldconfig
%postun -n qt5-qtxml -p /sbin/ldconfig

%post -n qt5-qtprintsupport -p /sbin/ldconfig
%postun -n qt5-qtprintsupport -p /sbin/ldconfig

%post -n qt5-qtwidgets -p /sbin/ldconfig
%postun -n qt5-qtwidgets -p /sbin/ldconfig

%post -n qt5-qtconcurrent -p /sbin/ldconfig
%postun -n qt5-qtconcurrent -p /sbin/ldconfig


%files -n qt5-tools
%defattr(-,root,root,-)
%{_libdir}/qt5/bin/moc
%{_libdir}/qt5/bin/rcc
%{_libdir}/qt5/bin/syncqt.pl
%{_libdir}/qt5/bin/uic
%{_libdir}/qt5/bin/qdoc
%{_libdir}/qt5/bin/qlalr
%{_docdir}/qt5/*

%files -n qt5-qtcore
%defattr(-,root,root,-)
%dir %{_includedir}/qt5/
%dir %{_datadir}/qt5/
%dir %{_libdir}/qt5/plugins/
%dir %{_libdir}/qt5/imports/
%dir %{_libdir}/qt5/translations/
%dir %{_libdir}/qt5/examples/
%{_libdir}/libQt5Core.so.*

%files -n qt5-qtcore-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtCore/
%{_libdir}/libQt5Core.prl
%{_libdir}/libQt5Core.so
%{_libdir}/pkgconfig/Qt5Core.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_core.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_core_private.pri
%{_libdir}/cmake/

%files -n qt5-qmake
%defattr(-,root,root,-)
%{_libdir}/qt5/bin/qmake
%{_datadir}/qt5/mkspecs/aix-*/
%{_datadir}/qt5/mkspecs/blackberry*/
%{_datadir}/qt5/mkspecs/common/
%{_datadir}/qt5/mkspecs/cygwin-*/
%{_datadir}/qt5/mkspecs/darwin-*/
%{_datadir}/qt5/mkspecs/features/
%{_datadir}/qt5/mkspecs/freebsd-*/
%{_datadir}/qt5/mkspecs/hpux-*
%{_datadir}/qt5/mkspecs/hpuxi-*
%{_datadir}/qt5/mkspecs/hurd-g++/
%{_datadir}/qt5/mkspecs/irix-*/
%{_datadir}/qt5/mkspecs/linux-*/
%{_datadir}/qt5/mkspecs/lynxos-*/
%{_datadir}/qt5/mkspecs/macx-*/
%{_datadir}/qt5/mkspecs/netbsd-*/
%{_datadir}/qt5/mkspecs/openbsd-*/
%{_datadir}/qt5/mkspecs/qconfig.pri
%{_datadir}/qt5/mkspecs/qmodule.pri
%{_datadir}/qt5/mkspecs/qnx*/
%{_datadir}/qt5/mkspecs/sco-*/
%{_datadir}/qt5/mkspecs/solaris-*/
%{_datadir}/qt5/mkspecs/tru64-*/
%{_datadir}/qt5/mkspecs/unixware-*/
%{_datadir}/qt5/mkspecs/unsupported/
%{_datadir}/qt5/mkspecs/win32-g++/
%{_datadir}/qt5/mkspecs/win32-icc/
%{_datadir}/qt5/mkspecs/win32-msvc20*/
%{_datadir}/qt5/mkspecs/wince*/
%{_datadir}/qt5/mkspecs/winphone*/
%{_datadir}/qt5/mkspecs/winrt*/
%{_datadir}/qt5/mkspecs/devices/
%{_datadir}/qt5/mkspecs/qdevice.pri
%{_datadir}/qt5/mkspecs/qfeatures.pri
%config(noreplace) %{_sysconfdir}/rpm/macros.qt5-default

%files -n qt5-qtdbus
%defattr(-,root,root,-)
%{_libdir}/libQt5DBus.so.*

%files -n qt5-qtdbus-devel
%defattr(-,root,root,-)
%{_libdir}/qt5/bin/qdbuscpp2xml
%{_libdir}/qt5/bin/qdbusxml2cpp
%{_includedir}/qt5/QtDBus/
%{_libdir}/libQt5DBus.so
%{_libdir}/libQt5DBus.prl
%{_libdir}/pkgconfig/Qt5DBus.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_dbus.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_dbus_private.pri

%files -n qt5-qtgui
%defattr(-,root,root,-)
%{_libdir}/libQt5Gui.so.*

%files -n qt5-qtgui-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtGui/
%{_libdir}/libQt5Gui.prl
%{_libdir}/libQt5Gui.so
%{_libdir}/pkgconfig/Qt5Gui.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_gui.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_gui_private.pri

%files -n qt5-qtnetwork
%defattr(-,root,root,-)
%{_libdir}/libQt5Network.so.*

%files -n qt5-qtnetwork-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtNetwork/
%{_libdir}/libQt5Network.prl
%{_libdir}/libQt5Network.so
%{_libdir}/pkgconfig/Qt5Network.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_network.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_network_private.pri

%files -n qt5-qtopengl
%defattr(-,root,root,-)
%{_libdir}/libQt5OpenGL.so.*

%files -n qt5-qtopengl-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtOpenGL/
%{_includedir}/qt5/QtOpenGLExtensions/
%{_libdir}/libQt5OpenGL.prl
%{_libdir}/libQt5OpenGLExtensions.prl
%{_libdir}/libQt5OpenGL.so
%{_libdir}/libQt5OpenGLExtensions.a
%{_libdir}/pkgconfig/Qt5OpenGL.pc
%{_libdir}/pkgconfig/Qt5OpenGLExtensions.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_opengl.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_opengl_private.pri
%{_datadir}/qt5/mkspecs/android-g++/qmake.conf
%{_datadir}/qt5/mkspecs/android-g++/qplatformdefs.h
%{_datadir}/qt5/mkspecs/modules/qt_lib_openglextensions.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_openglextensions_private.pri

%files -n qt5-qtsql
%defattr(-,root,root,-)
%{_libdir}/libQt5Sql.so.*

%files -n qt5-qtsql-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtSql/
%{_libdir}/libQt5Sql.prl
%{_libdir}/libQt5Sql.so
%{_libdir}/pkgconfig/Qt5Sql.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_sql.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_sql_private.pri

%files -n qt5-qttest
%defattr(-,root,root,-)
%{_libdir}/libQt5Test.so.*

%files -n qt5-qttest-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtTest/
%{_libdir}/libQt5Test.prl
%{_libdir}/libQt5Test.so
%{_libdir}/pkgconfig/Qt5Test.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_testlib.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_testlib_private.pri

%files -n qt5-qtxml
%defattr(-,root,root,-)
%{_libdir}/libQt5Xml.so.*

%files -n qt5-qtxml-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtXml/
%{_libdir}/libQt5Xml.prl
%{_libdir}/libQt5Xml.so
%{_libdir}/pkgconfig/Qt5Xml.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_xml.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_xml_private.pri

%files -n qt5-qtwidgets
%defattr(-,root,root,-)
%{_libdir}/libQt5Widgets.so.*

%files -n qt5-qtwidgets-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtWidgets/
%{_libdir}/libQt5Widgets.prl
%{_libdir}/libQt5Widgets.so
%{_libdir}/pkgconfig/Qt5Widgets.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_widgets.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_widgets_private.pri

%files -n qt5-qtplatformsupport-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtPlatformSupport/
%{_libdir}/libQt5PlatformSupport.prl
%{_libdir}/libQt5PlatformSupport.a
%{_libdir}/pkgconfig/Qt5PlatformSupport.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_platformsupport_private.pri

%files -n qt5-qtbootstrap-devel
%defattr(-,root,root,-)
%{_libdir}/libQt5Bootstrap.prl
%{_libdir}/libQt5Bootstrap.a
%{_libdir}/pkgconfig/Qt5Bootstrap.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_bootstrap_private.pri

%files -n qt5-qtprintsupport
%defattr(-,root,root,-)
%{_libdir}/libQt5PrintSupport.so.*

%files -n qt5-qtprintsupport-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtPrintSupport/
%{_libdir}/libQt5PrintSupport.prl
%{_libdir}/libQt5PrintSupport.so
%{_libdir}/pkgconfig/Qt5PrintSupport.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_printsupport.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_printsupport_private.pri

%files -n qt5-qtconcurrent
%defattr(-,root,root,-)
%{_libdir}/libQt5Concurrent.so.*

%files -n qt5-qtconcurrent-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtConcurrent/
%{_libdir}/libQt5Concurrent.prl
%{_libdir}/libQt5Concurrent.so
%{_libdir}/pkgconfig/Qt5Concurrent.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_concurrent.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_concurrent_private.pri

%files -n qt5-plugin-bearer-connman
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/bearer/libqconnmanbearer.so

%files -n qt5-plugin-bearer-generic
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/bearer/libqgenericbearer.so

%files -n qt5-plugin-bearer-nm
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/bearer/libqnmbearer.so

%files -n qt5-plugin-imageformat-gif
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqgif.so

%files -n qt5-plugin-imageformat-ico
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqico.so

%files -n qt5-plugin-imageformat-jpeg
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqjpeg.so

%files -n qt5-plugin-platform-minimal
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqminimal.so

%files -n qt5-plugin-platform-offscreen
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqoffscreen.so

%if %{with X11}
%files -n qt5-plugin-platform-inputcontext-compose
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforminputcontexts/libcomposeplatforminputcontextplugin.so
%endif

%files -n qt5-plugin-platform-eglfs
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqeglfs.so

%files -n qt5-plugin-platform-minimalegl
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqminimalegl.so

%if %{with X11}
%files -n qt5-plugin-platform-xcb
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqxcb.so
%endif

%files -n qt5-plugin-platform-linuxfb
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqlinuxfb.so

%files -n qt5-plugin-platform-kms
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqkms.so

%files -n qt5-plugin-printsupport-cups
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/printsupport/libcupsprintersupport.so

%files -n qt5-plugin-accessible-widgets
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/accessible/libqtaccessiblewidgets.so

%files -n qt5-plugin-sqldriver-sqlite
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/sqldrivers/libqsqlite.so

%files -n qt5-plugin-platforminputcontext-ibus
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforminputcontexts/libibusplatforminputcontextplugin.so

%files -n qt5-plugin-generic-evdev
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/generic/libqevdev*plugin.so

%files -n qt5-default
%defattr(-,root,root,-)
%{_sysconfdir}/xdg/qtchooser/default.conf
