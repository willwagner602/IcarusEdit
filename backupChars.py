import shutil
from datetime import datetime

source_path = "C:\\Users\\will\\AppData\\Local\\Icarus\\Saved\\PlayerData\\76561198004413179\\Characters.json"
target_path = f"C:\\Users\\will\\AppData\\Local\\Icarus\\Saved\\PlayerData\\76561198004413179\\Characters-{datetime.now():%d-%m-%Y-%H_%M_%S}.json"

print(f"Copying\n{source_path}\n\tto\n{target_path}")

if input("Look good? ") != "y":
    print("okay, skipping")
    exit(1)

shutil.copy(source_path, target_path)

print("Copied")
