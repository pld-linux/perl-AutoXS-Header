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
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/S/SM/SMUELLER/%{pdir}-%{pnam}-%{version}.tar.gz
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
Moduł ten jest prostym pojemnikiem na najnowszą wersję pliku
nagłówkowego AutoXS o nazwie AutoXS.h.

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
%dir %{perl_vendorlib}/AutoXS
%{perl_vendorlib}/AutoXS/Header.pm
%{_mandir}/man3/AutoXS::Header.3pm*
