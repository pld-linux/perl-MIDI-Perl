%define	pdir	MIDI
%define	pnam	Perl
%include	/usr/lib/rpm/macros.perl
Summary:	MIDI-Perl perl module
Summary(pl):	Modu� perla MIDI-Perl
Name:		perl-MIDI-Perl
Version:	0.79
Release:	5

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
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
