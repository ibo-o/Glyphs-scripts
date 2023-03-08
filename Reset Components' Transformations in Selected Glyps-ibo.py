#MenuTitle: Reset Components' Transformations in Selected Glyps
# -*- coding: utf-8 -*-
#This script resets the transformations of components in selected glyphs.
#Thanks to Florian Pircher
# He wrote this code in: https://forum.glyphsapp.com/t/is-there-a-way-to-reset-transformations-for-components/21496/5

for layer in Font.selectedLayers:
	for component in layer.components:
		component.transform = ((1, 0, 0, 1, 0, 0))