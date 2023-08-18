#MenuTitle: Toggle Color Labels
# -*- coding: utf-8 -*-

#Thanks to Georg Seifert
# He wrote the code in: https://forum.glyphsapp.com/t/feature-request-hide-show-color-labels/21398/2
if Glyphs.defaults["GSFontViewDrawLabelColor"] == True:
		Glyphs.defaults["GSFontViewDrawLabelColor"] = False
else:
		Glyphs.defaults["GSFontViewDrawLabelColor"] = True