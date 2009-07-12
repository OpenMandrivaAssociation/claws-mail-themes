Summary:	Icon themes for Claws-Mail
Name:		claws-mail-themes
Version:	20090605
Release:	%mkrel 1
License:	GPL
Group:		Networking/Mail
URL:		http://claws-mail.org/
Source0:	http://www.claws-mail.org/themes/%{name}-%{version}.tar.bz2 
Requires:	claws-mail >= 2.7.0
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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %{name}
%defattr(-,root,root)
%doc RELEASE_NOTES
%{_datadir}/claws-mail/themes/*
