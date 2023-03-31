%define major 2
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	A clean C library for processing UTF-8 Unicode data
Name:		utf8proc
Version:	2.6.1
Release:	2
Group:		System/Libraries
License:	MIT
Url:		https://julialang.org/%{name}/
Source0:	https://github.com/JuliaStrings/utf8proc/archive/%{name}-%{version}.tar.gz

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
%doc LICENSE.md
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/libutf8proc.pc

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%make_build CFLAGS="%{optflags}"

%install
%makeinstall_std  prefix=%{_prefix} includedir=%{_includedir} libdir=%{_libdir}
rm %{buildroot}%{_libdir}/libutf8proc.a

%check
%make CFLAGS="%{optflags}" test
