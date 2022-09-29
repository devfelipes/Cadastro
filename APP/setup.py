import sys
from cx_Freeze import setup, Executable


# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os",'janela','conexao','logs'], "includes": ["datetime","win32com.client","tkinter","sqlite3"], "include_files":['ico.ico']}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="CADASTRO",
    version="1.0",
    description="Banco de Dados!",
    options={"build_exe": build_exe_options},
    executables=[Executable("janela.py", base=base, icon='ico.ico')]
)