#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MIDI
%define		pnam	Perl
Summary:	MIDI::Perl perl module
Summary(pl):	Modu³ perla MIDI::Perl
Name:		perl-MIDI-Perl
Version:	0.8
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5d2c37e1263e4b8dd9b468e094c1afcb
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIDI::Perl is a suite of Perl modules that allows you to read, compose,
modify, and write MIDI files.

%description -l pl
MIDI::Perl jest zestawem modu³ów umo¿liwiaj±cych czytanie, tworzenie,
modyfikowanie i zapis plików MIDI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# get rid of pod documentation
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/MIDI/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/MIDI.pm
%{perl_vendorlib}/MIDI
%{_mandir}/man3/*
