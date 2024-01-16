import requests
import os

icon = os.getenv("APPDATA") + "\\ezres\\icon.ico"

def get_icon():
    if not os.path.exists(icon):
        os.mkdir(os.getenv("APPDATA") + "//ezres")
        url = "https://raw.githubusercontent.com/ivoxprojects/ezres/main/ezres.ico"
        response = requests.get(url, allow_redirects=True)
        open(icon, "wb").write(response.content)
        print("[ezres] Getting icon")
        return icon
    else:
        print("[ezres] Icon found")
        return icon