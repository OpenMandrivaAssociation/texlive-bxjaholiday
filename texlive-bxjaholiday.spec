Name:		texlive-bxjaholiday
Version:	60636
Release:	2
Summary:	Support for Japanese holidays
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bxjaholiday
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxjaholiday.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxjaholiday.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package provides a command to convert dates to names
of Japanese holidays. Another command, converting dates to the
day of the week in Japanese, is available as a free gift.
Further (lower-level) APIs are provided for expl3. The package
supports pdfTeX, XeTeX, LuaTeX, pTeX, and upTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bxjaholiday
%doc %{_texmfdistdir}/doc/latex/bxjaholiday

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
