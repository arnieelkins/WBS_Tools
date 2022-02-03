import os
import reportlab.rl_config
 
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
 
def registerFonts(homedir):
    font_mappings = []
    for fname in os.listdir(os.path.join(homedir, "resources")):
        psname, ext = os.path.splitext(fname)
        if ext == ".ttf":
            name = psname
            name_lower = name.lower()
            pdfmetrics.registerFont(TTFont(psname,
                    os.path.join(homedir, "resources", fname)))
            try:
                idx = name_lower.index("oblique")
                italic = True
                name = name[:idx] + name[idx+len("oblique"):]
                name_lower = name.lower()
            except ValueError:
                italic = False
 
            if not italic:
                try:
                    idx = name_lower.index("italic")
                    italic = True
                    name = name[:idx] + name[idx+len("italic"):]
                    name_lower = name.lower()
                except ValueError:
                    italic = False
 
            try:
                idx = name_lower.index("bold")
                bold = True
                name = name[:idx] + name[idx+len("bold"):]
            except ValueError:
                bold = False
 
            name = name.replace("-", "").lower()
            font_mappings.append((name, bold, italic, psname))
 
    for font_mapping in sorted(font_mappings):
        addMapping(*font_mapping)
        print font_mapping
 
 
if __name__ == "__main__":
    registerFonts(".")