#MenuTitle: Remove Backup Layers for Selected Master
# encoding: utf-8

# 30.08.23 Modified to work on only selected masters. 

# Originally by Tim Ahrens
# http://justanotherfoundry.com
# https://github.com/justanotherfoundry/glyphsapp-scripts

from __future__ import division, print_function, unicode_literals

__doc__='''
Removes all backup layers (i.e. those created using the "Copy" button) from the selected glyphs in the currently selected master.

'''

import re

font = Glyphs.currentDocument.font
selected_glyphs = set([layer.parent for layer in font.selectedLayers])
selected_master = font.selectedFontMaster

for glyph in selected_glyphs:
    associated_layers = [layer.layerId for layer in glyph.layers if layer.layerId != layer.associatedMasterId and (not layer.name or not re.search(r"(\{[^a-zA-Z]+\})|([\[\]][^a-zA-Z]+\])", layer.name))]
    for layerId in associated_layers:
        if glyph.layers[layerId].associatedMasterId == selected_master.id:
            print('deleting extra layer from', glyph.name)
            del glyph.layers[layerId]
