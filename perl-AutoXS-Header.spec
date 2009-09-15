#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	AutoXS
%define	pnam	Header
Summary:	AutoXS::Header - Container for the AutoXS header files
Summary(pl.UTF-8):	AutoXS::Header - pojemnik na pliki nagłówkowe AutoXS
Name:		perl-AutoXS-Header
Version:	1.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/S/SM/SMUELLER/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bfed85ce503f6a2222b6ddd5cf7c41bc
URL:		http://search.cpan.org/dist/AutoXS-Header/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a simple container for the newest version of the AutoXS
header file AutoXS.h.

%description -l pl.UTF-8
Moduł ten jest prostym pojemnikiem na najnowsze wersje plików
nagłówkowych AutoXS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/AutoXS/*.pm
%{_mandir}/man3/*
