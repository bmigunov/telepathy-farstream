Name:           telepathy-farstream
Version:        0.6.2
Release:        1
Summary:        Telepathy client library to handle Call channels
License:        LGPLv2+
URL:            http://www.freedesktop.org/wiki/Software/Farstream
Source0:        %{name}-%{version}.tar.gz
Patch0:         disable-gtkdoc.patch
BuildRequires:  pkgconfig(telepathy-glib)
BuildRequires:  pkgconfig(farstream-0.2)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

Obsoletes: telepathy-farsight

%description
Telepathy client libraries for video conferencing applications

%package        devel
Summary:        Development files for telepathy based video conferencing applications
Requires:       %{name} = %{version}-%{release}
Obsoletes:      telepathy-farsight-devel

%description    devel
Telepathy client libraries for video conferencing applications

%prep
%autosetup -p1 -n %{name}-%{version}/telepathy-farstream

%build
%autogen --disable-python --enable-static=no --disable-gtk-doc --disable-introspection
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%doc NEWS README
%{_libdir}/libtelepathy-farstream*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libtelepathy-farstream.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/telepathy-1.0/%{name}/
