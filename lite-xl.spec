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
   /usr/lib/debug/usr/local/bin/lite-xl-nightly-20221017.fc3*
   /usr/local/bin/lite-xl
   /usr/local/share/applications/org.lite_xl.lite_xl.desktop
   /usr/local/share/doc/lite-xl/licenses.md
   /usr/local/share/icons/hicolor/scalable/apps/lite-xl.svg
   /usr/local/share/lite-xl/colors/default.lua
   /usr/local/share/lite-xl/colors/fall.lua
   /usr/local/share/lite-xl/colors/summer.lua
   /usr/local/share/lite-xl/colors/textadept.lua
   /usr/local/share/lite-xl/core/bit.lua
   /usr/local/share/lite-xl/core/command.lua
   /usr/local/share/lite-xl/core/commands/command.lua
   /usr/local/share/lite-xl/core/commands/core.lua
   /usr/local/share/lite-xl/core/commands/dialog.lua
   /usr/local/share/lite-xl/core/commands/doc.lua
   /usr/local/share/lite-xl/core/commands/drawwhitespace.lua
   /usr/local/share/lite-xl/core/commands/files.lua
   /usr/local/share/lite-xl/core/commands/findreplace.lua
   /usr/local/share/lite-xl/core/commands/log.lua
   /usr/local/share/lite-xl/core/commands/root.lua
   /usr/local/share/lite-xl/core/commands/statusbar.lua
   /usr/local/share/lite-xl/core/commandview.lua
   /usr/local/share/lite-xl/core/common.lua
   /usr/local/share/lite-xl/core/config.lua
   /usr/local/share/lite-xl/core/contextmenu.lua
   /usr/local/share/lite-xl/core/dirwatch.lua
   /usr/local/share/lite-xl/core/doc/highlighter.lua
   /usr/local/share/lite-xl/core/doc/init.lua
   /usr/local/share/lite-xl/core/doc/search.lua
   /usr/local/share/lite-xl/core/doc/translate.lua
   /usr/local/share/lite-xl/core/docview.lua
   /usr/local/share/lite-xl/core/emptyview.lua
   /usr/local/share/lite-xl/core/ime.lua
   /usr/local/share/lite-xl/core/init.lua
   /usr/local/share/lite-xl/core/keymap-macos.lua
   /usr/local/share/lite-xl/core/keymap.lua
   /usr/local/share/lite-xl/core/logview.lua
   /usr/local/share/lite-xl/core/modkeys-generic.lua
   /usr/local/share/lite-xl/core/modkeys-macos.lua
   /usr/local/share/lite-xl/core/nagview.lua
   /usr/local/share/lite-xl/core/node.lua
   /usr/local/share/lite-xl/core/object.lua
   /usr/local/share/lite-xl/core/regex.lua
   /usr/local/share/lite-xl/core/rootview.lua
   /usr/local/share/lite-xl/core/scrollbar.lua
   /usr/local/share/lite-xl/core/start.lua
   /usr/local/share/lite-xl/core/statusview.lua
   /usr/local/share/lite-xl/core/strict.lua
   /usr/local/share/lite-xl/core/style.lua
   /usr/local/share/lite-xl/core/syntax.lua
   /usr/local/share/lite-xl/core/titleview.lua
   /usr/local/share/lite-xl/core/tokenizer.lua
   /usr/local/share/lite-xl/core/utf8string.lua
   /usr/local/share/lite-xl/core/view.lua
   /usr/local/share/lite-xl/fonts/FiraSans-Regular.ttf
   /usr/local/share/lite-xl/fonts/JetBrainsMono-Regular.ttf
   /usr/local/share/lite-xl/fonts/icons.ttf
   /usr/local/share/lite-xl/globals.lua
   /usr/local/share/lite-xl/plugins/autocomplete.lua
   /usr/local/share/lite-xl/plugins/autoreload.lua
   /usr/local/share/lite-xl/plugins/contextmenu.lua
   /usr/local/share/lite-xl/plugins/detectindent.lua
   /usr/local/share/lite-xl/plugins/drawwhitespace.lua
   /usr/local/share/lite-xl/plugins/language_c.lua
   /usr/local/share/lite-xl/plugins/language_cpp.lua
   /usr/local/share/lite-xl/plugins/language_css.lua
   /usr/local/share/lite-xl/plugins/language_html.lua
   /usr/local/share/lite-xl/plugins/language_js.lua
   /usr/local/share/lite-xl/plugins/language_lua.lua
   /usr/local/share/lite-xl/plugins/language_md.lua
   /usr/local/share/lite-xl/plugins/language_python.lua
   /usr/local/share/lite-xl/plugins/language_xml.lua
   /usr/local/share/lite-xl/plugins/lineguide.lua
   /usr/local/share/lite-xl/plugins/linewrapping.lua
   /usr/local/share/lite-xl/plugins/macro.lua
   /usr/local/share/lite-xl/plugins/projectsearch.lua
   /usr/local/share/lite-xl/plugins/quote.lua
   /usr/local/share/lite-xl/plugins/reflow.lua
   /usr/local/share/lite-xl/plugins/scale.lua
   /usr/local/share/lite-xl/plugins/tabularize.lua
   /usr/local/share/lite-xl/plugins/toolbarview.lua
   /usr/local/share/lite-xl/plugins/treeview.lua
   /usr/local/share/lite-xl/plugins/trimwhitespace.lua
   /usr/local/share/lite-xl/plugins/workspace.lua
   /usr/local/share/lite-xl/process.lua
   /usr/local/share/lite-xl/regex.lua
   /usr/local/share/lite-xl/renderer.lua
   /usr/local/share/lite-xl/string.lua
   /usr/local/share/lite-xl/system.lua
   /usr/local/share/lite-xl/utf8extra.lua
   /usr/local/share/metainfo/org.lite_xl.lite_xl.appdata.xml


%license LICENSE
