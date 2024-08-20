# MenuTitle: Font and File name with timestamp
# -*- coding: utf-8 -*-
import datetime

def exportFontWithTimestamp():
    # Get the current font
    font = Glyphs.font
    
    # Get the current date and time
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    
    # Save the original family name
    originalFamilyName = font.familyName
    
    # Modify the family name
    font.familyName += f"_{timestamp}"
    
    # Define export path
    exportPath = "/Library/Application Support/Adobe/Fonts"
    
    try:
        # Generate each instance
        for instance in font.instances:
            # Define file path for each instance
            filePath = f"{exportPath}/{font.familyName}_{instance.name}.otf"
            
            # Generate the instance
            exportResult = instance.generate(FontPath=filePath, autoHint=False, Format="OTF")
            
            if exportResult == True:
                print(f"Instance {instance.name} exported successfully to {filePath}")
            else:
                print(f"Failed to export instance {instance.name}. Error: {exportResult}")
    finally:
        # Restore the original family name
        font.familyName = originalFamilyName

# Run the export function
exportFontWithTimestamp()

