from __future__ import annotations

try:
    from .uiev import *

except Exception as e:
    import Cython, setuptools, platform, subprocess, os, sys, time

    iswindows = "win" in platform.platform().lower()
    olddict = os.getcwd()
    dirname = os.path.dirname(__file__)
    os.chdir(dirname)
    compile_file = os.path.join(dirname, "uiev_compile.py")
    cmd2execute = " ".join([sys.executable, compile_file, "build_ext", "--inplace"])
    if iswindows:
        subprocess.run(
            cmd2execute,
            shell=True,
            env=os.environ,
        )
    else:
        os.system(cmd2execute)
    os.chdir(olddict)
    from .uiev import *
