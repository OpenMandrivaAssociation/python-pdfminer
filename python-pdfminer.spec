%global cmapdir %(echo `rpm -qls ghostscript-common | grep CMap | awk '{print $2}'`)

Summary:	PDF parser and analyzer
Name:		python-pdfminer
Version:	20250327
Release:	2
Group:		Development/Python
License:	MIT and Public Domain and APAFML and BSD and (ASL 2.0 and MIT)
URL:		https://github.com/pdfminer/pdfminer.six
#Source0:	https://github.com/pdfminer/pdfminer.six/archive/%{version}/pdfminer-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/p/pdfminer.six/pdfminer_six-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-git-versioning)
BuildRequires:	python%{pyver}dist(wheel)
BuildArch:	noarch

%rename python-pdfminer-six

%description
PDFMiner is a tool for extracting information from PDF documents. Unlike other
PDF-related tools, it focuses entirely on getting and analyzing text data.
PDFMiner allows to obtain the exact location of texts in a page, as well as
other information such as fonts or lines. It includes a PDF converter that can
transform PDF files into other text formats (such as HTML). It has an
extensible PDF parser that can be used for other purposes instead of text
analysis.

%files
%{_bindir}/dumppdf.py
%{_bindir}/pdf2txt.py
%{py_puresitedir}/pdfminer
%{py_puresitedir}/pdfminer_six-*.*-info/

#--------------------------------------------------------------------

%prep
%autosetup -n pdfminer_six-%{version}

%build
%py_build

%install
%py_install

rm -fr %{buildroot}%{_bindir}/__pycache__
