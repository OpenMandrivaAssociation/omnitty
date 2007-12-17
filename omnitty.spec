%define name omnitty
%define version 0.2.8
%define release %mkrel 2

Summary: Omnitty ssh multiplexer
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: System
Url: http://omnitty.sourceforge.net/
BuildRequires: librote-devel

%description
Omnitty is a curses-based program that allows one to log into 
several machines simultaneously and interact with them, selectively 
directing input to individual machines or groups of selected machines.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/*

