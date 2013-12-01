import os
import glob
import dabo
import dabo.icons

daboDir = os.path.split(dabo.__file__)[0]

# Find the location of the dabo icons:
iconDir = os.path.split(dabo.icons.__file__)[0]
iconSubDirs = []
def getIconSubDir(arg, dirname, fnames):
	if ".svn" not in dirname and "cards" not in dirname.lower() and dirname[-1] != "\\":
		icons = glob.glob(os.path.join(dirname, "*.png"))
		if icons:
			subdir = (os.path.join("resources", dirname[len(arg)+1:]), icons)
			iconSubDirs.append(subdir)
os.path.walk(iconDir, getIconSubDir, iconDir)

# locales:
localeDir = "%s%slocale" % (daboDir, os.sep)
#locales = [("dabo.locale", (os.path.join(daboDir, "locale", "dabo.pot"),))]
locales = []
def getLocales(arg, dirname, fnames):
	if ".svn" not in dirname and dirname[-1] != "\\":
		#po_files = tuple(glob.glob(os.path.join(dirname, "*.po")))
		mo_files = tuple(glob.glob(os.path.join(dirname, "*.mo")))
		if mo_files:
			subdir = os.path.join("dabo.locale", dirname[len(arg)+1:])
			locales.append((subdir, mo_files))
os.path.walk(localeDir, getLocales, localeDir)



def getVersionTuple(ss_version):
	l = [int(i) for i in ss_version.split(".")] + [0]
	return tuple(l)