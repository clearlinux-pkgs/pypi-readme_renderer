#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-readme_renderer
Version  : 42.0
Release  : 44
URL      : https://files.pythonhosted.org/packages/b5/35/1cb5a6a97514812f63c06df6c2855d82ebed3e5c02e9d536a78669854c8a/readme_renderer-42.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b5/35/1cb5a6a97514812f63c06df6c2855d82ebed3e5c02e9d536a78669854c8a/readme_renderer-42.0.tar.gz
Summary  : readme_renderer is a library for rendering readme descriptions for Warehouse
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-readme_renderer-license = %{version}-%{release}
Requires: pypi-readme_renderer-python = %{version}-%{release}
Requires: pypi-readme_renderer-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Readme Renderer
===============
.. image:: https://badge.fury.io/py/readme-renderer.svg
:target: https://badge.fury.io/py/readme-renderer

%package license
Summary: license components for the pypi-readme_renderer package.
Group: Default

%description license
license components for the pypi-readme_renderer package.


%package python
Summary: python components for the pypi-readme_renderer package.
Group: Default
Requires: pypi-readme_renderer-python3 = %{version}-%{release}

%description python
python components for the pypi-readme_renderer package.


%package python3
Summary: python3 components for the pypi-readme_renderer package.
Group: Default
Requires: python3-core
Provides: pypi(readme_renderer)
Requires: pypi(docutils)
Requires: pypi(nh3)
Requires: pypi(pygments)

%description python3
python3 components for the pypi-readme_renderer package.


%prep
%setup -q -n readme_renderer-42.0
cd %{_builddir}/readme_renderer-42.0
pushd ..
cp -a readme_renderer-42.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1694446492
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-readme_renderer
cp %{_builddir}/readme_renderer-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-readme_renderer/43a3a49bd7af636c923a5ae475395b8e29320529 || :
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-readme_renderer/43a3a49bd7af636c923a5ae475395b8e29320529

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
