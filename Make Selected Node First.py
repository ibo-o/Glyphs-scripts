# MenuTitle: Make Selected Node First
# -*- coding: utf-8 -*-

__doc__ = """
Makes Selected nodes first on the path.
"""

Font = Glyphs.font

# Run
Font.disableUpdateInterface()

for layer in Font.selectedLayers:
    if layer.selection:
        for node in layer.selection:
            node.makeNodeFirst()
    else:
        print("nothing selected")
            
Font.enableUpdateInterface()