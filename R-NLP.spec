#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: 5424026
#
Name     : R-NLP
Version  : 0.3.1
Release  : 51
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/NLP_0.3-1.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/NLP_0.3-1.tar.gz
Summary  : Natural Language Processing Infrastructure
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%prep
%setup -q -n NLP
pushd ..
cp -a NLP buildavx2
popd
pushd ..
cp -a NLP buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1731646758

%install
export SOURCE_DATE_EPOCH=1731646758
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/NLP/texts/spanish.conllu
/usr/lib64/R/library/NLP/texts/stanford.rds
