from cx_Freeze import  setup, Executable

executables = [Executable("main.py")]

setup(

    name="Deserto dos Monstros",
    version="1.0",
    description="Desert Monsters app",
    options={"build_exe": {"packages": ["pygame"]}},
    executables=executables
)