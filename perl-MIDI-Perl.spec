%include	/usr/lib/rpm/macros.perl
Summary:	MIDI-Perl perl module
Summary(pl):	Modu� perla MIDI-Perl
Name:		perl-MIDI-Perl
Version:	0.79
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/MIDI/MIDI-Perl-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIDI-Perl is a suite of Perl modules that allows you to read, compose,
modify, and write MIDI files.

%description -l pl
MIDI-Perl jest zestawem modu��w umo�liwiaj�cych czytanie, tworzenie,
modyfikowanie i zapis plik�w MIDI.

%prep
%setup -q -n MIDI-Perl-%{version}

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
