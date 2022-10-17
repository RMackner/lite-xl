Name:           lite-xl
Version:        2.0.5
Release:        %autorelease
Summary:        A lightweight text editor written in Lua, adapted from lite.
License:        MIT
URL:            https://github.com/lite-xl/lite-xl
Source0:        https://github.com/RMackner/lite-xl/releases/download/test/2.0.5.tar.gz
Conflicts:      lite-xl

Requires: lua
Requires: pcre2
Requires: freetype

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  git
BuildRequires:  scdoc
BuildRequires:  lua-devel
BuildRequires:  pcre2-devel
BuildRequires:  lua-libs
BuildRequires:  SDL2-devel
BuildRequires:  freetype
BuildRequires:  freetype-devel

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
   /usr/lib/debug/usr/local/bin/lite-xl-2.0.5-1.fc36.x86_64.debug
   /usr/local/bin/lite-xl
   /usr/local/include/agg2/Makefile.am
   /usr/local/include/agg2/agg_alpha_mask_u8.h
   /usr/local/include/agg2/agg_arc.h
   /usr/local/include/agg2/agg_array.h
   /usr/local/include/agg2/agg_arrowhead.h
   /usr/local/include/agg2/agg_basics.h
   /usr/local/include/agg2/agg_bezier_arc.h
   /usr/local/include/agg2/agg_bitset_iterator.h
   /usr/local/include/agg2/agg_blur.h
   /usr/local/include/agg2/agg_bounding_rect.h
   /usr/local/include/agg2/agg_bspline.h
   /usr/local/include/agg2/agg_clip_liang_barsky.h
   /usr/local/include/agg2/agg_color_gray.h
   /usr/local/include/agg2/agg_color_rgba.h
   /usr/local/include/agg2/agg_config.h
   /usr/local/include/agg2/agg_conv_adaptor_vcgen.h
   /usr/local/include/agg2/agg_conv_adaptor_vpgen.h
   /usr/local/include/agg2/agg_conv_bspline.h
   /usr/local/include/agg2/agg_conv_clip_polygon.h
   /usr/local/include/agg2/agg_conv_clip_polyline.h
   /usr/local/include/agg2/agg_conv_close_polygon.h
   /usr/local/include/agg2/agg_conv_concat.h
   /usr/local/include/agg2/agg_conv_contour.h
   /usr/local/include/agg2/agg_conv_curve.h
   /usr/local/include/agg2/agg_conv_dash.h
   /usr/local/include/agg2/agg_conv_gpc.h
   /usr/local/include/agg2/agg_conv_marker.h
   /usr/local/include/agg2/agg_conv_marker_adaptor.h
   /usr/local/include/agg2/agg_conv_segmentator.h
   /usr/local/include/agg2/agg_conv_shorten_path.h
   /usr/local/include/agg2/agg_conv_smooth_poly1.h
   /usr/local/include/agg2/agg_conv_stroke.h
   /usr/local/include/agg2/agg_conv_transform.h
   /usr/local/include/agg2/agg_conv_unclose_polygon.h
   /usr/local/include/agg2/agg_curves.h
   /usr/local/include/agg2/agg_dda_line.h
   /usr/local/include/agg2/agg_ellipse.h
   /usr/local/include/agg2/agg_ellipse_bresenham.h
   /usr/local/include/agg2/agg_embedded_raster_fonts.h
   /usr/local/include/agg2/agg_font_cache_manager.h
   /usr/local/include/agg2/agg_gamma_functions.h
   /usr/local/include/agg2/agg_gamma_lut.h
   /usr/local/include/agg2/agg_glyph_raster_bin.h
   /usr/local/include/agg2/agg_gradient_lut.h
   /usr/local/include/agg2/agg_gsv_text.h
   /usr/local/include/agg2/agg_image_accessors.h
   /usr/local/include/agg2/agg_image_filters.h
   /usr/local/include/agg2/agg_line_aa_basics.h
   /usr/local/include/agg2/agg_math.h
   /usr/local/include/agg2/agg_math_stroke.h
   /usr/local/include/agg2/agg_path_length.h
   /usr/local/include/agg2/agg_path_storage.h
   /usr/local/include/agg2/agg_path_storage_integer.h
   /usr/local/include/agg2/agg_pattern_filters_rgba.h
   /usr/local/include/agg2/agg_pixfmt_amask_adaptor.h
   /usr/local/include/agg2/agg_pixfmt_gray.h
   /usr/local/include/agg2/agg_pixfmt_rgb.h
   /usr/local/include/agg2/agg_pixfmt_rgb_packed.h
   /usr/local/include/agg2/agg_pixfmt_rgba.h
   /usr/local/include/agg2/agg_pixfmt_transposer.h
   /usr/local/include/agg2/agg_rasterizer_cells_aa.h
   /usr/local/include/agg2/agg_rasterizer_compound_aa.h
   /usr/local/include/agg2/agg_rasterizer_outline.h
   /usr/local/include/agg2/agg_rasterizer_outline_aa.h
   /usr/local/include/agg2/agg_rasterizer_scanline_aa.h
   /usr/local/include/agg2/agg_rasterizer_sl_clip.h
   /usr/local/include/agg2/agg_renderer_base.h
   /usr/local/include/agg2/agg_renderer_markers.h
   /usr/local/include/agg2/agg_renderer_mclip.h
   /usr/local/include/agg2/agg_renderer_outline_aa.h
   /usr/local/include/agg2/agg_renderer_outline_image.h
   /usr/local/include/agg2/agg_renderer_primitives.h
   /usr/local/include/agg2/agg_renderer_raster_text.h
   /usr/local/include/agg2/agg_renderer_scanline.h
   /usr/local/include/agg2/agg_rendering_buffer.h
   /usr/local/include/agg2/agg_rendering_buffer_dynarow.h
   /usr/local/include/agg2/agg_rounded_rect.h
   /usr/local/include/agg2/agg_scanline_bin.h
   /usr/local/include/agg2/agg_scanline_boolean_algebra.h
   /usr/local/include/agg2/agg_scanline_p.h
   /usr/local/include/agg2/agg_scanline_storage_aa.h
   /usr/local/include/agg2/agg_scanline_storage_bin.h
   /usr/local/include/agg2/agg_scanline_u.h
   /usr/local/include/agg2/agg_shorten_path.h
   /usr/local/include/agg2/agg_simul_eq.h
   /usr/local/include/agg2/agg_span_allocator.h
   /usr/local/include/agg2/agg_span_converter.h
   /usr/local/include/agg2/agg_span_gouraud.h
   /usr/local/include/agg2/agg_span_gouraud_gray.h
   /usr/local/include/agg2/agg_span_gouraud_rgba.h
   /usr/local/include/agg2/agg_span_gradient.h
   /usr/local/include/agg2/agg_span_gradient_alpha.h
   /usr/local/include/agg2/agg_span_image_filter.h
   /usr/local/include/agg2/agg_span_image_filter_gray.h
   /usr/local/include/agg2/agg_span_image_filter_rgb.h
   /usr/local/include/agg2/agg_span_image_filter_rgba.h
   /usr/local/include/agg2/agg_span_interpolator_adaptor.h
   /usr/local/include/agg2/agg_span_interpolator_linear.h
   /usr/local/include/agg2/agg_span_interpolator_persp.h
   /usr/local/include/agg2/agg_span_interpolator_trans.h
   /usr/local/include/agg2/agg_span_pattern_gray.h
   /usr/local/include/agg2/agg_span_pattern_rgb.h
   /usr/local/include/agg2/agg_span_pattern_rgba.h
   /usr/local/include/agg2/agg_span_solid.h
   /usr/local/include/agg2/agg_span_subdiv_adaptor.h
   /usr/local/include/agg2/agg_trans_affine.h
   /usr/local/include/agg2/agg_trans_bilinear.h
   /usr/local/include/agg2/agg_trans_double_path.h
   /usr/local/include/agg2/agg_trans_perspective.h
   /usr/local/include/agg2/agg_trans_single_path.h
   /usr/local/include/agg2/agg_trans_viewport.h
   /usr/local/include/agg2/agg_trans_warp_magnifier.h
   /usr/local/include/agg2/agg_vcgen_bspline.h
   /usr/local/include/agg2/agg_vcgen_contour.h
   /usr/local/include/agg2/agg_vcgen_dash.h
   /usr/local/include/agg2/agg_vcgen_markers_term.h
   /usr/local/include/agg2/agg_vcgen_smooth_poly1.h
   /usr/local/include/agg2/agg_vcgen_stroke.h
   /usr/local/include/agg2/agg_vcgen_vertex_sequence.h
   /usr/local/include/agg2/agg_vertex_sequence.h
   /usr/local/include/agg2/agg_vpgen_clip_polygon.h
   /usr/local/include/agg2/agg_vpgen_clip_polyline.h
   /usr/local/include/agg2/agg_vpgen_segmentator.h
   /usr/local/include/agg2/ctrl/Makefile.am
   /usr/local/include/agg2/ctrl/agg_bezier_ctrl.h
   /usr/local/include/agg2/ctrl/agg_cbox_ctrl.h
   /usr/local/include/agg2/ctrl/agg_ctrl.h
   /usr/local/include/agg2/ctrl/agg_gamma_ctrl.h
   /usr/local/include/agg2/ctrl/agg_gamma_spline.h
   /usr/local/include/agg2/ctrl/agg_polygon_ctrl.h
   /usr/local/include/agg2/ctrl/agg_rbox_ctrl.h
   /usr/local/include/agg2/ctrl/agg_scale_ctrl.h
   /usr/local/include/agg2/ctrl/agg_slider_ctrl.h
   /usr/local/include/agg2/ctrl/agg_spline_ctrl.h
   /usr/local/include/agg2/platform/Makefile.am
   /usr/local/include/agg2/platform/agg_platform_support.h
   /usr/local/include/agg2/platform/mac/agg_mac_pmap.h
   /usr/local/include/agg2/platform/win32/agg_win32_bmp.h
   /usr/local/include/agg2/util/Makefile.am
   /usr/local/include/agg2/util/agg_color_conv.h
   /usr/local/include/agg2/util/agg_color_conv_rgb16.h
   /usr/local/include/agg2/util/agg_color_conv_rgb8.h
   /usr/local/include/lauxlib.h
   /usr/local/include/lua.h
   /usr/local/include/lua.hpp
   /usr/local/include/luaconf.h
   /usr/local/include/lualib.h
   /usr/local/include/reproc/drain.h
   /usr/local/include/reproc/export.h
   /usr/local/include/reproc/reproc.h
   /usr/local/include/reproc/run.h
   /usr/local/lib64/libagg.a
   /usr/local/lib64/libaggplatform.a
   /usr/local/lib64/liblua.a
   /usr/local/lib64/libreproc.a
   /usr/local/lib64/pkgconfig/libagg.pc
   /usr/local/lib64/pkgconfig/libaggplatform.pc
   /usr/local/lib64/pkgconfig/lua5.2.pc
   /usr/local/lib64/pkgconfig/reproc.pc
   /usr/local/share/applications/org.lite_xl.lite_xl.desktop
   /usr/local/share/doc/lite-xl/licenses.md
   /usr/local/share/icons/hicolor/scalable/apps/lite-xl.svg
   /usr/local/share/lite-xl/colors/fall.lua
   /usr/local/share/lite-xl/colors/gruvbox-dark.lua
   /usr/local/share/lite-xl/colors/gruvbox-light.lua
   /usr/local/share/lite-xl/colors/summer.lua
   /usr/local/share/lite-xl/colors/textadept.lua
   /usr/local/share/lite-xl/core/command.lua
   /usr/local/share/lite-xl/core/commands/command.lua
   /usr/local/share/lite-xl/core/commands/core.lua
   /usr/local/share/lite-xl/core/commands/dialog.lua
   /usr/local/share/lite-xl/core/commands/doc.lua
   /usr/local/share/lite-xl/core/commands/drawwhitespace.lua
   /usr/local/share/lite-xl/core/commands/files.lua
   /usr/local/share/lite-xl/core/commands/findreplace.lua
   /usr/local/share/lite-xl/core/commands/root.lua
   /usr/local/share/lite-xl/core/commandview.lua
   /usr/local/share/lite-xl/core/common.lua
   /usr/local/share/lite-xl/core/config.lua
   /usr/local/share/lite-xl/core/contextmenu.lua
   /usr/local/share/lite-xl/core/doc/highlighter.lua
   /usr/local/share/lite-xl/core/doc/init.lua
   /usr/local/share/lite-xl/core/doc/search.lua
   /usr/local/share/lite-xl/core/doc/translate.lua
   /usr/local/share/lite-xl/core/docview.lua
   /usr/local/share/lite-xl/core/init.lua
   /usr/local/share/lite-xl/core/keymap-macos.lua
   /usr/local/share/lite-xl/core/keymap.lua
   /usr/local/share/lite-xl/core/logview.lua
   /usr/local/share/lite-xl/core/modkeys-generic.lua
   /usr/local/share/lite-xl/core/modkeys-macos.lua
   /usr/local/share/lite-xl/core/nagview.lua
   /usr/local/share/lite-xl/core/object.lua
   /usr/local/share/lite-xl/core/regex.lua
   /usr/local/share/lite-xl/core/rootview.lua
   /usr/local/share/lite-xl/core/start.lua
   /usr/local/share/lite-xl/core/statusview.lua
   /usr/local/share/lite-xl/core/strict.lua
   /usr/local/share/lite-xl/core/style.lua
   /usr/local/share/lite-xl/core/syntax.lua
   /usr/local/share/lite-xl/core/titleview.lua
   /usr/local/share/lite-xl/core/tokenizer.lua
   /usr/local/share/lite-xl/core/view.lua
   /usr/local/share/lite-xl/fonts/FiraSans-Regular.ttf
   /usr/local/share/lite-xl/fonts/JetBrainsMono-Regular.ttf
   /usr/local/share/lite-xl/fonts/icons.ttf
   /usr/local/share/lite-xl/plugins/autocomplete.lua
   /usr/local/share/lite-xl/plugins/autoreload.lua
   /usr/local/share/lite-xl/plugins/contextmenu.lua
   /usr/local/share/lite-xl/plugins/detectindent.lua
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
   /usr/local/share/metainfo/org.lite_xl.lite_xl.appdata.xml


%changelog
%autochangelog
