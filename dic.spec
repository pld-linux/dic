Summary:	Dic is a simple, console-based disk catalogizer
Summary(hu.UTF-8):	Dic egy egyszerű, konzolos lemez katalogizáló
Name:		dic
Version:	0.7
Release:	0.1
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

%description
Dic is a simple, console-based disk catalogizer.

%description -l hu.UTF-8
Dic egy egyszerű, konzolos lemez katalogizáló.

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
