from requests import get
from os import getenv, mkdir
from os.path import isdir
from tkinter.messagebox import showinfo

path_appdata = getenv("APPDATA") + "\\ezres"

def download_icons():
    if not isdir(path_appdata):
        showinfo("ezres", "Installing appdata please wait")
        mkdir(path_appdata)
        URLS = ["https://raw.githubusercontent.com/ivoxprojects/ezres/main/icon.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/height_dark.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/height_light.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/width_dark.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/width_light.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/lock_dark.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/lock_light.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/fullscreen_dark.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/fullscreen_light.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/windowed_dark.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/windowed_light.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/windowedfullscreen_dark.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/windowedfullscreen_light.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/theme_dark.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/theme_light.png",
                "https://raw.githubusercontent.com/ivoxprojects/ezres/main/ico.ico"]
        
        for url in URLS:
            response = get(url, allow_redirects=True)
            if response.ok:
                print("[ezres] Downloading icon > " + response.url)

                with open(f"{path_appdata}\\{response.url.split("/")[-1]}", "wb") as file:
                    file.write(response.content)

        print("[ezres] Done installing")

    else:
        print("[ezres] Icons are already Installed")
