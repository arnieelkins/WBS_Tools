from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('WBSTools.py', base=base)
]

setup(name='WBSTools',
      version = '0.9.2.2',
      description = 'Tools for grading World Bible School lessons and tracking student information',
      options = dict(build_exe = buildOptions),
      executables = executables)
