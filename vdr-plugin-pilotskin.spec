
%define plugin	pilotskin
%define name	vdr-plugin-%plugin
%define version	0.0.3
%define rel	8

Summary:	VDR plugin: A zapping co-pilot
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL+
URL:		http://vdrwiki.free.fr/vdr/pilotskin/
Source:		http://vdrwiki.free.fr/vdr/pilotskin/files/vdr-%plugin-%version.tgz
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Pilotskin is a plugin for VDR based on the plugin vdr-pilot created
by Olivier Jacques. It brings the ability to quickly browse the EPG
information. The browsing calls the skin that you use, and the
plugin has the appearance of the OSD *Display Channel Info*. The
plugin adds the possibility of having detailed information of the
event and launching timers.

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.3-7mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.3-6mdv2009.1
+ Revision: 359348
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.3-5mdv2009.0
+ Revision: 197960
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.3-4mdv2009.0
+ Revision: 197703
- add vdr_plugin_prep
- bump buildrequires on vdr-devel

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.3-3mdv2008.1
+ Revision: 145166
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3-2mdv2008.1
+ Revision: 103178
- rebuild for new vdr

* Fri Sep 07 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3-1mdv2008.0
+ Revision: 81885
- 0.0.3
- adapt license tag to the new policy

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-10mdv2008.0
+ Revision: 50028
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-9mdv2008.0
+ Revision: 42114
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-8mdv2008.0
+ Revision: 22766
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-7mdv2007.0
+ Revision: 90957
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-6mdv2007.1
+ Revision: 74067
- rebuild for new vdr
- Import vdr-plugin-pilotskin

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-2mdv2007.0
- rebuild for new vdr

* Tue Jul 18 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-1mdv2007.0
- initial Mandriva release

