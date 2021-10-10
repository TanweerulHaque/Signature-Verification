import cv2
import numpy as np
from pathlib import Path
from tqdm import tqdm
import time
import shutil

print("starting")
start = time.time()
print("creating folders")

root = r"E:\Tanweer Internships & Jobs\Rashmi Sir\Raw datasets\BengaliBHSig260splitsomerandom"
for t in ["test", "train", "val"]:
    for g in ["forged", "genuine"]:
        Path(root).joinpath(t, g).mkdir(parents=True, exist_ok=True)

print("created folders")


rootdir = r"E:\Tanweer Internships & Jobs\Rashmi Sir\Raw datasets\BHSig260\Bengali"
for i in tqdm(list(Path(rootdir).iterdir())):
    if Path(i).is_dir():
        a = list(Path(i).iterdir())
        first = a[:30]
        second = a[30:]
        checklist = ["011", "012", "013", "014", "078", "082",
                     "016", "017", "019", "023", "025", "027",
                     "037", "038", "044", "049", "006", "071",
                     "099", "010", "015", "022", "067", "077"]
        if str(i.relative_to(rootdir)) in checklist:
            np.random.shuffle(first)
            np.random.shuffle(second)

        for k, p in enumerate(first):
            if k < 21:
                dest = rootdir.replace(
                    r"BHSig260\Bengali", "BengaliBHSig260splitsomerandom\\train\\forged")
                shutil.copy2(str(p), dest)
            elif k < 29:
                dest = rootdir.replace(
                    r"BHSig260\Bengali", "BengaliBHSig260splitsomerandom\\test\\forged")
                shutil.copy2(str(p), dest)
            elif k < 30:
                dest = rootdir.replace(
                    r"BHSig260\Bengali", "BengaliBHSig260splitsomerandom\\val\\forged")
                shutil.copy2(str(p), dest)

        for k, p in enumerate(second):
            if k < 17:
                dest = rootdir.replace(
                    r"BHSig260\Bengali", "BengaliBHSig260splitsomerandom\\train\\genuine")
                shutil.copy2(str(p), dest)
            elif k < 23:
                dest = rootdir.replace(
                    r"BHSig260\Bengali", "BengaliBHSig260splitsomerandom\\test\\genuine")
                shutil.copy2(str(p), dest)
            elif k < 24:
                dest = rootdir.replace(
                    r"BHSig260\Bengali", "BengaliBHSig260splitsomerandom\\val\\genuine")
                shutil.copy2(str(p), dest)

print("creating folders")

root = r"E:\Tanweer Internships & Jobs\Rashmi Sir\Raw datasets\BengaliBHSig260splitsomerandomcropped"
for t in ["test", "train", "val"]:
    for g in ["forged", "genuine"]:
        Path(root).joinpath(t, g).mkdir(parents=True, exist_ok=True)

print("created folders")

res_height = []
res_width = []

total_dirs = [
    r"E:\Tanweer Internships & Jobs\Rashmi Sir\Raw datasets\BengaliBHSig260splitsomerandom\test\forged",
    r"E:\Tanweer Internships & Jobs\Rashmi Sir\Raw datasets\BengaliBHSig260splitsomerandom\test\genuine",
    r"E:\Tanweer Internships & Jobs\Rashmi Sir\Raw datasets\BengaliBHSig260splitsomerandom\train\forged",
    r"E:\Tanweer Internships & Jobs\Rashmi Sir\Raw datasets\BengaliBHSig260splitsomerandom\train\genuine",
    r"E:\Tanweer Internships & Jobs\Rashmi Sir\Raw datasets\BengaliBHSig260splitsomerandom\val\forged",
    r"E:\Tanweer Internships & Jobs\Rashmi Sir\Raw datasets\BengaliBHSig260splitsomerandom\val\genuine"]

for p in tqdm(total_dirs):
    for z in Path(p).iterdir():
        image = cv2.imread(str(z))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        points = np.argwhere(binary == 0)
        lowest_x = 100000
        lowest_y = 100000
        max_x = -100000
        max_y = -100000

        for i in points:
            if i[0] < lowest_x:
                lowest_x = i[0]
                cor_lowest_x = i
            if i[1] < lowest_y:
                lowest_y = i[1]
                cor_lowest_y = i
            if i[0] > max_x:
                max_x = i[0]
                cor_max_x = i
            if i[1] > max_y:
                max_y = i[1]
                cor_max_y = i
        newimg = binary[lowest_x:max_x, lowest_y:max_y]
        res_height.append(
            ((binary.shape[0]-newimg.shape[0])/(binary.shape[0]))*100)
        res_width.append(
            ((binary.shape[1]-newimg.shape[1])/(binary.shape[1]))*100)
        newpath = str(z).replace("BengaliBHSig260splitsomerandom",
                                 "BengaliBHSig260splitsomerandomcropped")
        cv2.imwrite(newpath, newimg)

print("Average Height Decrease -> ", np.mean(res_height), " %")
print("Average Width Decrease -> ", np.mean(res_width), " %")

end = time.time()
print("FINISHED IN -> ", end-start, " seconds")
print("ended")
