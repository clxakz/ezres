#ivoxprojects 2024

from configparser import ConfigParser
import os

config = ConfigParser()
gameusersettings = os.getenv("LOCALAPPDATA") + "\\FortniteGame\\Saved\\Config\\WindowsClient\\GameUserSettings.ini"

def check_if_config_exists():
    if os.path.isfile(gameusersettings):
        return True
    

def retrieve_resolutionfps():
    config.read(gameusersettings)
    resx = config["/Script/FortniteGame.FortGameUserSettings"]["ResolutionSizeX"]
    resy = config["/Script/FortniteGame.FortGameUserSettings"]["ResolutionSizeY"]
    fps = float(config["/Script/FortniteGame.FortGameUserSettings"]["FrameRateLimit"])
    return [resx, resy, "{:0.0f}".format(int(fps))]

def retrieve_windowmode():
    config.read(gameusersettings)
    windowmode =  config["/Script/FortniteGame.FortGameUserSettings"]["lastconfirmedfullscreenmode"]
    return windowmode

def retrieve_resolutionscale():
    config.read(gameusersettings)
    resolutionscale = int(config["ScalabilityGroups"]["sg.ResolutionQuality"])
    return resolutionscale

def apply(resx, resy, fps, windowmode, resscale):
    config["/Script/FortniteGame.FortGameUserSettings"]["ResolutionSizeX"] = str(resx)
    config["/Script/FortniteGame.FortGameUserSettings"]["ResolutionSizeY"] = str(resy)
    config["/Script/FortniteGame.FortGameUserSettings"]["lastuserconfirmedresolutionsizex"] = str(resx)
    config["/Script/FortniteGame.FortGameUserSettings"]["lastuserconfirmedresolutionsizey"] = str(resy)
    config["/Script/FortniteGame.FortGameUserSettings"]["FrameRateLimit"] = "{:.6f}".format(int(fps))
    try:
        config["/Script/FortniteGame.FortGameUserSettings"]["FullscreenMode"] = str(windowmode)
    except Exception as ex:
        print(str(ex))
    config["/Script/FortniteGame.FortGameUserSettings"]["lastconfirmedfullscreenmode"] = str(windowmode)
    config["/Script/FortniteGame.FortGameUserSettings"]["preferredfullscreenmode"] = str(windowmode)
    config["ScalabilityGroups"]["sg.ResolutionQuality"] = str(round(resscale))

    with open(gameusersettings, 'w') as configfile:
        config.write(configfile)