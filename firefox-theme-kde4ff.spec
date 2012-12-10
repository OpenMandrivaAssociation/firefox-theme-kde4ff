%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define _mozillaextpath %{firefox_mozillapath}/extensions

Summary: KDEFF theme for Mozilla Firefox
Name: firefox-theme-kde4ff
Version: 0.14
Release: %mkrel 23
License: GPLv3
Group: Networking/WWW
URL: https://addons.mozilla.org/en-US/firefox/addon/7574
Source: http://kfirefox.googlecode.com/files/kde4-%version.jar
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: firefox = %{firefox_epoch}:%{firefox_version}
Obsoletes: mozilla-firefox-theme-kdeff <= 0.4
Provides: mozilla-firefox-theme-kdeff = %{version}-%{release}
BuildRequires: firefox-devel

%description
KDE4FF is a KDE4-like theme using Oxygen icons for Mozilla Firefox 3.

%prep
# Unfortunately, we have to fix the packaging for this one. :(
%setup -T -q -c -n %{name}-%{version}
unzip -q %{SOURCE0}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_mozillaextpath}

# this rdf contains 3 em:id sections.
hash="$(sed -n '/.*em:id="\(kde.*\)"/{s//\1/p;q}' install.rdf)"
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
%dir %firefox_mozillapath
%{_mozillaextpath}


%changelog
* Thu Jan 06 2011 Thierry Vignaud <tv@mandriva.org> 0.14-23mdv2011.0
+ Revision: 628971
- rebuild for new firefox

* Tue Jul 27 2010 Funda Wang <fwang@mandriva.org> 0.14-22mdv2011.0
+ Revision: 561840
- rebulid for ff 3.6.8

* Fri Jan 22 2010 Funda Wang <fwang@mandriva.org> 0.14-21mdv2010.1
+ Revision: 494805
- rebuild

* Wed Dec 16 2009 Funda Wang <fwang@mandriva.org> 0.14-20mdv2010.1
+ Revision: 479194
- rebuild for new ff

* Fri Nov 06 2009 Funda Wang <fwang@mandriva.org> 0.14-19mdv2010.1
+ Revision: 460659
- rebuild for new ff

* Tue Oct 06 2009 Funda Wang <fwang@mandriva.org> 0.14-18mdv2010.0
+ Revision: 454545
- rebuild

* Tue Aug 18 2009 Gustavo De Nardin <gustavodn@mandriva.com> 0.14-17mdv2010.0
+ Revision: 417676
- buildrequire firefox-devel, which provides the new macros for building extensions
- make use of the firefox package macros
- rebuild for firefox 3.5.2

  + Eugeni Dodonov <eugeni@mandriva.com>
    - Rebuild for firefox 3.0.13.

* Fri Jul 31 2009 Funda Wang <fwang@mandriva.org> 0.14-14mdv2010.0
+ Revision: 405037
- rebuild for new ff

* Wed Jul 22 2009 Raphaël Gertz <rapsys@mandriva.org> 0.14-13mdv2010.0
+ Revision: 398604
- Rebuild
- Revert the greater or equal useless

* Wed Jul 22 2009 Raphaël Gertz <rapsys@mandriva.org> 0.14-12mdv2010.0
+ Revision: 398583
- Allow firefox 3.0.11 and greater

* Sun Jun 14 2009 Funda Wang <fwang@mandriva.org> 0.14-11mdv2010.0
+ Revision: 385779
- rebuild for new ff

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 0.14-10mdv2010.0
+ Revision: 369621
- rebuild for new ff

* Sat Mar 28 2009 Gustavo De Nardin <gustavodn@mandriva.com> 0.14-9mdv2009.1
+ Revision: 361855
- rebuild for firefox 3.0.8

* Sat Mar 14 2009 Funda Wang <fwang@mandriva.org> 0.14-8mdv2009.1
+ Revision: 354812
- rebuild for new ff

* Wed Feb 04 2009 Funda Wang <fwang@mandriva.org> 0.14-7mdv2009.1
+ Revision: 337345
- rebuild for new ff

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 0.14-6mdv2009.1
+ Revision: 318925
- rebuild for new ff

* Sun Nov 16 2008 Funda Wang <fwang@mandriva.org> 0.14-5mdv2009.1
+ Revision: 303690
- rebuild for new ff

* Mon Sep 29 2008 Funda Wang <fwang@mandriva.org> 0.14-4mdv2009.0
+ Revision: 289181
- rebuild for new FF

* Fri Sep 26 2008 Tiago Salem <salem@mandriva.com.br> 0.14-3mdv2009.0
+ Revision: 288677
- version 3.0.2

* Wed Aug 13 2008 Tiago Salem <salem@mandriva.com.br> 0.14-2mdv2009.0
+ Revision: 271642
- fix sed in rdf file to get the right id.
- bump release

* Tue Aug 12 2008 Funda Wang <fwang@mandriva.org> 0.14-1mdv2009.0
+ Revision: 271098
- New version 0.14

* Wed Aug 06 2008 Frederic Crozat <fcrozat@mandriva.com> 0.10-3mdv2009.0
+ Revision: 264185
- handle upgrade from 2008.1 better

* Fri Aug 01 2008 Tiago Salem <salem@mandriva.com.br> 0.10-2mdv2009.0
+ Revision: 260088
- obsoleting kde theme for firefox 2

* Fri Aug 01 2008 Tiago Salem <salem@mandriva.com.br> 0.10-1mdv2009.0
+ Revision: 259827
- import firefox-theme-kde4ff


