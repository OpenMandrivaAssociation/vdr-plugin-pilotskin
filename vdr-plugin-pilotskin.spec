
%define plugin	pilotskin
%define name	vdr-plugin-%plugin
%define version	0.0.2
%define rel	7

Summary:	VDR plugin: A zapping co-pilot
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://vdrwiki.free.fr/vdr/pilotskin/
Source:		http://vdrwiki.free.fr/vdr/pilotskin/files/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
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

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README


