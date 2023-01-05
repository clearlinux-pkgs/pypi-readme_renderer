#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-readme_renderer
Version  : 37.3
Release  : 41
URL      : https://files.pythonhosted.org/packages/81/c3/d20152fcd1986117b898f66928938f329d0c91ddc47f081c58e64e0f51dc/readme_renderer-37.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/81/c3/d20152fcd1986117b898f66928938f329d0c91ddc47f081c58e64e0f51dc/readme_renderer-37.3.tar.gz
Summary  : readme_renderer is a library for rendering "readme" descriptions for Warehouse
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-readme_renderer-license = %{version}-%{release}
Requires: pypi-readme_renderer-python = %{version}-%{release}
Requires: pypi-readme_renderer-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(bleach)
BuildRequires : pypi(docutils)
BuildRequires : pypi(py)
BuildRequires : pypi(pygments)
BuildRequires : pypi(setuptools)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

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
Requires: pypi(bleach)
Requires: pypi(docutils)
Requires: pypi(pygments)

%description python3
python3 components for the pypi-readme_renderer package.


%prep
%setup -q -n readme_renderer-37.3
cd %{_builddir}/readme_renderer-37.3
pushd ..
cp -a readme_renderer-37.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1667331995
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
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
