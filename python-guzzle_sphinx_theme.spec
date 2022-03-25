#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx theme used by Guzzle
Summary(pl.UTF-8):	Motyw Sphinksa wykorzystywany przez Guzzle
Name:		python-guzzle_sphinx_theme
Version:	0.7.11
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/guzzle_sphinx_theme/
Source0:	https://files.pythonhosted.org/packages/source/g/guzzle_sphinx_theme/guzzle_sphinx_theme-%{version}.tar.gz
# Source0-md5:	f6ec1c3fe16ce9f076941912df0cc4cd
URL:		https://pypi.org/project/guzzle_sphinx_theme/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinx theme used by Guzzle: <http://guzzlephp.org/>.

%description -l pl.UTF-8
Motyw Sphinksa wykorzystywany przez Guzzle: <http://guzzlephp.org/>.

%package -n python3-guzzle_sphinx_theme
Summary:	Sphinx theme used by Guzzle
Summary(pl.UTF-8):	Motyw Sphinksa wykorzystywany przez Guzzle
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-guzzle_sphinx_theme
Sphinx theme used by Guzzle: <http://guzzlephp.org/>.

%description -n python3-guzzle_sphinx_theme -l pl.UTF-8
Motyw Sphinksa wykorzystywany przez Guzzle: <http://guzzlephp.org/>.

%prep
%setup -q -n guzzle_sphinx_theme-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
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
%doc LICENSE README.rst
%{py_sitescriptdir}/guzzle_sphinx_theme
%{py_sitescriptdir}/guzzle_sphinx_theme-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-guzzle_sphinx_theme
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/guzzle_sphinx_theme
%{py3_sitescriptdir}/guzzle_sphinx_theme-%{version}-py*.egg-info
%endif
