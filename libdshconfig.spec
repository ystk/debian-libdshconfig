Summary: 	Library for parsing dsh-style configuration files
Name: 		libdshconfig
Version: 	0.20.12
Release: 	2%{?disttag}
License: 	GPL
Group: 		System Environment/Libraries
URL: 		http://www.netfort.gr.jp/~dancer/software/dsh.html.en
Source0: 	http://www.netfort.gr.jp/~dancer/software/downloads/%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)

%package devel
Summary:	Development files for libdshconfig
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

# -----------------------------------------------------------------------------

%description
Library for parsing dsh-style configuration files. Required by dsh and
other applications.

%description devel
Development files for libdshconfig

Library for parsing dsh-style configuration files. Required by dsh and
other applications.

# -----------------------------------------------------------------------------

%prep
%setup -q

# -----------------------------------------------------------------------------

%build
%configure
make %{?_smp_mflags}

# -----------------------------------------------------------------------------

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -Rf $RPM_BUILD_ROOT%{_libdir}/*.la

# -----------------------------------------------------------------------------

%clean
rm -rf $RPM_BUILD_ROOT

# -----------------------------------------------------------------------------

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS ChangeLog NEWS README
%{_libdir}/libdshconfig.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/libdshconfig.h
%{_libdir}/libdshconfig.a
%{_libdir}/libdshconfig.so

# -----------------------------------------------------------------------------

%changelog
* Tue Feb 14 2006 Dams <anvil[AT]livna.org> - 0.20.12-1
- Updated to 0.20.12

* Wed Jan 26 2005 Dams <anvil[AT]livna.org> 0.20.11-1
- Updated to 0.20.11

* Thu Jun  3 2004 Dams <anvil[AT]livna.org> 
- Initial build.
