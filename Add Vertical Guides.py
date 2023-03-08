#MenuTitle: Vertical Guides for Each Node
# -*- coding: utf-8 -*-
__doc__="""
Adding vertical guides separately for each selected nodes
"""
#thanks to alexs on Glyphs app Forum https://forum.glyphsapp.com/t/add-guides-for-each-selected-nodes/24805/2

font = Glyphs.font
selectedLayer = font.selectedLayers[0]

for node in selectedLayer.selection: 
	guideLine = GSGuide()
	guideLine.position = node.position
	guideLine.angle = 90
	selectedLayer.guides.append(guideLine)