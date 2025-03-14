import webbrowser
import pyautogui
import time

url = "https://reelit.net/#google_vignette"
insta_link = "https://www.instagram.com/reel/DHJM9eZT_q1/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA=="
rename_file = "test" + ".mp4"
yt_folder_link = "C:/Users/ronis/OneDrive - Global College of Management/ytshorts"

print(rename_file)


webbrowser.open_new(url)
time.sleep(3)

pyautogui.scroll(-600)
time.sleep(3)
pyautogui.click(829, 867)
pyautogui.typewrite(insta_link)
pyautogui.press("enter")
pyautogui.scroll(-200)
time.sleep(2)
pyautogui.click(913, 1447)

print(pyautogui.position())

time.sleep(2)


# import os

# print("hello")
# downloads_path = os.path.expanduser("~/Downloads")  # Works for Windows, Mac, Linux
# files = os.listdir(downloads_path)
# print(files)  # List all files

# for fil in files:
#     if fil.startswith("Reelit.net"):
#         continue
#     else:


# file_name = "example.txt"
# absolute_path = os.path.abspath(file_name)


import os
import shutil

downloads_folder = os.path.expanduser("~/Downloads")  # Path to Downloads folder
files = os.listdir(downloads_folder)  # List all files in Downloads

# Get the full file paths
files = [
    os.path.join(downloads_folder, f)
    for f in files
    if os.path.isfile(os.path.join(downloads_folder, f))
]

# Filter for .mp4 files
mp4_files = [f for f in files if f.endswith(".mp4")]

# Find the most recently created .mp4 file
if mp4_files:
    last_downloaded_mp4 = max(mp4_files, key=os.path.getctime)

    Absolute_Path_of_Mp4 = os.path.abspath(last_downloaded_mp4)

    # Use os.path.abspath() to ensure the path is fully expanded to an absolute path
    print("Last downloaded .mp4 file:", Absolute_Path_of_Mp4)
else:
    print("No .mp4 files found in Downloads")

shutil.move(Absolute_Path_of_Mp4, yt_folder_link + f"/{rename_file}")
