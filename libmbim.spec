Summary:	GLib library for talking to WWAN modems and devices using MBIM protocol
Name:		libmbim
Version:	1.8.0
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://www.freedesktop.org/software/libmbim/%{name}-%{version}.tar.xz
# Source0-md5:	530826b6f5129b997d9f107892afc200
URL:		http://www.freedesktop.org/wiki/Software/libmbim
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	udev-glib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmbim is a GLib library for talking to WWAN modems and devices which
speak the Mobile Interface Broadband Model (MBIM) protocol.

%package devel
Summary:	Header files for libmbim library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libmbim library.

%package apidocs
Summary:	libmbim API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
API documentation for libmbim library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/mbim-network
%attr(755,root,root) %{_bindir}/mbimcli
%attr(755,root,root) %ghost %{_libdir}/libmbim-glib.so.0
%attr(755,root,root) %{_libdir}/libmbim-glib.so.*.*.*
%{_mandir}/man1/mbim-network.1*
%{_mandir}/man1/mbimcli.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmbim-glib.so
%{_includedir}/libmbim-glib
%{_pkgconfigdir}/mbim-glib.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libmbim-glib

