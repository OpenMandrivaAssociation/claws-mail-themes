%define debug_package %{nil}

Summary:	Icon themes for Claws-Mail
Name:		claws-mail-themes
Version:	20140629
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
%make_build

%install
%make_install

%files
%{_datadir}/claws-mail/themes/*

