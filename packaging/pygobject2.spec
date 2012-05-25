%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

# Last updated for version 2.19.0
%define glib2_version           2.16.0
%define python2_version         2.3.5

### Abstract ###

Name: pygobject2
Version: 2.21.3
Release: 1.1
License: LGPLv2+
Group: Development/Languages
Summary: Python bindings for GObject
URL: http://www.pygtk.org/
Source: http://ftp.gnome.org/pub/GNOME/sources/pygobject/2.21/pygobject-%{version}.tar.gz
Source101: %{name}-rpmlintrc


### Build Dependencies ###

BuildRequires: automake
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: libtool
BuildRequires: python-devel >= %{python2_version}

%description
The %{name} package provides a convenient wrapper for the GObject library
for use in Python programs.

%package codegen
Summary: The code generation program for PyGObject
Group: Development/Languages

%description codegen
The package contains the C code generation program for PyGObject.

%package devel
Summary: Development files for building add-on libraries
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: %{name}-codegen = %{version}-%{release}
Requires: %{name}-doc = %{version}-%{release}
Requires: glib2-devel
Requires: pkgconfig

%description devel
This package contains files required to build wrappers for %{name}-based
libraries such as pygtk2.

%package doc
Summary: Documentation files for %{name}
Group: Development/Languages

%description doc
This package contains documentation files for %{name}.

%prep
%setup -q -n pygobject-%{version}

%build
%configure --enable-thread
export tagname=CC
make LIBTOOL=/usr/bin/libtool

%install
rm -rf $RPM_BUILD_ROOT
export tagname=CC
make LIBTOOL=/usr/bin/libtool DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name '*.la' -or -name '*.a' | xargs rm -f

rm examples/Makefile*

%clean
rm -fr $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%doc AUTHORS NEWS README

%{_libdir}/libpyglib-2.0-python.so*
%dir %{python_sitearch}/gtk-2.0
%{python_sitearch}/gtk-2.0/dsextras.*
%{python_sitearch}/pygtk.*

%defattr(755, root, root, 755)
%{python_sitearch}/gtk-2.0/gio
#%{python_sitearch}/gtk-2.0/girepository
%{python_sitearch}/gtk-2.0/glib
%{python_sitearch}/gtk-2.0/gobject

%files codegen
%defattr(755, root, root, 755)
%{_bindir}/pygobject-codegen-2.0
%defattr(644, root, root, 755)
%dir %{_datadir}/pygobject/2.0
%{_datadir}/pygobject/2.0/codegen

%files devel
%defattr(644, root, root, 755)
%dir %{_datadir}/pygobject
%dir %{_includedir}/pygtk-2.0
%{_datadir}/pygobject/2.0/defs
#%{_includedir}/pygobject/bank.h
%{_includedir}/pygtk-2.0/pyglib.h
%{_includedir}/pygtk-2.0/pygobject.h
%{_libdir}/pkgconfig/pygobject-2.0.pc

%files doc
%defattr(644, root, root, 755)
%doc examples
%{_datadir}/gtk-doc/html/pygobject
%{_datadir}/pygobject/xsl

%changelog
* Tue Dec  7 2010 Damien Lespiau <damien.lespiau@intel.com> - 2.21.3
- Update to 2.21.3 (needed for pyclutter 1.3.2) (BMC#11291)
* Sat Apr 10 2010 Anas Nashif <anas.nashif@intel.com> - 2.21.1
- Fixed rpmlint errors
* Sun Mar 14 2010 Anas Nashif <anas.nashif@intel.com> - 2.21.1
- Fixed file list
* Thu Mar 11 2010 Zhang Qiang <qiang.z.zhang@intel.com> 2.21.1
- Update to 2.21
* Thu Sep 24 2009 Zhang Qiang <qiang.z.zhang@intel.com> 2.20
- Update to 2.20
* Tue Sep  1 2009 Xu Li <xu.li@intel.com> 2.19.0
- Upgraded to 2.19.0
- Fixed the file list
* Fri Mar 20 2009 Anas Nashif <anas.nashif@intel.com> 2.16.1
- Fixed dependencies and file list
* Mon Mar  2 2009 Zhu Yanhai <yanhai.zhu@intel.com> 2.16.1
- Update to 2.16.1
- Remove a unused patch
- Fix .spec to silent rpmlint
* Fri Feb 20 2009 Zhu Yanhai <yanhai.zhu@intel.com> 2.16.0
- Update to 2.16.0
- Correct the URL in spec file
* Sat Sep 20 2008 Anas Nashif <anas.nashif@intel.com> 2.15.4
- initial import into moblin
* Wed Sep  3 2008 Matthew Barnes <mbarnes@redhat.com> - 2.15.4-1.fc10
- Update to 2.15.4
* Sun Aug 31 2008 Matthew Barnes <mbarnes@redhat.com> - 2.15.3-1.fc10
- Update to 2.15.3
* Tue Aug 12 2008 Matthew Barnes <mbarnes@redhat.com> - 2.15.2-3.fc10
- Modify thread initialization patch to fix RH bug #458522.
* Thu Aug  7 2008 Matthew Barnes <mbarnes@redhat.com> - 2.15.2-2.fc10
- Add patch for RH bug #544946 (error on gtk.gdk.threads_init).
* Sat Jul 26 2008 Matthew Barnes <mbarnes@redhat.com> - 2.15.2-1.fc10
- Update to 2.15.2
* Sun Jul 20 2008 Matthew Barnes <mbarnes@redhat.com> - 2.15.1-2.fc10
- Fix directory ownership.  (RH bug #455974, patch by Robert Scheck).
* Wed Jul 16 2008 Matthew Barnes <mbarnes@redhat.com> - 2.15.1-1.fc10
- Update to 2.15.1
- Bump glib2_version to 2.16.0.
- Remove ancient automake_version.
- Add a pygobject2-codegen subpackage.
* Fri May 23 2008 Matthew Barnes <mbarnes@redhat.com> - 2.14.2-1.fc10
- Update to 2.14.2
* Sun Feb 17 2008 Matthew Barnes <mbarnes@redhat.com> - 2.14.1-2.fc9
- Rebuild with GCC 4.3
* Thu Jan  3 2008 Matthew Barnes <mbarnes@redhat.com> - 2.14.1-1.fc9
- Update to 2.14.1
* Fri Oct 26 2007 Matthew Barnes <mbarnes@redhat.com> - 2.14.0-2.fc9
- Remove redundant requirements.
- Use name tag where appropriate.
* Sun Sep 16 2007 Matthew Barnes <mbarnes@redhat.com> - 2.14.0-1.fc8
- Update to 2.14.0
  * Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 2.13.2-3
- Rebuild for selinux ppc32 issue.
* Wed Aug  8 2007 Matthias Clasen <mclasen@redhat.com> - 2.13.2-2
- Update the license field
* Sat Jul  7 2007 Matthew Barnes <mbarnes@redhat.com> - 2.13.2-1.fc8
- Update to 2.13.2
* Fri May 18 2007 Matthew Barnes <mbarnes@redhat.com> - 2.13.1-1.fc8
- Update to 2.13.1
- Remove patch for RH bug #237179 (fixed upstream).
* Thu May  3 2007 Matthew Barnes <mbarnes@redhat.com> - 2.12.3-5.fc7
- Fix devel subpackage dependency (RH bug #238793).
* Thu Apr 19 2007 Matthew Barnes <mbarnes@redhat.com> - 2.12.3-3.fc7
- Add patch for RH bug #237179 (memory leak).
* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 2.12.3-2
- rebuild against python 2.5
* Sat Nov 18 2006 Matthew Barnes <mbarnes@redhat.com> - 2.12.3-1.fc7
- Update to 2.12.3
* Thu Oct 26 2006 Matthew Barnes <mbarnes@redhat.com> - 2.12.2-3.fc7
- Add subpackage pygobject2-doc (bug #205231).
* Tue Oct 24 2006 Matthew Barnes <mbarnes@redhat.com> - 2.12.2-2.fc7
- Use python_sitearch instead of python_sitelib.
* Sun Oct 15 2006 Matthew Barnes <mbarnes@redhat.com> - 2.12.2-1.fc7
- Update to 2.12.2
* Sun Sep 24 2006 Matthew Barnes <mbarnes@redhat.com> - 2.12.1-3.fc6
- Require glib2-devel for the -devel package.
* Fri Sep 22 2006 Matthew Barnes <mbarnes@redhat.com> - 2.12.1-2.fc6
- Define a python_sitelib macro for files under site_packages.
- Spec file cleanups.
* Tue Sep  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.12.1-1.fc6
- Update to 2.12.1
- Require pkgconfig for the -devel package
* Sun Aug 27 2006 Matthias Clasen <mclasen@redhat.com> - 2.11.4-1.fc6
- Update to 2.11.4
- Use pre-built docs
* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.11.3-1.fc6
- Update to 2.11.3
* Sun Aug 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.11.2-2.fc6
- BR libxslt
* Sun Aug 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.11.2-1.fc6
- Update to 2.11.2
* Wed Jul 19 2006 Jesse Keating <jkeating@redhat.com> - 2.11.0-2
- rebuild
* Wed Jul 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.11.0-1
- Update to 2.11.0
* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.10.1-3
- rebuild
- Add missing br libtool
* Fri May 19 2006 John (J5) Palmieri <johnp@redhat.com> - 2.10.1-2
- Cleanup
* Fri May 12 2006 John (J5) Palmieri <johnp@redhat.com> - 2.10.1-1
- Initial package
