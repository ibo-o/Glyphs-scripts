#MenuTitle: Clear Selected Glyphs in Current Master

# -*- coding: utf-8 -*-

__doc__=""" Removes all elements from selected glyph in current master."""

#thanks to HugoJ and justinpenner https://forum.glyphsapp.com/t/clear-selected-glyphs-in-current-master/24942


font = Glyphs.font
selectedMaster = font.selectedFontMaster

for glyph in font.glyphs:
	if glyph.selected:
		glyph.layers[selectedMaster.id].clear()
