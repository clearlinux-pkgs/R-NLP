#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-NLP
Version  : 0.2.0
Release  : 17
URL      : https://cran.r-project.org/src/contrib/NLP_0.2-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/NLP_0.2-0.tar.gz
Summary  : Natural Language Processing Infrastructure
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n NLP

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552932772

%install
export SOURCE_DATE_EPOCH=1552932772
rm -rf %{buildroot}
export LANG=C
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library NLP
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library NLP
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library NLP
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  NLP || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/NLP/DESCRIPTION
/usr/lib64/R/library/NLP/INDEX
/usr/lib64/R/library/NLP/Meta/Rd.rds
/usr/lib64/R/library/NLP/Meta/features.rds
/usr/lib64/R/library/NLP/Meta/hsearch.rds
/usr/lib64/R/library/NLP/Meta/links.rds
/usr/lib64/R/library/NLP/Meta/nsInfo.rds
/usr/lib64/R/library/NLP/Meta/package.rds
/usr/lib64/R/library/NLP/NAMESPACE
/usr/lib64/R/library/NLP/R/NLP
/usr/lib64/R/library/NLP/R/NLP.rdb
/usr/lib64/R/library/NLP/R/NLP.rdx
/usr/lib64/R/library/NLP/R/sysdata.rdb
/usr/lib64/R/library/NLP/R/sysdata.rdx
/usr/lib64/R/library/NLP/help/AnIndex
/usr/lib64/R/library/NLP/help/NLP.rdb
/usr/lib64/R/library/NLP/help/NLP.rdx
/usr/lib64/R/library/NLP/help/aliases.rds
/usr/lib64/R/library/NLP/help/paths.rds
/usr/lib64/R/library/NLP/html/00Index.html
/usr/lib64/R/library/NLP/html/R.css
/usr/lib64/R/library/NLP/po/en@quot/LC_MESSAGES/R-NLP.mo
/usr/lib64/R/library/NLP/texts/stanford.rds
