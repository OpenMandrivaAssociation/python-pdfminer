%global	module	pdfminer
%global mod %(m=%{module}; echo ${m:0:1})

%global oname %{module}

%global cmapdir %(echo `rpm -qls ghostscript-common | grep CMap | awk '{print $2}'`)

Summary:	PDF parser and analyzer
Name:		python-%{module}
Version:	20220524
Release:	1
Group:		Development/Python
License:	MIT and Public Domain and APAFML and BSD and (ASL 2.0 and MIT)
URL:		https://github.com/pdfminer/pdfminer.six
#Source0:	https://github.com/pdfminer/pdfminer.six/archive/%{version}/%{oname}-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/%{mod}/%{module}.six/%{module}.six-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(wheel)

BuildArch:	noarch

%{?python_provide:%python_provide python3-%{oname}}

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
%{python3_sitelib}/%{module}
%{py_puresitedir}/%{module}.six-%{version}-py%{py_ver}.egg-info

#--------------------------------------------------------------------

%prep
%autosetup -n %{module}.six-%{version}

# TODO_ unbundle cmap data
#rm -vf cmaprsrc/* pdfminer/cmap/*

%build
#%%make_build cmap
%py_build

%install
%py_install

