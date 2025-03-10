#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	A case-insensitive ordered dictionary for Python
Summary(pl.UTF-8):	Uporządkowany słownik dla Pythona ignorujący wielkość liter
Name:		python-nocasedict
# keep 1.x here for python2 support
Version:	1.1.2
Release:	2
License:	LGPL v2+
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/nocasedict/
Source0:	https://files.pythonhosted.org/packages/source/n/nocasedict/nocasedict-%{version}.tar.gz
# Source0-md5:	19771bb79c0376a1eb128697dcf5963f
URL:		https://pypi.org/project/nocasedict/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest >= 4.3.1
BuildRequires:	python-six >= 1.14.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 6.2.5
BuildRequires:	python3-six >= 1.14.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class NocaseDict is a case-insensitive ordered dictionary that
preserves the original lexical case of its keys.

%description -l pl.UTF-8
Klasa NocaseDict to ignorujący wielkość liter, uporządkowany słownik,
zachowujący oryginalną wielkość liter kluczy.

%package -n python3-nocasedict
Summary:	A case-insensitive ordered dictionary for Python
Summary(pl.UTF-8):	Uporządkowany słownik dla Pythona ignorujący wielkość liter
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-nocasedict
Class NocaseDict is a case-insensitive ordered dictionary that
preserves the original lexical case of its keys.

%description -n python3-nocasedict -l pl.UTF-8
Klasa NocaseDict to ignorujący wielkość liter, uporządkowany słownik,
zachowujący oryginalną wielkość liter kluczy.

%prep
%setup -q -n nocasedict-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/nocasedict
%{py_sitescriptdir}/nocasedict-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-nocasedict
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/nocasedict
%{py3_sitescriptdir}/nocasedict-%{version}-py*.egg-info
%endif
