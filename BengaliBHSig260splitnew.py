import cv2
import numpy as np
from pathlib import Path
from tqdm import tqdm

res_height = []
res_width = []

total_dirs = [
    r"E:\Tanweer Internships & Jobs\Rashmi Sir\Processed datasets\BengaliBHSig260split\test\forged",
    r"E:\Tanweer Internships & Jobs\Rashmi Sir\Processed datasets\BengaliBHSig260split\test\genuine",
    r"E:\Tanweer Internships & Jobs\Rashmi Sir\Processed datasets\BengaliBHSig260split\train\forged",
    r"E:\Tanweer Internships & Jobs\Rashmi Sir\Processed datasets\BengaliBHSig260split\train\genuine",
    r"E:\Tanweer Internships & Jobs\Rashmi Sir\Processed datasets\BengaliBHSig260split\val\forged",
    r"E:\Tanweer Internships & Jobs\Rashmi Sir\Processed datasets\BengaliBHSig260split\val\genuine"]

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
        newpath = str(z).replace("BengaliBHSig260split",
                                 "BengaliBHSig260splitnew")
        cv2.imwrite(newpath, newimg)

print("Average Height Decrease = ", np.mean(res_height), " %")
print("Average Width Decrease = ", np.mean(res_width), " %")
