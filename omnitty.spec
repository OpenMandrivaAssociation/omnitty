%define debug_package %{nil}

Summary: Omnitty ssh multiplexer
Name:    omnitty
Version: 0.2.8
Release: 8
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group:   System/Kernel and hardware
Url:     http://omnitty.sourceforge.net/
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
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
