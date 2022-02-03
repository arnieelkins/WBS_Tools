# -*- coding: utf-8 -*-

import dabo
from dabo.dApp import dApp
from dabo.dLocalize import _
import os

__version__ = "1.1.0.0"
class App(dApp):
    def initProperties(self):
    	# Manages how preferences are saved
    	self.BasePrefKey = "dabo.app.WBSTools"
    	self.setAppInfo("appShortName", "WBSTools")
    	self.setAppInfo("appName", "WBSTools")
    	self.setAppInfo("copyright", "(c) 2013-2022")
    	self.setAppInfo("companyName", "Monrovia Church of Christ")
    	self.setAppInfo("companyAddress1", "595 Nance Road")
    	self.setAppInfo("companyAddress2", "Madison, AL 35757")
    	self.setAppInfo("companyPhone", "256.837.5255")
    	self.setAppInfo("companyEmail", "wbs@monrovia.org")
    	self.setAppInfo("companyUrl", "http://monrovia.org")

    	self.setAppInfo("appDescription", _("Tools for grading World Bible School lessons and recording \
    										student information in a MySQL database"))

    	## Information about the developer of the software:
    	self.setAppInfo("authorName", "Arnie Elkins")
    	self.setAppInfo("authorEmail", "arnie.elkins@gmail.com")

    	## Set app version information:
    	self.setAppInfo("appVersion", __version__)
    	self.CryptoKey = "WeHoldTheseTruths"
    	registerFonts("")
    	self.Icon = "icons/wbs.ico"

    def setup(self):
    	if dabo.MDI:
    		#self.MainFormClass = dabo.ui.createForm("ui/StudentsForm.cdxml")
    		self.MainFormClass = dabo.ui.dFormMain
    	else:
    		# no need for main form in SDI mode
    		self.MainFormClass = None
    	super(App, self).setup()


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
 
 
