import time
import os
import shutil
from tqdm import tqdm

start = time.time()

for fol in ["full_forg", "full_org"]:
    loc = ""
    if fol == "full_forg":
        loc = "forged"
    else:
        loc = "genuine"
    for root, dirs, files in os.walk("E:\\Tanweer Internships & Jobs\\Rashmi Sir\\CEDAR signatures\\" + fol):
        for file in tqdm(sorted(files), desc="PROCESSING : {}".format(fol)):
            if file == 'Thumbs.db':
                continue

            s = file.split("_")
            s = s[2].split(".")
            s = int(s[0])
            fp = os.path.join(root, file)
            fpnew = fp
            fpnew = fpnew.replace("CEDAR signatures", "CEDAR_split")

            if s >= 1 and s <= 19:
                fpnew = fpnew.replace(fol, "train\\" + loc)
            elif s >= 20 and s <= 23:
                fpnew = fpnew.replace(fol, "test\\" + loc)
            else:
                fpnew = fpnew.replace(fol, "val\\" + loc)

            shutil.copy2(fp, fpnew)

end = time.time()

print("FINISHED IN -> ", end-start, " seconds")
