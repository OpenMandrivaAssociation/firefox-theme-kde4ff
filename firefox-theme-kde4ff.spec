%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define ff_epoch 0
%define ff_ver 3.0.1

%define _mozillapath %{_libdir}/firefox-%{ff_ver}
%define _mozillaextpath %{_mozillapath}/extensions

Summary: KDEFF theme for Mozilla Firefox
Name: firefox-theme-kde4ff
Version: 0.10
Release: %mkrel 2
License: GPL
Group: Networking/WWW
URL: https://addons.mozilla.org/en-US/firefox/addon/7574
Source: https://addons.mozilla.org/pt-BR/firefox/downloads/file/31103/kde4_+_firefox3-%{version}-fx.jar
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: firefox = %{ff_epoch}:%{ff_ver}
Obsoletes: mozilla-firefox-theme-kdeff

%description
KDE4FF is a KDE4-like theme using Oxygen icons for Mozilla Firefox 3.

%prep
# Unfortunately, we have to fix the packaging for this one. :(
%setup -T -q -c -n %{name}-%{version}
unzip %{SOURCE0}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_mozillaextpath}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{_mozillaextpath}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%dir %_mozillapath
%{_mozillaextpath}
