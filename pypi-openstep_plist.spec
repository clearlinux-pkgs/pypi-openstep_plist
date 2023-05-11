#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-openstep_plist
Version  : 0.3.0.post1
Release  : 1
URL      : https://files.pythonhosted.org/packages/8b/91/93e85357548eb41a699854d8ac6054c7c0736d73999dd2708bd3257a4acf/openstep_plist-0.3.0.post1.zip
Source0  : https://files.pythonhosted.org/packages/8b/91/93e85357548eb41a699854d8ac6054c7c0736d73999dd2708bd3257a4acf/openstep_plist-0.3.0.post1.zip
Summary  : ASCII plist parser written in Cython
Group    : Development/Tools
License  : MIT
Requires: pypi-openstep_plist-python = %{version}-%{release}
Requires: pypi-openstep_plist-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cython)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![Github CI Status](https://github.com/fonttools/openstep-plist/workflows/Wheels/badge.svg)](https://github.com/fonttools/openstep-plist/actions?query=workflow%3A%22Wheels%22)
[![codecov](https://codecov.io/gh/fonttools/openstep-plist/branch/master/graph/badge.svg)](https://codecov.io/gh/fonttools/openstep-plist)
[![PyPI](https://img.shields.io/pypi/v/openstep-plist.svg)](https://pypi.org/project/openstep-plist/)

%package python
Summary: python components for the pypi-openstep_plist package.
Group: Default
Requires: pypi-openstep_plist-python3 = %{version}-%{release}

%description python
python components for the pypi-openstep_plist package.


%package python3
Summary: python3 components for the pypi-openstep_plist package.
Group: Default
Requires: python3-core
Provides: pypi(openstep_plist)

%description python3
python3 components for the pypi-openstep_plist package.


%prep
%setup -q -n openstep_plist-0.3.0.post1
cd %{_builddir}/openstep_plist-0.3.0.post1
pushd ..
cp -a openstep_plist-0.3.0.post1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683819241
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
