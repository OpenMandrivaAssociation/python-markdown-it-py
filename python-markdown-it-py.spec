Summary:	Python port of markdown-it
Name:		python-markdown-it-py
Version:	3.0.0
Release:	2
Group:		Development/Python
License:	MIT
URL:		https://github.com/executablebooks/markdown-it-py
#Source0:	https://github.com/executablebooks/markdown-it-py/archive/v%{version}/markdown-it-py-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/m/markdown-it-py/markdown-it-py-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(wheel)

BuildArch:	noarch

%description
Markdown parser, done right. 100% CommonMark support, extensions, syntax
plugins & high speed. Now in Python!

Features:

 *   Follows the CommonMark spec for baseline parsing
 *   Configurable syntax: you can add new rules and even replace existing
     ones.
 *   Pluggable: Adds syntax extensions to extend the parser (see the
     plugin list).
 *   High speed (see our benchmarking tests)
 *   Safe by default

This is a Python port of markdown-it, and some of its associated plugins.

%files
%license LICENSE LICENSE.markdown-it
%doc README.md
%{_bindir}/markdown-it
%{py_sitedir}/markdown_it
%{py_sitedir}/markdown_it_py-*.*-info

#--------------------------------------------------------------------

%prep
%autosetup -n markdown-it-py-%{version}

%build
%py_build
 
%install
%py_install

