Name:		texlive-gitinfo2
Version:	38913
Release:	1
Summary:	Access metadata from the git distributed version control system
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gitinfo2
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gitinfo2.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gitinfo2.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package makes it possible to incorporate git version
control metadata into documents. For memoir users, the package
provides the means to tailor page headers and footers to use
the metadata. gitinfo2 is a new release of gitinfo. The changes
to version 2 are not backward-compatible, and the package name
has been changed to avoid impact on existing users'
repositories. All new repositories should use this version of
the package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/gitinfo2
%doc %{_texmfdistdir}/doc/latex/gitinfo2

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
