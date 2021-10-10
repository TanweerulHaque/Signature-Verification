from pathlib import Path

rootdir = r"E:\Tanweer Internships & Jobs\Rashmi Sir\Raw datasets\BHSig260\Bengali"
for i in Path(rootdir).iterdir():
    if Path(i).is_dir():
        print(str(i.relative_to(rootdir)))
