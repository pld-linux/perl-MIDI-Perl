#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	MIDI
%define		pnam	Perl
%include	/usr/lib/rpm/macros.perl
Summary:	MIDI::Perl perl module
Summary(pl.UTF-8):	Moduł perla MIDI::Perl
Name:		perl-MIDI-Perl
Version:	0.82
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a4f1c45483b460b4059664cde8636de1
URL:		http://search.cpan.org/dist/MIDI-Perl/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIDI::Perl is a suite of Perl modules that allows you to read,
compose, modify, and write MIDI files.

%description -l pl.UTF-8
MIDI::Perl jest zestawem modułów umożliwiających czytanie, tworzenie,
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
