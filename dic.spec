# TODO:
# - maybe create bash-completion
# - mc subpackage: doesn't work the %%post. Why?
Summary:	Dic is a simple, console-based disk catalogizer
Summary(hu.UTF-8):	Dic egy egyszerű, konzolos lemez katalogizáló
Name:		dic
Version:	0.7
Release:	1.7
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/dic/%{name}-%{version}.tar.bz2
# Source0-md5:	c604751a05298dad2492189e1f31ec21
URL:		http://dic.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
#Requires:		python-libs
Requires:	python-modules
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	mcextfs %{_datadir}/mc/extfs/extfs.ini

%description
Dic is a simple, console-based disk catalogizer. It can easily add
disks to the catalog, search in the catalog, search for files,
automatically retrieve found files without requiring you to manually
navigate through the source media, and more.

%description -l hu.UTF-8
Dic egy egyszerű, konzolos lemez katalogizáló. Könnyen adhatsz új
lemezeket a katalógushoz, kereshetsz a katalógusban, fájlok után,
automatikusan átmásolhatod a fájlokat kézi navigálás nélkül, stb.

%package mc
Summary:	Extfs plugin for Midnight Commander
Summary(hu.UTF-8):	Extfs plugin Midnight Commander-hez
Group:		Applications/Shells
Requires:	mc

%description mc
Extfs plugin for Midnight Commander. In the running Midnight Commander
type "cd #mcdic".

%description mc -l hu.UTF-8
Extfs plugin Midnight Commander-hez. A futó Midnight Commander-ben
gépeld be a "cd #mcdic" sort!

%prep
%setup -q

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

install -d $RPM_BUILD_ROOT%{_mandir}/man{1,5}
install man/dic.1 $RPM_BUILD_ROOT%{_mandir}/man1
install man/dic.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5

install -d $RPM_BUILD_ROOT%{_datadir}/mc/extfs
install build/scripts-2.6/mcdic $RPM_BUILD_ROOT%{_datadir}/mc/extfs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_sysconfdir}/dic
%{_mandir}/man1/dic.1.*
%{_mandir}/man5/dic.conf.5.*
%{_sysconfdir}/dic/*
%attr(755,root,root) %{_bindir}/*dic
%{py_sitescriptdir}/*

%files mc
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/mc/extfs/mcdic

%post mc
if [ -f %{mcextfs} ]; then
	grep -q mcdic %{mcextfs} || echo -e "\n# dic disk catalogizer\nmcdic:\n" >> %{mcextfs}
fi
