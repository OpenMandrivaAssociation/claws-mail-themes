%define name claws-mail-themes
%define pkgname sylpheed-claws-themes
%define version_name claws-mail
%define version 20070116 
%define rel 4

Summary:             Icon themes for %{version_name}
Name:			%{name}
Version:		%{version}
Release:		%mkrel %{rel}
Source:			http://prdownloads.sf.net/%{name}-%{version}.tar.bz2 
License:		GPL
URL:			http://claws-mail.org/
Group:			Networking/Mail
Requires:              %{version_name} >= 2.7.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch 
Obsoletes:	sylpheed-claws-themes
Provides:	sylpheed-claws-themes

%description
This package contains various user contributed icon themes for claws-mail.
Now available as a separate rpm.

%prep
%setup -q 

%build

%configure2_5x

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std   

%clean
rm -rf %{buildroot}

%files -n %{name}
%defattr(-,root,root)
%doc RELEASE_NOTES
%{_datadir}/%{version_name}/themes/*


