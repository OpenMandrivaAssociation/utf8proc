%define major	2
%define minor	2
%define mini	0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

Summary:	A clean C library for processing UTF-8 Unicode data
Name:		utf8proc
Version:	2.3.0
Release:	1
Group:		System/Libraries
License:	MIT
Url:		https://julialang.org/%{name}/
Source0:	https://github.com/JuliaLang/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake

%description
utf8proc is a small, clean C library that provides Unicode normalization,
case-folding, and other operations for data in the UTF-8 encoding,
supporting Unicode version 9.0. It was initially developed by Jan Behrens
and the rest of the Public Software Group. With the blessing of the Public
Software Group, the Julia developers have taken over development of
utf8proc, since the original developers have moved to other projects.

utf8proc is used for basic Unicode support in the Julia language, and the
Julia developers became involved because they wanted to add Unicode 7
support and other features.

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library plugin handling
Group:		System/Libraries

%description -n %{libname}
utf8proc is a small, clean C library that provides Unicode normalization,
case-folding, and other operations for data in the UTF-8 encoding,
supporting Unicode version 9.0. It was initially developed by Jan Behrens
and the rest of the Public Software Group. With the blessing of the Public
Software Group, the Julia developers have taken over development of
utf8proc, since the original developers have moved to other projects.

utf8proc is used for basic Unicode support in the Julia language, and the
Julia developers became involved because they wanted to add Unicode 7
support and other features.

%files -n %{libname}
%doc LICENSE.md NEWS.md README.md
%{_libdir}/lib%{name}.so.%{major}*

#---------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package provides the header files, link libraries, and documentation for
building applications that use %{name}.

%files -n %{devname}
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%doc LICENSE.md

#---------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

# Do not ues Makefile provides with the package
rm  -f Makefile

%build
%cmake
%make CFLAGS="%{optflags}"

%install
#% makeinstall_std -C build

# library
install -dm 0755 %{buildroot}%{_libdir}/
install -pm 0755 build/lib%{name}.so.%{major}.%{minor}.%{mini} %{buildroot}%{_libdir}/
ln -s lib%{name}.so.%{major}.%{minor}.%{mini} %{buildroot}%{_libdir}/lib%{name}.so.%{major}
ln -s lib%{name}.so.%{major}.%{minor}.%{mini} %{buildroot}%{_libdir}/lib%{name}.so

# header
install -dm 0755 %{buildroot}%{_includedir}/
install -pm 0755 %{name}.h %{buildroot}%{_includedir}/

%check
%make CFLAGS="%{optflags}" test
