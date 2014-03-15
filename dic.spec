Summary:	Dic is a simple, console-based disk catalogizer
Summary(hu.UTF-8):	Dic egy egyszerű, konzolos lemez katalogizáló
Name:		dic
Version:	0.7
Release:	7
License:	GPL v2
Group:		Applications
Source0:	http://downloads.sourceforge.net/dic/%{name}-%{version}.tar.bz2
# Source0-md5:	c604751a05298dad2492189e1f31ec21
Source1:	%{name}-bash-completion
URL:		http://dic.sourceforge.net/
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dic is a simple, console-based disk catalogizer. It can easily add
disks to the catalog, search in the catalog, search for files,
automatically retrieve found files without requiring you to manually
navigate through the source media, and more.

%description -l hu.UTF-8
Dic egy egyszerű, konzolos lemez katalogizáló. Könnyen adhatsz új
lemezeket a katalógushoz, kereshetsz a katalógusban, fájlok után,
automatikusan átmásolhatod a fájlokat kézi navigálás nélkül, stb.

%package -n mc-plugin-dic
Summary:	Extfs plugin for Midnight Commander
Summary(hu.UTF-8):	Extfs plugin Midnight Commander-hez
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	mc
Obsoletes:	dic-dic

%description -n mc-plugin-dic
Extfs plugin for Midnight Commander. In the running Midnight Commander
type "cd #mcdic".

%description -n mc-plugin-dic -l hu.UTF-8
Extfs plugin Midnight Commander-hez. A futó Midnight Commander-ben
gépeld be a "cd #mcdic" sort!

%package -n bash-completion-%{name}
Summary:	bash-completion to dic
Summary(hu.UTF-8):	Bash automatikus kiegészítés dic-hez
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n bash-completion-%{name}
Bash-completion to dic.

%description -n bash-completion-%{name} -l hu.UTF-8
Bash automatikus kiegészítés dic-hez.

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
cp -a man/dic.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -a man/dic.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5

install -d $RPM_BUILD_ROOT%{_libdir}/mc/extfs.d
install -p build/scripts-2.7/mcdic $RPM_BUILD_ROOT%{_libdir}/mc/extfs.d

install -d $RPM_BUILD_ROOT/etc/bash_completion.d
cp -a %{SOURCE1} $RPM_BUILD_ROOT/etc/bash_completion.d/dic

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

%files -n mc-plugin-dic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mc/extfs.d/mcdic

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
/etc/bash_completion.d/%{name}
