%include	/usr/lib/rpm/macros.perl
%define	pdir	MIDI
%define	pnam	Perl
Summary:	MIDI::Perl perl module
Summary(pl):	Modu³ perla MIDI::Perl
Name:		perl-MIDI-Perl
Version:	0.79
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/MIDI.pm
%{perl_sitelib}/MIDI
%{_mandir}/man3/*
