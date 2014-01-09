Name:       sclo-build
Version:    4
Release:    1%{?dist}
Summary:    Macros for collections for softwarecollections.org

Group:		Development/Tools
License:	MIT
URL:		https://github.com/xsuchy/sclo-build
# git clone git@github.com:xsuchy/sclo-build.git
# cd sclo-build
# tito build --tgz
Source0:    %{name}-%{version}.tar.gz
BuildArch:  noarch
%if 0%{?rhel} && 0%{?rhel} < 6
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
%endif

%description
Define macros for building software collection into
softwarecollections.org.

%prep
%setup -q


%build
# nothing to do here


%install
%if 0%{?rhel} && 0%{?rhel} < 6
rm -rf %{buildroot}
%endif
mkdir -p %{buildroot}%{_sysconfdir}/rpm/
%if 0%{?rhel} && 0%{?rhel} < 8
install -p macros.sclo.el %{buildroot}%{_sysconfdir}/rpm/macros.sclo
%else
install -p macros.sclo %{buildroot}%{_sysconfdir}/rpm/
%endif


%if 0%{?rhel} && 0%{?rhel} < 6
%clean
rm -rf %{buildroot}
%endif

%files
%doc LICENSE
%{_sysconfdir}/rpm/macros.sclo


%changelog
* Thu Jan 09 2014 Miroslav Suchý <msuchy@redhat.com> 4-1
- define and clean buildroot on el5 (msuchy@redhat.com)
- scl_vendor is not defined neither in el7 (msuchy@redhat.com)

* Thu Jan 09 2014 Miroslav Suchý <msuchy@redhat.com> 3-1
- fix path on el6 (msuchy@redhat.com)

* Thu Jan 09 2014 Miroslav Suchý <msuchy@redhat.com> 2-1
- rhel does not have scl_vendor macro (yet) (msuchy@redhat.com)
- package is noarch (msuchy@redhat.com)

* Thu Jan 09 2014 Miroslav Suchý <msuchy@redhat.com> 1-1
- initial release


