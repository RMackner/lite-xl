Name:           lite-xl
Version:        2.0.5
Release:        %autorelease
Summary:        A lightweight text editor written in Lua, adapted from lite.
License:        MIT
URL:            https://github.com/lite-xl/lite-xl
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Conflicts:      lite-xl

Requires: lua
Requires: pcre2
Requires: freetype
Requires: libxkbcommon

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  git
BuildRequires:  scdoc
BuildRequires:  lua-devel
BuildRequires:  pcre2-devel
BuildRequires:  lua-libs
BuildRequires:  lua

%description
%{summary}

%prep
%setup

%build
meson _build
ninja -C _build/

%install
export DESTDIR=%{buildroot}
ninja -C _build/ install

%files


%changelog
%autochangelog
