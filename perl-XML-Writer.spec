%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Writer
Summary:	XML::Writer perl module
Summary(pl):	Modu³ perla XML::Writer
Name:		perl-XML-Writer
Version:	0.4
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5: d07811beb3329ef6bbe7f50b52d242dd
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Writer - module for writing XML documents.

%description -l pl
XML::Writer - modu³ do pisania dokumentów XML.

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
%doc Changes README
%{perl_vendorlib}/XML/Writer.pm
%{_mandir}/man3/*
