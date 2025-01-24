# read version from installed package
from importlib.metadata import version
__version__ = version("myprojectpythonReda")
from myprojectpythonReda import main, run_app
