%define debug_package %{nil}

Summary:	Icon themes for Claws-Mail
Name:		claws-mail-themes
Version:	20110216
Release:	%mkrel 1
License:	GPL+
Group:		Networking/Mail
URL:		http://claws-mail.org/
Source0:	http://www.claws-mail.org/themes/%{name}-%{version}.tar.gz
Patch0:		claws-mail-themes-20110216-fix-elementary-makefile.patch
Requires:	claws-mail >= 2.7.0
BuildArch:	noarch
Obsoletes:	sylpheed-claws-themes < %{version}
Provides:	sylpheed-claws-themes = %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This package contains various user contributed icon themes for claws-mail.

%prep
%setup -q
%patch0 -p1

%build
./autogen.sh

%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %{name}
%defattr(-,root,root)
%{_datadir}/claws-mail/themes/*
