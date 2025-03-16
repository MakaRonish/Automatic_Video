import webbrowser
import pyautogui
import time

print(pyautogui.position())


import os
import shutil


def open_Realit(url, insta_link):
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
    time.sleep(3)


def moving_file():
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
    try:
        shutil.move(Absolute_Path_of_Mp4, yt_folder_link + f"/{rename_file}")
    except NameError:
        open_Realit(url, insta_link)
        moving_file()
    return yt_folder_link + f"/{rename_file}"


def upload_in_tiktok():
    webbrowser.open_new(tiktok_studio)
    time.sleep(3)
    pyautogui.doubleClick(305, 405)
    time.sleep(2)
    pyautogui.click(1618, 1196)
    time.sleep(2)
    pyautogui.click(667, 328)
    time.sleep(2)
    pyautogui.click(2383, 1637)
    time.sleep(5)
    pyautogui.scroll(-1000)
    time.sleep(5)
    pyautogui.click(738, 1515)


def upload_in_youtube():
    webbrowser.open_new(yt_studio)
    time.sleep(3)
    pyautogui.click(2473, 227)
    time.sleep(1)

    pyautogui.click(2404, 314)
    time.sleep(1)
    pyautogui.click(1362, 1175)
    time.sleep(3)
    pyautogui.click(667, 328)
    time.sleep(2)
    pyautogui.click(2383, 1637)
    time.sleep(5)
    pyautogui.click(1756, 1360)
    time.sleep(1)
    pyautogui.scroll(-1000)
    time.sleep(2)
    pyautogui.click(524, 1094)
    time.sleep(2)
    pyautogui.click(2208, 1549)
    time.sleep(2)
    pyautogui.click(2208, 1549)
    time.sleep(2)
    pyautogui.click(2208, 1549)
    time.sleep(2)
    pyautogui.click(625, 1108)
    time.sleep(2)
    pyautogui.click(2208, 1549)


def delete_file(path):
    os.remove(path)


if __name__ == "__main__":
    url = "https://reelit.net/#google_vignette"
    insta_link = input("Video link:")
    rename_file = input("Title of video") + ".mp4"
    yt_folder_link = "C:/Users/ronis/OneDrive - Global College of Management/ytshorts"
    tiktok_studio = "https://www.tiktok.com/tiktokstudio"
    yt_studio = "https://studio.youtube.com/"
    open_Realit(url, insta_link)
    time.sleep(2)
    path = moving_file()

    upload_in_tiktok()
    upload_in_youtube()
    delete_file(path)
