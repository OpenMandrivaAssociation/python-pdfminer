#!/bin/sh
py_module=pdfminer.six
curl https://pypi.org/project/${py_module}/ 2>/dev/null |grep -A1 "package-header__name" |sed -ne "s,.*${py_module} ,,p"


