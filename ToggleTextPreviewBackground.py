#MenuTitle: Toggle Text Preview Background
# -*- coding: utf-8 -*-

#Thanks to Georg Seifert
# He wrote the prompt code in: https://forum.glyphsapp.com/t/change-background-color-in-text-preview/17085/9

from AppKit import NSAppearance

text_view = PreviewTextWindow.defaultInstance().textView()
current_appearance = text_view.appearance()

dark_appearance = NSAppearance.darkAppearance()
light_appearance = NSAppearance.lightAppearance()

if current_appearance == dark_appearance:
    # If current appearance is dark, switch to light
    text_view.setAppearance_(light_appearance)
else:
    # If current appearance is light, switch to dark
    text_view.setAppearance_(dark_appearance)
