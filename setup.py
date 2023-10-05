import sys
from cx_Freeze import setup, Executable

# Create an Executable instance
executables = [Executable("main.py", base = "Win32GUI")]

build_options = {
    "packages": ["pygame"], 
    "include_files": ["assets/"],
}

# Set up the setup function
setup(
    name="Snake",
    version="1.0",
    description="Python Snake Game",
    options={"build_exe": build_options},
    executables=executables
)
