#MenuTitle: Text Preview Light
# -*- coding: utf-8 -*-

#Thanks to Georg Seifert
# He wrote this code in: https://forum.glyphsapp.com/t/change-background-color-in-text-preview/17085/9
from AppKit import NSAppearance
PreviewTextWindow.defaultInstance().textView().setAppearance_(NSAppearance.lightAppearance())