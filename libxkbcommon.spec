%global debug_package %{nil}

Name:           libxkbcommon
Version:        1.8.0
Release:        1%{?dist}
Summary:        Keymap handling library for xkb

License:        MIT
URL:            https://xkbcommon.org
Source0:        https://github.com/xkbcommon/libxkbcommon/archive/refs/tags/xkbcommon-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  bison
BuildRequires: pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(xcb)
BuildRequires: pkgconfig(libxml)

%description
xkbcommon is a keymap compiler and support library which processes
keyboard descriptions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%package        x11
Summary:        X11 support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    x11
X11 support library for %{name}.

%package        x11-devel
Summary:        Development files for X11 support of %{name}
Requires:       %{name}-x11%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    x11-devel
Development files for X11 support of %{name}.

%prep
%autosetup -n libxkbcommon-xkbcommon-%{version}

%build
%meson \
  -Denable-docs=false \

%meson_build

%install
%meson_install

%files
%license LICENSE
%{_libdir}/libxkbcommon.so.*
%{_libexecdir}/xkbcommon/

%files devel
%{_includedir}/xkbcommon/
%{_libdir}/libxkbcommon.so
%{_libdir}/pkgconfig/xkbcommon.pc

%files x11
%{_libdir}/libxkbcommon-x11.so.*

%files x11-devel
%{_libdir}/libxkbcommon-x11.so
%{_libdir}/pkgconfig/xkbcommon-x11.pc

%changelog
* Tue Aug 04 2026 Custom Maintainer - 1.8.0-1
- Update libxkbcommon for MangoWM stack
