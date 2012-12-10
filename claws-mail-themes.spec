%define debug_package %{nil}

Summary:	Icon themes for Claws-Mail
Name:		claws-mail-themes
Version:	20120129
Release:	1
License:	GPL+
Group:		Networking/Mail
URL:		http://claws-mail.org/
Source0:	http://www.claws-mail.org/themes/%{name}-%{version}.tar.gz
Requires:	claws-mail
BuildArch:	noarch
Obsoletes:	sylpheed-claws-themes < %{version}
Provides:	sylpheed-claws-themes = %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This package contains various user contributed icon themes for claws-mail.

%prep
%setup -q

%build
./autogen.sh

%configure2_5x
%make

%install
%makeinstall_std

%files
%{_datadir}/claws-mail/themes/*


%changelog
* Thu Jul 19 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 20120129-1
+ Revision: 810297
- update to new snapshot 20120129

* Tue Oct 04 2011 Andrey Bondrov <abondrov@mandriva.org> 20110216-1
+ Revision: 702765
- New version: 20110216

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - update to new version 20100514

* Sun Feb 28 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 20100115-1mdv2010.1
+ Revision: 512743
- update to new version 20100115

* Sun Jul 12 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 20090605-1mdv2010.0
+ Revision: 395171
- remove %%doc
- don't generate debug package
- update to new version 20090605
- spec file clean

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 20070116-5mdv2009.0
+ Revision: 140694
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Apr 19 2007 Jérôme Soyer <saispo@mandriva.org> 20070116-5mdv2008.0
+ Revision: 14995
- Rebuild for latest release


* Fri Mar 09 2007 Jérôme Soyer <saispo@mandriva.org> 20070116-4mdv2007.1
+ Revision: 138690
- Rebuild for latest claws-mail

* Wed Feb 28 2007 Jérôme Soyer <saispo@mandriva.org> 20070116-3mdv2007.1
+ Revision: 126866
- Rebuild

* Fri Feb 16 2007 Jérôme Soyer <saispo@mandriva.org> 20070116-2mdv2007.1
+ Revision: 121614
- Rebuild for latest RC

* Sun Jan 28 2007 Jérôme Soyer <saispo@mandriva.org> 20070116-1mdv2007.1
+ Revision: 114619
- New release

* Sat Jan 06 2007 Jérôme Soyer <saispo@mandriva.org> 20060615-1mdv2007.1
+ Revision: 104882
- Import claws-mail-themes

