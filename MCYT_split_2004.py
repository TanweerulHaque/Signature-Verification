import time
import os
import shutil

start = time.time()

for root, dirs, files in os.walk("E:\\Tanweer Internships & Jobs\\Rashmi Sir\\2004_MCYTDB_OffLineSignSubCorpus"):
    for dir in dirs:
        fols = sorted(os.listdir(os.path.join(root, dir)))
        fol = [x for x in fols if x != 'Thumbs.db']
        for i, fp in enumerate(fol):
            filepath = os.path.join(root, dir, fp)
            if i < 11:
                shutil.copy2(filepath, os.path.join(
                    "E:\\Tanweer Internships & Jobs\\Rashmi Sir\\MCYT_2004_split\\train\\genuine", fp))
                continue
            elif i < 14:
                shutil.copy2(filepath, os.path.join(
                    "E:\\Tanweer Internships & Jobs\\Rashmi Sir\\MCYT_2004_split\\test\\genuine", fp))
                continue
            elif i < 15:
                shutil.copy2(filepath, os.path.join(
                    "E:\\Tanweer Internships & Jobs\\Rashmi Sir\\MCYT_2004_split\\val\\genuine", fp))
                continue
            elif i < 26:
                shutil.copy2(filepath, os.path.join(
                    "E:\\Tanweer Internships & Jobs\\Rashmi Sir\\MCYT_2004_split\\train\\forged", fp))
                continue
            elif i < 29:
                shutil.copy2(filepath, os.path.join(
                    "E:\\Tanweer Internships & Jobs\\Rashmi Sir\\MCYT_2004_split\\test\\forged", fp))
                continue
            elif i < 30:
                shutil.copy2(filepath, os.path.join(
                    "E:\\Tanweer Internships & Jobs\\Rashmi Sir\\MCYT_2004_split\\val\\forged", fp))
                continue

end = time.time()
print("FINISHED IN -> ", end-start, " seconds")
