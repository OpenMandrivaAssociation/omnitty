%define name omnitty
%define version 0.2.8
%define release 6

%define debug_package %{nil}

Summary: Omnitty ssh multiplexer
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: System/Kernel and hardware
Url: http://omnitty.sourceforge.net/
BuildRequires: librote-devel

%description
Omnitty is a curses-based program that allows one to log into 
several machines simultaneously and interact with them, selectively 
directing input to individual machines or groups of selected machines.

%prep
%setup -q

%build
export LDFLAGS="-lncurses"
%configure
%make

%install
%makeinstall

%clean

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*


%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.2.8-5mdv2010.0
+ Revision: 430202
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.2.8-4mdv2009.0
+ Revision: 254524
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.2.8-2mdv2008.1
+ Revision: 134698
- fix group
- kill re-definition of %%buildroot on Pixel's request
- import omnitty


* Mon Apr 24 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.2.8-2mdk
- Add BuildRequires
- use mkrel

* Fri Apr 15 2005  <guibo@guibpiv.guibland.com> 0.2.8-1mdk
- first release
