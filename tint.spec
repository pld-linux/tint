#
Summary:	Alter photos by selectively choosing tints
Name:		tint
Version:	1.0.1
Release:	1
License:	BSD
Group:		Applications
Source0:	http://www.indii.org/files/tint/releases/%{name}-%{version}.tar.gz
# Source0-md5:	36dbab3a0540014b49b771af8db25837
Patch0:		%{name}-wxgtk.patch
URL:		http://www.indii.org/software/tint/
BuildRequires:	boost-uBLAS-devel
BuildRequires:	scons
BuildRequires:	wxGTK2-unicode-devel >= 2.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tint is a photo editor for colour-select effects. It automatically
clusters the colours of a photo into groups, and allows each colour to
be switched on or off to create the desired effect.

%prep
%setup -q
%patch0 -p1

%build
scons

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install tint $RPM_BUILD_ROOT%{_bindir}/tint


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt VERSION.txt
%attr(755,root,root) %{_bindir}/*
