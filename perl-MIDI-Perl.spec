%include	/usr/lib/rpm/macros.perl
Summary:	MIDI-Perl perl module
Summary(pl):	Modu³ perla MIDI-Perl
Name:		perl-MIDI-Perl
Version:	0.73
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/MIDI/MIDI-Perl-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
MIDI-Perl is a suite of Perl modules that allows you to read, compose, modify,
and write MIDI files.

%description -l pl
MIDI-Perl jest zestawem modu³ów umo¿liwiaj±cych czytanie, tworzenie, 
modyfikowanie i zapis plików MIDI.

%prep
%setup -q -n MIDI-Perl-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/MIDI-Perl
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/MIDI.pm
%{perl_sitelib}/MIDI
%{perl_sitearch}/auto/MIDI-Perl

%{_mandir}/man3/*
