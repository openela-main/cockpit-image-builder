Name:           cockpit-image-builder
Version:        60
Release:        1%{?dist}
Summary:        Image builder plugin for Cockpit

License:        Apache-2.0
URL:            http://osbuild.org/
Source0:        https://github.com/osbuild/image-builder-frontend/releases/download/v%{version}/%{name}-%{version}.tar.gz

Obsoletes:      cockpit-composer < 54
Provides:       cockpit-composer = %{version}-%{release}

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  nodejs

Requires:       cockpit
Requires:       cockpit-files
Requires:       osbuild-composer >= 131

%description
The image-builder-frontend generates custom images suitable for
deploying systems or uploading to the cloud. It integrates into Cockpit
as a frontend for osbuild.

%prep
%setup -q -n %{name}

%build
# Nothing to build

%install
%make_install PREFIX=/usr
# drop source maps, they are large and just for debugging
find %{buildroot}%{_datadir}/cockpit/ -name '*.map' | xargs --no-run-if-empty rm --verbose

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*

%files
%doc cockpit/README.md
%license LICENSE
%{_datadir}/cockpit/cockpit-image-builder
%{_datadir}/metainfo/*

%changelog
* Wed Feb 12 2025 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 60-1
- New upstream release

* Fri Feb 07 2025 Sanne Raymaekers <sanne.raymaekers@gmail.com> - 59-1
- New upstream release


* Thu Jan 16 2025 Packit <hello@packit.dev> - v54-1
Initial commit on c10s
Resolves: RHELPLAN-171405

