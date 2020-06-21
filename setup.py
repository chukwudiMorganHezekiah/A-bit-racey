
import cx_Freeze
from cx_Freeze import *
setup(
    name="A bit Racey",
    options={"build_exe" : {"packages":['pygame']}},
    executables=[
        Executable(
            "welcome.py"
        )
    ]
)