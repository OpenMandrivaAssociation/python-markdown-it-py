%define module markdown_it
%define oname markdown_it_py

Name:		python-markdown-it-py
Summary:	Python port of markdown-it
Version:	4.0.0
Release:	1
Group:		Development/Python
License:	MIT
URL:		https://github.com/executablebooks/markdown-it-py
Source0:	https://github.com/executablebooks/markdown-it-py/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

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
%doc README.md
%license LICENSE LICENSE.markdown-it
%{_bindir}/markdown-it
%{py_sitedir}/%{module}
%{py_sitedir}/%{oname}-%{version}.dist-info
