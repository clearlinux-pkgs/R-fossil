#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fossil
Version  : 0.3.7
Release  : 17
URL      : https://cran.r-project.org/src/contrib/fossil_0.3.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fossil_0.3.7.tar.gz
Summary  : Palaeoecological and Palaeogeographical Analysis Tools
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-maps
Requires: R-shapefiles
Requires: R-sp
BuildRequires : R-maps
BuildRequires : R-shapefiles
BuildRequires : R-sp
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
and geographical data sets, both ancient and modern. The
        package includes functions for estimating species richness
        (Chao 1 and 2, ACE, ICE, Jacknife), shared species/beta
        diversity, species area curves and geographic distances and
        areas.

%prep
%setup -q -c -n fossil

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571833161

%install
export SOURCE_DATE_EPOCH=1571833161
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fossil
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fossil
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fossil
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc fossil || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fossil/CITATION
/usr/lib64/R/library/fossil/DESCRIPTION
/usr/lib64/R/library/fossil/INDEX
/usr/lib64/R/library/fossil/Meta/Rd.rds
/usr/lib64/R/library/fossil/Meta/data.rds
/usr/lib64/R/library/fossil/Meta/features.rds
/usr/lib64/R/library/fossil/Meta/hsearch.rds
/usr/lib64/R/library/fossil/Meta/links.rds
/usr/lib64/R/library/fossil/Meta/nsInfo.rds
/usr/lib64/R/library/fossil/Meta/package.rds
/usr/lib64/R/library/fossil/NAMESPACE
/usr/lib64/R/library/fossil/R/fossil
/usr/lib64/R/library/fossil/R/fossil.rdb
/usr/lib64/R/library/fossil/R/fossil.rdx
/usr/lib64/R/library/fossil/data/fdata.lats.rda
/usr/lib64/R/library/fossil/data/fdata.list.rda
/usr/lib64/R/library/fossil/data/fdata.mat.rda
/usr/lib64/R/library/fossil/help/AnIndex
/usr/lib64/R/library/fossil/help/aliases.rds
/usr/lib64/R/library/fossil/help/fossil.rdb
/usr/lib64/R/library/fossil/help/fossil.rdx
/usr/lib64/R/library/fossil/help/paths.rds
/usr/lib64/R/library/fossil/html/00Index.html
/usr/lib64/R/library/fossil/html/R.css
