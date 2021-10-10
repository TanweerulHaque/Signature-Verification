# forged - 30
# 21 8 1

# genuine - 24
# 17 6 1

import time
from pathlib import Path
import shutil

start = time.time()
rootdir = "E:\Tanweer Internships & Jobs\Rashmi Sir\BHSig260\Bengali"
for i in Path(rootdir).iterdir():
    if Path(i).is_dir():
        for k, p in enumerate(list(Path(i).iterdir())):
            if k < 21:
                dest = rootdir.replace(
                    "BHSig260\Bengali", "BengaliBHSig260split\\train\\forged")
                shutil.copy2(str(p), dest)
            elif k < 29:
                dest = rootdir.replace(
                    "BHSig260\Bengali", "BengaliBHSig260split\\test\\forged")
                shutil.copy2(str(p), dest)
            elif k < 30:
                dest = rootdir.replace(
                    "BHSig260\Bengali", "BengaliBHSig260split\\val\\forged")
                shutil.copy2(str(p), dest)
            elif k < 47:
                dest = rootdir.replace(
                    "BHSig260\Bengali", "BengaliBHSig260split\\train\\genuine")
                shutil.copy2(str(p), dest)
            elif k < 53:
                dest = rootdir.replace(
                    "BHSig260\Bengali", "BengaliBHSig260split\\test\\genuine")
                shutil.copy2(str(p), dest)
            elif k < 54:
                dest = rootdir.replace(
                    "BHSig260\Bengali", "BengaliBHSig260split\\val\\genuine")
                shutil.copy2(str(p), dest)


end = time.time()

print("FINISHED IN -> ", end-start, " seconds")
