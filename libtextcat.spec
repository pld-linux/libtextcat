Summary:	Text Categorization Library
Name:		libtextcat
Version:	2.2
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://software.wise-guys.nl/download/%{name}-%{version}.tar.gz
# Source0-md5:	128cfc86ed5953e57fe0f5ae98b62c2e
Source1:	http://hg.services.openoffice.org/hg/DEV300/raw-file/tip/libtextcat/data/new_fingerprints/fpdb.conf
# Source1-md5:	f4fafe97d3aa184f5476e4918dba045d
Source2:	http://hg.services.openoffice.org/hg/DEV300/raw-file/tip/libtextcat/data/new_fingerprints/lm/chinese_simplified.lm
# Source2-md5:	aaecf093c984cc018584eb4e55babc1d
Source3:	http://hg.services.openoffice.org/hg/DEV300/raw-file/tip/libtextcat/data/new_fingerprints/lm/chinese_traditional.lm
# Source3-md5:	39ab7bcfb0d71e01dfcf919cbd2a7dac
Source4:	http://hg.services.openoffice.org/hg/DEV300/raw-file/tip/libtextcat/data/new_fingerprints/lm/japanese.lm
# Source4-md5:	630cdcaf85638804ca0e04530f3ac6b6
Source5:	http://hg.services.openoffice.org/hg/DEV300/raw-file/tip/libtextcat/data/new_fingerprints/lm/luxembourgish.lm
# Source5-md5:	239df8a8b283b9f9503758852cace61f
Source6:	http://hg.services.openoffice.org/hg/DEV300/raw-file/tip/libtextcat/data/new_fingerprints/lm/mongolian_cyrillic.lm
# Source6-md5:	72bd27a60a4db478f3162eb4da387252
Source7:	http://hg.services.openoffice.org/hg/DEV300/raw-file/tip/libtextcat/data/new_fingerprints/lm/zulu.lm
# Source7-md5:	c8ce1e0b3e965aa2bd9e96ebc34c60fc
URL:		http://software.wise-guys.nl/libtextcat/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	libtool
#wrap headers in extern "C" for use with C++ and split common.h into multilib headers
Patch0:		%{name}-2.2-exportapi.patch
#make libtextcat utf8 aware for use with OOo
#See http://www.mail-archive.com/dev@lingucomponent.openoffice.org/msg00912.html
#and http://hg.services.openoffice.org/hg/DEV300/raw-file/tip/libtextcat/libtextcat-2.2.patch
Patch1:		%{name}-2.2-OOo.patch

%description
Libtextcat is a library with functions that implement the
classification technique described in Cavnar & Trenkle, "N-Gram-Based
Text Categorization". It was primarily developed for language
guessing, a task on which it is known to perform with near-perfect
accuracy.

%package devel
Summary:	Support files necessary to compile applications with libtextcat
Group:		Development/Libraries
Requires:	libtextcat = %{version}-%{release}

%description devel
Libraries, headers, and support files necessary to compile
applications using libtextcat.

%prep
%setup -q
%patch0 -p1 -b .exportapi.patch
%patch1 -p1 -b .ooo.patch

%build
autoreconf -f -i
%configure \
	--disable-static \

%{__make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
install -d $RPM_BUILD_ROOT/%{_datadir}/libtextcat
cp -p %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/libtextcat
cd langclass/LM
cp -p amharic-utf.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/amharic_utf.lm
cp -p yiddish-utf.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/yiddish_utf.lm
cp -p afrikaans.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/afrikaans.lm
cp -p basque.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/basque.lm
cp -p bosnian.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/bosnian.lm
cp -p croatian-ascii.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/croatian.lm
cp -p dutch.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/dutch.lm
cp -p english.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/english.lm
cp -p icelandic.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/icelandic.lm
cp -p indonesian.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/indonesian.lm
cp -p latin.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/latin.lm
cp -p malay.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/malay.lm
cp -p manx.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/manx_gaelic.lm
cp -p marathi.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/marathi.lm
cp -p nepali.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/nepali.lm
cp -p romanian.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/romanian.lm
cp -p sanskrit.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/sanskrit.lm
cp -p scots.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/scots.lm
cp -p serbian-ascii.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/serbian_ascii.lm
cp -p slovak-ascii.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/slovak_ascii.lm
cp -p swahili.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/swahili.lm
cp -p tagalog.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/tagalog.lm
cp -p welsh.lm $RPM_BUILD_ROOT/%{_datadir}/libtextcat/welsh.lm
iconv -f WINDOWS-1256 -t UTF-8 arabic-windows1256.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/arabic.lm
iconv -f ISO-8859-1 -t UTF-8 albanian.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/albanian.lm
iconv -f WINDOWS-1251 -t UTF-8 belarus-windows1251.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/belarus.lm
iconv -f ISO-8859-1 -t UTF-8 breton.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/breton.lm
iconv -f ISO-8859-1 -t UTF-8 catalan.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/catalan.lm
iconv -f ISO-8859-2 -t UTF-8 czech-iso8859_2.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/czech.lm
iconv -f ISO-8859-1 -t UTF-8 danish.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/danish.lm
iconv -f ISO-8859-3 -t UTF-8 esperanto.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/esperanto.lm
iconv -f ISO-8859-15 -t UTF-8 estonian.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/estonian.lm
iconv -f ISO-8859-1 -t UTF-8 finnish.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/finnish.lm
iconv -f ISO-8859-1 -t UTF-8 french.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/french.lm
iconv -f ISO-8859-1 -t UTF-8 frisian.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/frisian.lm
iconv -f ISO-8859-1 -t UTF-8 georgian.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/georgian.lm
iconv -f ISO-8859-1 -t UTF-8 german.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/german.lm
iconv -f ISO-8859-7 -t UTF-8 greek-iso8859-7.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/greek.lm
iconv -f ISO-8859-8 -t UTF-8 hebrew-iso8859_8.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/hebrew.lm
iconv -f ISO-8859-2 -t UTF-8 hungarian.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/hungarian.lm
iconv -f ISO-8859-1 -t UTF-8 irish.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/irish_gaelic.lm
iconv -f ISO-8859-1 -t UTF-8 italian.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/italian.lm
iconv -f ISO-8859-13 -t UTF-8 latvian.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/latvian.lm
iconv -f ISO-8859-13 -t UTF-8 lithuanian.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/lithuanian.lm
iconv -f ISO-8859-1 -t UTF-8 malay.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/malay.lm
iconv -f ISO-8859-1 -t UTF-8 middle_frisian.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/middle_frisian.lm
iconv -f ISO-8859-1 -t UTF-8 mingo.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/mingo.lm
iconv -f ISO-8859-1 -t UTF-8 norwegian.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/norwegian.lm
iconv -f ISO-8859-2 -t UTF-8 polish.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/polish.lm
iconv -f ISO-8859-1 -t UTF-8 portuguese.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/portuguese.lm
iconv -f ISO-8859-1 -t UTF-8 quechua.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/quechua.lm
iconv -f ISO-8859-1 -t UTF-8 rumantsch.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/romansh.lm
iconv -f ISO-8859-5 -t UTF-8 russian-iso8859_5.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/russian.lm
iconv -f ISO-8859-1 -t UTF-8 scots_gaelic.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/scots_gaelic.lm
iconv -f ISO-8859-2 -t UTF-8 slovenian-iso8859_2.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/slovenian.lm
iconv -f ISO-8859-1 -t UTF-8 spanish.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/spanish.lm
iconv -f ISO-8859-1 -t UTF-8 swedish.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/swedish.lm
iconv -f ISO-8859-9 -t UTF-8 turkish.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/turkish.lm
iconv -f KOI8-R -t UTF-8 ukrainian-koi8_r.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/ukrainian.lm
#these look wrong to me, but that's what upstream OOo has done, raise this upstream
iconv -f ISO-8859-1 -t UTF-8 hindi.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/hindi.lm
iconv -f ISO-8859-1 -t UTF-8 persian.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/persian.lm
iconv -f ISO-8859-1 -t UTF-8 korean.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/korean.lm
iconv -f ISO-8859-1 -t UTF-8 tamil.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/tamil.lm
iconv -f ISO-8859-1 -t UTF-8 thai.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/thai.lm
iconv -f ISO-8859-1 -t UTF-8 vietnamese.lm > $RPM_BUILD_ROOT/%{_datadir}/libtextcat/vietnamese.lm
#and I have no idea how they fixed the encoding of these ones
cp -p %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/libtextcat/chinese_simplified.lm
cp -p %{SOURCE3} $RPM_BUILD_ROOT/%{_datadir}/libtextcat/chinese_traditional.lm
cp -p %{SOURCE4} $RPM_BUILD_ROOT/%{_datadir}/libtextcat/japanese.lm
cp -p %{SOURCE5} $RPM_BUILD_ROOT/%{_datadir}/libtextcat/luxembourgish.lm
cp -p %{SOURCE6} $RPM_BUILD_ROOT/%{_datadir}/libtextcat/mongolian_cyrillic.lm
cp -p %{SOURCE7} $RPM_BUILD_ROOT/%{_datadir}/libtextcat/zulu.lm

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README LICENSE TODO
%attr(755,root,root) %{_libdir}/lib*.so.*
%{_datadir}/libtextcat

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/createfp
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/%{name}

%clean
rm -r $RPM_BUILD_ROOT
