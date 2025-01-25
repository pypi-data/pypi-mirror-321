# read version from installed package
from importlib.metadata import version
__version__ = version("myprojectpythonReda")
from myprojectpythonReda import main, run_app, compute_correlation_matrix
df_test = main()
run_app(df_test)