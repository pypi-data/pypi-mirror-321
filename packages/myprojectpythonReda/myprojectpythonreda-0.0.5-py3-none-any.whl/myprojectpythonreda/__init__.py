# read version from installed package
from importlib.metadata import version
__version__ = version("myprojectpythonReda")
from myprojectpythonReda import main, run_app


if __name__ == "__main__":
    # Exécutez la logique principale une seule fois
    df_test = main()
    print(df_test)
    # Lancer l'application Dash avec les données générées
    if df_test is not None:
        run_app(df_test)
    else:
        print("No valid data available to run the Dash app.")