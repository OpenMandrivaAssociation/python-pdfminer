%global cmapdir %(echo `rpm -qls ghostscript-common | grep CMap | awk '{print $2}'`)
%define module pdfminer-six
%define oname pdfminer_six

Summary:	PDF parser and analyzer
Name:		python-pdfminer
Version:	20260107
Release:	1
Group:		Development/Python
License:	MIT and Public Domain and APAFML and BSD and (ASL 2.0 and MIT)
URL:		https://github.com/pdfminer/pdfminer.six
#Source0:	https://github.com/pdfminer/pdfminer.six/archive/%{version}/%{name}-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/p/pdfminer.six/%{oname}-%{version}.tar.gz#/%{name}-%version.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
# Optional dependency
Recommends:	python%{pyver}dist(pillow)

%rename python-pdfminer-six
Provides:	python%{pyver}dist(pdfminer-six) = %{version}

%description
PDFMiner is a tool for extracting information from PDF documents. Unlike other
PDF-related tools, it focuses entirely on getting and analyzing text data.
PDFMiner allows to obtain the exact location of texts in a page, as well as
other information such as fonts or lines. It includes a PDF converter that can
transform PDF files into other text formats (such as HTML). It has an
extensible PDF parser that can be used for other purposes instead of text
analysis.

%prep -a
# Remove bundled egg-info
rm -rf pdfminer.sx.egg-info
# fix interpreter
sed -i -e '/^#!\//, 1d' pdfminer/psparser.py
sed -i '1i #!%{__python}' tools/dumppdf.py tools/pdf2txt.py

%install -a
rm -fr %{buildroot}%{_bindir}/__pycache__

%files
%{_bindir}/dumppdf.py
%{_bindir}/pdf2txt.py
%{python_sitelib}/pdfminer
%{python_sitelib}/%{oname}-%{version}.dist-info
