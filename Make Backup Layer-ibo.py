#MenuTitle: Make Backup Layer-ibo
# encoding: utf-8

# by Tim Ahrens
# I just customised the layer name to add "ibrahim"
# http://justanotherfoundry.com
# https://github.com/justanotherfoundry/glyphsapp-scripts

__doc__="""
Same as the “+” button on the Layers palette.

I wrote this script mostly because it allows me to assign a keyboard shortcut. Also, it correctly copies brace layers, unlike Glyphs’ built-in function.
"""

GSLayer.isBraceLayer = property(lambda self: bool(self.pyobjc_instanceMethods.isBraceLayer()),
								lambda self, value: self.setBraceLayer_(value) )

import datetime

for layer in Glyphs.font.selectedLayers:
	glyph = layer.parent
	newLayer = layer.copy()
	if newLayer.isBraceLayer:
		newLayer.name = newLayer.name + datetime.datetime.now().strftime( "ibrahim %b %-d %y, %H:%M" )
		newLayer.isBraceLayer = False
	else:
		newLayer.name = datetime.datetime.now().strftime( "ibrahim %b %-d %y, %H:%M" )
	glyph.layers.append( newLayer )
