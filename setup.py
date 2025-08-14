from cx_Freeze import setup, Executable

setup(
    name="YourAppName",
    version="AppVersion",
    description="AppDescription",
    executables=[Executable("main.py")]
)
