from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

executables = [
    Executable('wbstools.py', 'Win32GUI')
]

setup(name='wbstools',
      version = '1.0',
      description = '',
      options = dict(build_exe = buildOptions),
      executables = executables)
