%include	/usr/lib/rpm/macros.perl
%define	pdir	MIDI
%define	pnam	Perl
Summary:	MIDI::Perl perl module
Summary(pl):	Modu³ perla MIDI::Perl
Name:		perl-MIDI-Perl
Version:	0.8
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
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

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/MIDI.pm
%{perl_vendorlib}/MIDI
%{_mandir}/man3/*
