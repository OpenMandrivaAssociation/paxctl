%define name	paxctl
%define version	0.3
%define release 1

Name:		%{name}
Summary:	Tool that allows PaX flags to be modified on a per-binary basis
Version:	%{version}
Release:	%mkrel %{release}
Source0:	%{name}-%{version}.tar.gz
URL:		http://pax.grsecurity.net/
Group:		System/Configuration/Other
License:	Public Domain

%description
This is paxctl for controlling PaX flags on a per binary basis. PaX
is an intrusion prevention system that provides the best protection
mechanisms against memory corruption bugs. Some applications are not
compatible with certain features (due to design or bad engineering)
and therefore they have to be exempted from certain enforcements. It
is also possible to use PaX in soft mode where none of the protection
mechanisms are active by default - here paxctl can be used to turn
them on for selected programs (e.g., network daemons, programs that
process network data such as mail clients, web browsers, etc).

%prep
%setup -q

%build 
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(644,root,root,0755) 
%doc README ChangeLog
%{_mandir}/man1/%{name}.1*
%defattr(-,root,root,0755)
/sbin/%{name}

