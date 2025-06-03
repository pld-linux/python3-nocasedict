#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	A case-insensitive ordered dictionary for Python
Summary(pl.UTF-8):	Uporządkowany słownik dla Pythona ignorujący wielkość liter
Name:		python3-nocasedict
Version:	2.1.0
Release:	1
License:	LGPL v2+
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/nocasedict/
Source0:	https://files.pythonhosted.org/packages/source/n/nocasedict/nocasedict-%{version}.tar.gz
# Source0-md5:	23892628af81e55fd8192bc6fa2c4d0f
URL:		https://pypi.org/project/nocasedict/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.5
%if %{with tests}
BuildRequires:	python3-pytest >= 6.2.5
BuildRequires:	python3-six >= 1.14.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class NocaseDict is a case-insensitive ordered dictionary that
preserves the original lexical case of its keys.

%description -l pl.UTF-8
Klasa NocaseDict to ignorujący wielkość liter, uporządkowany słownik,
zachowujący oryginalną wielkość liter kluczy.

%prep
%setup -q -n nocasedict-%{version}

%build
%py3_build_pyproject

%if %{with tests}
%{__python3} -m zipfile -e build-3/*.whl build-3-test
# use explicit plugins list for reliable builds (delete PYTEST_PLUGINS if empty)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
%{__python3} -m pytest -o pythonpath="$PWD/build-3-test" tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.md README.md SECURITY.md
%{py3_sitescriptdir}/nocasedict
%{py3_sitescriptdir}/nocasedict-%{version}.dist-info
