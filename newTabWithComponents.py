#MenuTitle: New Tab with Components
# -*- coding: utf-8 -*-
__doc__="""
Opens the selected glyphs containing components in a new tab
"""


# Get the current font
font = Glyphs.font

# Get selected glyphs
selected_glyphs = font.selection

# Create a new edit tab
tab = font.newTab()

# List to store selected glyphs with components
selected_glyphs_with_components = []

# Iterate through selected glyphs
for glyph in selected_glyphs:
    if glyph.layers[0].components:  # Check if the glyph has components
        selected_glyphs_with_components.append(glyph)

# Add selected glyphs with components to the tab selection
tab.layers = selected_glyphs_with_components

# Print the number of glyphs in the new tab
num_glyphs_in_tab = len(selected_glyphs_with_components)
print("The amount of glyphs with components:", num_glyphs_in_tab)
