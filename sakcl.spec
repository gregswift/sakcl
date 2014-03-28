Name:           sakcl
Version:        0.1.0
Release:        1%{?dist}
Summary:        SSH AuthorizedKeysCommand Lookup tool

License:        ASLv2
URL:            https://github.com/gregswift/sakcl
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
Requires:       python-requests
Requires:       python-configobj

%description


%prep
%setup -q


%build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%doc
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_sbindir}/%{name}

%changelog
* Fri Mar 28 2014 greg5320 <gregswift@gmail.com>
- Initial build
