%global tl_name gitinfo2
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0.7
Release:	%{tl_revision}.1
Summary:	Access metadata from the git distributed version control system
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gitinfo2
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gitinfo2.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gitinfo2.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package makes it possible to incorporate git version control
metadata into documents. For memoir users, the package provides the
means to tailor page headers and footers to use the metadata. gitinfo2
is a new release of gitinfo. The changes to version 2 are not backward-
compatible, and the package name has been changed to avoid impact on
existing users' repositories. All new repositories should use this
version of the package.

