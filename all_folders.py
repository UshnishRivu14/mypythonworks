import os

folder = os.listdir("data")

for fol in folder:
    print(folder)
    print()
    print(os.listdir(f"data/{folder}"))