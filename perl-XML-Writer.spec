%include	/usr/lib/rpm/macros.perl
Summary:	XML-Writer perl module
Summary(pl):	Modu³ perla XML-Writer
Name:		perl-XML-Writer
Version:	0.4
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/XML-Writer-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML-Writer - module for writing XML documents.

%description -l pl
XML-Writer - modu³ do pisania dokumentów XML.

%prep
%setup -q -n XML-Writer-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/XML/Writer.pm
%{_mandir}/man3/*
