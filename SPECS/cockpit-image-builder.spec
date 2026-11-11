Name:           cockpit-image-builder
Version:        110.3
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
BuildRequires:  /usr/bin/node
BuildRequires:  npm
# for _tmpfilesdir macro
BuildRequires:  systemd-rpm-macros

Requires:       cockpit
Requires:       cockpit-files
Requires:       image-builder >= 76.0.0

Recommends:     cockpit-machines

%description
The image-builder-frontend generates custom images suitable for
deploying systems or uploading to the cloud. It integrates into Cockpit
as a frontend for osbuild.

%prep
%setup -q -n %{name}

%build
NODE_ENV=production npm run build:cockpit

%install
%make_install PREFIX=/usr
# drop source maps, they are large and just for debugging
find %{buildroot}%{_datadir}/cockpit/ -name '*.map' | xargs --no-run-if-empty rm --verbose

install -m 0755 -vd %{buildroot}%{_tmpfilesdir}
install -m 0644 -vp cockpit/tmpfiles.d/cockpit-image-builder.conf %{buildroot}%{_tmpfilesdir}/cockpit-image-builder.conf

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*

%files
%doc cockpit/README.md
%license LICENSE
%{_datadir}/cockpit/cockpit-image-builder
%{_datadir}/metainfo/*
%{_tmpfilesdir}/cockpit-image-builder.conf
%ghost %attr(0700, root, root) %dir /var/cache/cockpit-image-builder

%changelog
* Mon Oct 26 2026 Anna Vítová <avitova@redhat.com> - 110.3-1
- New upstream release

* Fri Oct 23 2026 Anna Vítová <avitova@redhat.com> - 110.2-1
- New upstream release

* Mon Sep 22 2026 Anna Vítová <avitova@redhat.com> - 110.1-1
- New upstream release

* Fri Aug 21 2026 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 110-1
- New upstream release

* Wed Aug 19 2026 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 108-1
- New upstream release

* Fri Aug 07 2026 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 106-1
- New upstream release

* Mon Feb 23 2026 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 94-1
- New upstream release

* Tue Feb 17 2026 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 93-1
- New upstream release

* Fri Feb 13 2026 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 92-1
- New upstream release

* Wed Dec 10 2025 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 86-1
- New upstream release

* Fri Nov 21 2025 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 83-1
- New upstream release

* Wed Oct 29 2025 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 81-1
- New upstream release

* Mon Oct 27 2025 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 80-1
- New upstream release

* Tue Oct 07 2025 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 78-1
- New upstream release

* Wed Sep 17 2025 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 77-1
- New upstream release

* Wed Sep 03 2025 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 76-1
- New upstream release

* Thu Aug 21 2025 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 75-1
- New upstream release

* Wed Aug 20 2025 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 74-1
- New upstream release

* Wed Aug 06 2025 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 73-1
- New upstream release

* Wed Jul 23 2025 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 72-1
- New upstream release

* Sat Jul 12 2025 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 71-1
- New upstream release

* Wed Jun 11 2025 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 69-1
- New upstream release

* Thu Jun 05 2025 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 68-1
- New upstream release

* Wed Apr 16 2025 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 65-1
- New upstream release

* Wed Feb 12 2025 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 60-1
- New upstream release

* Fri Feb 07 2025 Sanne Raymaekers <sanne.raymaekers@gmail.com> - 59-1
- New upstream release


* Thu Jan 16 2025 Packit <hello@packit.dev> - v54-1
Initial commit on c10s
Resolves: RHELPLAN-171405

