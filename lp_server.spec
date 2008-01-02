Summary:	Daemon for local printers (simulates HP JetDirect)
Name:		lp_server
Version:	1.1.6
Release:	%mkrel 1
License:	GPL
Group:		System/Servers
URL:		http://www.ltsp.org
Source0:	http://www.ltsp.org/tarballs/%{name}-%{version}.tar.bz2
BuildRequires:	uClibc-devel
BuildRequires:	uClibc-static-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This program allows you to 'export' a printer on your local host to be used by
an LPRng spooler.  It is basically simulating an HP JetDirect interface, which
opens a connection on port 9100 and simply dumps input to the PostScript
Engine.

%prep

%setup -q -n %{name}-%{version}

%build

export CFLAGS="%{optflags}"
uclibc ./configure --prefix=/

perl -pi -e "s/-lnsl/-Wl,-Bstatic -lnsl/;" src/Makefile

uclibc make

%install
rm -rf %{buildroot}

install -d %{buildroot}/sbin
install -d %{buildroot}%{_mandir}/man8

install -m0755 src/%{name} %{buildroot}/sbin
install -m0644 man/*.8 %{buildroot}%{_mandir}/man8

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING CHANGES Copyright INSTALL LICENSE README UPDATE VERSION
/sbin/%{name}
%{_mandir}/man8/*


