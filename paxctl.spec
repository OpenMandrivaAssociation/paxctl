%define name	paxctl
%define version	0.5
%define release 2

Name:		%{name}
Summary:	Tool that allows PaX flags to be modified on a per-binary basis
Version:	%{version}
Release:	%mkrel %{release}
Source0:	%{name}-%{version}.tar.gz
URL:		http://pax.grsecurity.net/
Group:		System/Configuration/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
rm -rf %{buildroot}
mkdir -p %{buildroot}/sbin %{buildroot}%{_mandir}/man1
cp -p %{name}.1* %{buildroot}%{_mandir}/man1
cp -p %{name} %{buildroot}/sbin

%clean 
rm -rf %{buildroot}

%files 
%defattr(644,root,root,0755) 
%doc README ChangeLog
%{_mandir}/man1/%{name}.1*
%defattr(-,root,root,0755)
/sbin/%{name}



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.5-2mdv2010.0
+ Revision: 433615
- fix installing (was installing system file instead of its own binary...)
- rebuild

  + Gustavo De Nardin <gustavodn@mandriva.com>
    - 0.5
    - build: easier to install manually than using make install

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.3-1mdv2009.0
+ Revision: 136642
- restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.3-1mdv2008.1
+ Revision: 131044
- kill re-definition of %%buildroot on Pixel's request
- import paxctl


* Mon Aug 08 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.3-1mdk
- 0.3
- %%mkrel

* Wed Jul 28 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.2-1mdk
- initial mdk release
