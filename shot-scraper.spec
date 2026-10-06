%define _unpackaged_files_terminate_build 1
%define pypi_name shot-scraper

Name: python3-module-%pypi_name
Version: 1.12
Release: alt1
Summary: A CLI utility for taking screenshots of websites, recording video demos and scraping sites using JavaScript
License: No license
Group: Development/Python3
Url: https://pypi.org/project/shot-scraper
VCS: https://github.com/simonw/shot-scraper.git
Packager: Щипакин М.А. <shipackin.maxim2@yandex.ru>
BuildArch: noarch

Source: shot_scraper-1.12.tar.gz

Provides: python3-module-%{pep503_name %pypi_name} = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-uv-build

Requires: python3-module-click
Requires: python3-module-click-default-group
Requires: python3-module-pydantic
Requires: python3-module-pyyaml
Requires: python3-module-playwright

%description
shot-scraper is a command line utility for taking automated screenshots of web
pages, recording video demos and scraping sites using JavaScript.

It is built on top of Playwright, so the browsers it drives have to be
installed separately:

    shot-scraper install

%prep
%setup -n shot_scraper-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%python3_sitelibdir/shot_scraper/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%_bindir/shot-scraper

%changelog
* Tue Oct 06 2026 Щипакин М.А. <shipackin.maxim2@yandex.ru> 1.12-alt
- First Build
