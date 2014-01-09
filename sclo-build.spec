Name:		sclo-build
Version:	3
Release:	1%{?dist}
Summary:	Macros for collections for softwarecollections.org

Group:		Development/Tools
License:	MIT
URL:		https://github.com/xsuchy/sclo-build
# git clone git@github.com:xsuchy/sclo-build.git
# cd sclo-build
# tito build --tgz
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

%description
Define macros for building software collection into
softwarecollections.org.

%prep
%setup -q


%build
# nothing to do here


%install
mkdir -p %{buildroot}%{_sysconfdir}/rpm/
%if 0%{?rhel} && 0%{?rhel} < 8
install -p macros.sclo.el %{buildroot}%{_sysconfdir}/rpm/macros.sclo
%else
install -p macros.sclo %{buildroot}%{_sysconfdir}/rpm/
%endif


%files
%doc LICENSE
%{_sysconfdir}/rpm/macros.sclo


%changelog
* Thu Jan 09 2014 Miroslav Suchý <msuchy@redhat.com> 3-1
- fix path on el6 (msuchy@redhat.com)

* Thu Jan 09 2014 Miroslav Suchý <msuchy@redhat.com> 2-1
- rhel does not have scl_vendor macro (yet) (msuchy@redhat.com)
- package is noarch (msuchy@redhat.com)

* Thu Jan 09 2014 Miroslav Suchý <msuchy@redhat.com> 1-1
- initial release


