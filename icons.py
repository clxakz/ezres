from requests import get
from os import getenv, mkdir
from os.path import isdir
from tkinter.messagebox import showinfo

path_appdata = getenv("APPDATA") + "\\ezres"

def download_icons():
    if not isdir(path_appdata):
        showinfo("ezres", "Installing appdata please wait")
        mkdir(path_appdata)
        URLS = ["https://raw.githubusercontent.com/ivoxprojects/ezres/main/icons/icon.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/icons/height_dark.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/icons/height_light.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/icons/width_dark.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/icons/width_light.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/icons/lock_dark.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/icons/lock_light.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/icons/fullscreen_dark.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/icons/fullscreen_light.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/icons/windowed_dark.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/icons/windowed_light.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/icons/windowedfullscreen_dark.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/icons/windowedfullscreen_light.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/icons/theme_dark.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/icons/theme_light.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/icons/ico.ico"]
        
        for url in URLS:
            response = get(url, allow_redirects=True)
            if response.ok:
                print("[ezres] Downloading icon > " + response.url)

                with open(f"{path_appdata}\\{response.url.split("/")[-1]}", "wb") as file:
                    file.write(response.content)

        print("[ezres] Done installing")

    else:
        print("[ezres] Icons are already Installed")