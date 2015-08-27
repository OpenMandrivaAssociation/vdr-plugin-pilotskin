%define plugin	pilotskin

Summary:	VDR plugin: A zapping co-pilot
Name:		vdr-plugin-%plugin
Version:	0.0.3
Release:	9
Group:		Video
License:	GPL+
URL:		http://vdrwiki.free.fr/vdr/pilotskin/
Source:		http://vdrwiki.free.fr/vdr/pilotskin/files/vdr-%plugin-%{version}.tgz
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
%setup -q -n %plugin-%{version}
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%doc README




