Name:           python-protonup
Version:        0.2.1
Release:        1
Summary:        Manage Proton-GE Installations
License:        GPL-3.0-only
Group:          Games/Tools
# Original source https://github.com/AUNaseef/protonup is no longer updated, so let's use active fork.
URL:            https://github.com/cloudishBenne/protonup-ng
Source:         https://github.com/cloudishBenne/protonup-ng/archive/refs/tags/%{version}/protonup-ng-%{version}.tar.gz
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)
Requires:       python3dist(requests)
# This is a drop in replacement of protonup, and uses the same filenames for compatibility.
Provides:       python3-protonup
BuildArch:      noarch


%description
Manage Proton-GE Installations

%prep
%autosetup -n protonup-ng-%{version} -p1

%build
%py_build

%install
%py_install



%files
%doc README.md
%license LICENSE
%{_bindir}/protonup
%{python_sitelib}/protonup*
