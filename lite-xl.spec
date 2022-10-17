%global         realname lite
%global         build_timestamp %{lua: print(os.date("%Y%m%d"))}

Name:           %{realname}-xl-nightly
Version:        nightly
Release:        %{build_timestamp}%{?dist}
Summary:        A lightweight text editor written in Lua

License:        MIT
URL:            https://github.com/franko/lite-xl
Source0:        https://github.com/lite-xl/lite-xl/archive/refs/heads/master.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  libX11-devel
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(lua)
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

Conflicts:      %{realname}-xl
Conflicts:      %{realname}

%description
lite is a lightweight text editor written mostly in Lua
it aims to provide something practical, pretty, small
and fast, implemented as simply as possible; easy to
modify and extend, or to use without doing either.

%prep
%autosetup -n %{realname}-xl-master

%build
meson _build
ninja -C _build/

%install
export DESTDIR=%{buildroot}
ninja -C _build/ install

%files
%{_bindir}/lite-xl
%{_datadir}/lite-xl/
%{_datadir}/applications/org.lite_xl.lite_xl.desktop
%{_datadir}/metainfo/org.lite_xl.lite_xl.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/lite-xl.svg
%{_docdir}/lite-xl/

%license LICENSE
