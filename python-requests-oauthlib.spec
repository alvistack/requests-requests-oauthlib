# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-requests-oauthlib
Epoch: 100
Version: 1.3.0
Release: 1%{?dist}
BuildArch: noarch
Summary: OAuthlib authentication support for Requests
License: ISC
URL: https://github.com/requests/requests-oauthlib/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This project provides first-class OAuth library support for Requests.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-requests-oauthlib
Summary: OAuthlib authentication support for Requests
Requires: python3
Requires: python3-oauthlib >= 3.0.0
Requires: python3-requests >= 2.0.0
Provides: python3-requests-oauthlib = %{epoch}:%{version}-%{release}
Provides: python3dist(requests-oauthlib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-requests-oauthlib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(requests-oauthlib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-requests-oauthlib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(requests-oauthlib) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-requests-oauthlib
This project provides first-class OAuth library support for Requests.

%files -n python%{python3_version_nodots}-requests-oauthlib
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-requests-oauthlib
Summary: OAuthlib authentication support for Requests
Requires: python3
Requires: python3-oauthlib >= 3.0.0
Requires: python3-requests >= 2.0.0
Provides: python3-requests-oauthlib = %{epoch}:%{version}-%{release}
Provides: python3dist(requests-oauthlib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-requests-oauthlib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(requests-oauthlib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-requests-oauthlib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(requests-oauthlib) = %{epoch}:%{version}-%{release}

%description -n python3-requests-oauthlib
This project provides first-class OAuth library support for Requests.

%files -n python3-requests-oauthlib
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
