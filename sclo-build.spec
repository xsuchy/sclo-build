Name:		sclo-build
Version:	1
Release:	1%{?dist}
Summary:	Macros for collections for softwarecollections.org

Group:		Development/Tools
License:	MIT
URL:		https://github.com/xsuchy/sclo-build
# git clone git@github.com:xsuchy/sclo-build.git
# cd sclo-build
# tito build --tgz
Source0:	%{name}-%{version}.tar.gz

%description
Define macros for building software collection into
softwarecollections.org.

%prep
%setup -q


%build
# nothing to do here


%install
mkdir -p %{buildroot}%{_sysconfdir}/rpm/
install -p macros.sclo %{buildroot}%{_sysconfdir}/rpm/ 


%files
%doc LICENSE
%{_sysconfdir}/rpm/macros.sclo


%changelog
* Thu Jan 09 2014 Miroslav Suchý <msuchy@redhat.com> 1-1
- initial release


