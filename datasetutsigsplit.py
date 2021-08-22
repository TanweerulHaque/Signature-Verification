# -*- coding: utf-8 -*-
import os
import shutil


def main():
    for root, dirs, files in os.walk("C:\\Users\\Tanweer\\Downloads\\UTSigSplit\\UTSig\\Forgery\\Simple"):
        for dir in dirs:
            for i, fp in enumerate(sorted(os.listdir(os.path.join(root, dir)))):
                filepath = os.path.join(root, dir, fp)
                fp = "s" + fp
                filepath2 = os.path.join(
                    root, dir, fp).replace("Simple", "Skilled")
                shutil.move(filepath, filepath2)

    for root, dirs, files in os.walk("C:\\Users\\Tanweer\\Downloads\\UTSigSplit\\UTSig\\Forgery\\Opposite Hand"):
        for dir in dirs:
            for i, fp in enumerate(sorted(os.listdir(os.path.join(root, dir)))):
                filepath = os.path.join(root, dir, fp)
                fp = "oh" + fp
                filepath2 = os.path.join(root, dir, fp).replace(
                    "Opposite Hand", "Skilled")
                shutil.move(filepath, filepath2)

    count = 0
    for root, dirs, files in os.walk("C:\\Users\\Tanweer\\Downloads\\UTSigSplit\\UTSig\\Forgery\\Skilled"):
        for dir in dirs:
            fol = sorted(os.listdir(os.path.join(root, dir)))
            for i, fp in enumerate(fol):
                count += 1
                filepath = os.path.join(root, dir, fp)
                fp = str(count) + "ab" + fp
                if i < 3:
                    shutil.move(filepath, os.path.join(
                        "C:\\Users\\Tanweer\\Downloads\\UTSigSplit\\UTSig_updated\\train\\FORGED", fp))
                    continue
                if i < 5:
                    shutil.move(filepath, os.path.join(
                        "C:\\Users\\Tanweer\\Downloads\\UTSigSplit\\UTSig_updated\\test\\FORGED", fp))
                    continue
                if i < 6:
                    shutil.move(filepath, os.path.join(
                        "C:\\Users\\Tanweer\\Downloads\\UTSigSplit\\UTSig_updated\\val\\FORGED", fp))
                    continue
                if i < 7:
                    shutil.move(filepath, os.path.join(
                        "C:\\Users\\Tanweer\\Downloads\\UTSigSplit\\UTSig_updated\\train\\FORGED", fp))
                    continue
                if i < 8:
                    shutil.move(filepath, os.path.join(
                        "C:\\Users\\Tanweer\\Downloads\\UTSigSplit\\UTSig_updated\\test\\FORGED", fp))
                    continue
                if i < 9:
                    shutil.move(filepath, os.path.join(
                        "C:\\Users\\Tanweer\\Downloads\\UTSigSplit\\UTSig_updated\\val\\FORGED", fp))
                    continue
                if i < 35:
                    shutil.move(filepath, os.path.join(
                        "C:\\Users\\Tanweer\\Downloads\\UTSigSplit\\UTSig_updated\\train\\FORGED", fp))
                    continue
                if i < 44:
                    shutil.move(filepath, os.path.join(
                        "C:\\Users\\Tanweer\\Downloads\\UTSigSplit\\UTSig_updated\\test\\FORGED", fp))
                    continue
                if i < 45:
                    shutil.move(filepath, os.path.join(
                        "C:\\Users\\Tanweer\\Downloads\\UTSigSplit\\UTSig_updated\\val\\FORGED", fp))
                    continue
    print("Done")

    countx = 0
    for root, dirs, files in os.walk("C:\\Users\\Tanweer\\Downloads\\UTSigSplit\\UTSig\\Genuine"):
        for dir in dirs:
            fol = sorted(os.listdir(os.path.join(root, dir)))
            for i, fp in enumerate(fol):
                countx += 1
                filepath = os.path.join(root, dir, fp)
                fp1 = str(countx) + "pq" + fp
                if i < 16:
                    shutil.move(filepath, os.path.join(
                        "C:\\Users\\Tanweer\\Downloads\\UTSigSplit\\UTSig_updated\\train\\GENUINE", fp1))
                    continue
                if i < 24:
                    shutil.move(filepath, os.path.join(
                        "C:\\Users\\Tanweer\\Downloads\\UTSigSplit\\UTSig_updated\\test\\GENUINE", fp1))
                    continue
                if i < 27:
                    shutil.move(filepath, os.path.join(
                        "C:\\Users\\Tanweer\\Downloads\\UTSigSplit\\UTSig_updated\\val\\GENUINE", fp1))
                    continue
    print("Done")


if __name__ == "__main__":
    main()
