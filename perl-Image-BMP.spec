#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Image
%define	pnam	BMP
Summary:	Image::BMP - Bitmap parser/viewer
#Summary(pl.UTF-8):	
Name:		perl-Image-BMP
Version:	1.16
Release:	1
# same as perl (REMOVE THIS LINE IF NOT TRUE)
#License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Image/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	89a00446b270f7a49c71c8aa3a3e06a7
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/Image-BMP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Image::BMP objects can parse and even ascii view bitmaps of the
.BMP format.  It can read most of the common forms of this format.

It can be used to:

It does not currently write bmap data, simply because I didn't
have a use for that yet.  Convince me and I'll add it.



# %description -l pl.UTF-8
# TODO

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
%doc INSTALL README
%{perl_vendorlib}/Image/*.pm
%{perl_vendorlib}/Image/BMP
%{_mandir}/man3/*
