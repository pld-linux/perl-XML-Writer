%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Writer
Summary:	XML::Writer perl module
Summary(pl):	Modu³ perla XML::Writer
Name:		perl-XML-Writer
Version:	0.4
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Writer - module for writing XML documents.

%description -l pl
XML::Writer - modu³ do pisania dokumentów XML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
