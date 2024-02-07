from configparser import ConfigParser
from os import getenv
from os.path import isfile
from winreg import OpenKey, HKEY_CURRENT_USER, KEY_WRITE, REG_DWORD, SetValueEx

gameconfig = ConfigParser()
path_gameusersettings = getenv("LOCALAPPDATA") + "\\FortniteGame\\Saved\\Config\\WindowsClient\\GameUserSettings.ini"

class GameConfig():
    def check_if_config_exists():
        if isfile(path_gameusersettings):
            return True
        

    def retrieve_resolutionfps():
        gameconfig.read(path_gameusersettings)
        resx = gameconfig["/Script/FortniteGame.FortGameUserSettings"]["ResolutionSizeX"]
        resy = gameconfig["/Script/FortniteGame.FortGameUserSettings"]["ResolutionSizeY"]
        fps = float(gameconfig["/Script/FortniteGame.FortGameUserSettings"]["FrameRateLimit"])
        return [resx, resy, "{:0.0f}".format(int(fps))]

    def retrieve_windowmode():
        gameconfig.read(path_gameusersettings)
        windowmode = gameconfig["/Script/FortniteGame.FortGameUserSettings"]["lastconfirmedfullscreenmode"]
        return windowmode


    def apply(resx, resy, fps, windowmode):
        gameconfig["/Script/FortniteGame.FortGameUserSettings"]["ResolutionSizeX"] = str(resx)
        gameconfig["/Script/FortniteGame.FortGameUserSettings"]["ResolutionSizeY"] = str(resy)
        gameconfig["/Script/FortniteGame.FortGameUserSettings"]["lastuserconfirmedresolutionsizex"] = str(resx)
        gameconfig["/Script/FortniteGame.FortGameUserSettings"]["lastuserconfirmedresolutionsizey"] = str(resy)
        gameconfig["/Script/FortniteGame.FortGameUserSettings"]["FrameRateLimit"] = "{:.6f}".format(int(fps))
        gameconfig["/Script/FortniteGame.FortGameUserSettings"]["lastconfirmedfullscreenmode"] = str(windowmode)
        gameconfig["/Script/FortniteGame.FortGameUserSettings"]["preferredfullscreenmode"] = str(windowmode)
        gameconfig["/Script/FortniteGame.FortGameUserSettings"]["FullscreenMode"] = str(windowmode)

        with open(path_gameusersettings, 'w') as file:
            gameconfig.write(file)


usersettingsconfig = ConfigParser()
path_usersettings = getenv("APPDATA") + "\\ezres\\usersettings.ini"

class UserSettings():
    def apply(theme="dark"):
        if not isfile(path_usersettings):
            usersettingsconfig.add_section("UserSettings")
            usersettingsconfig.set("UserSettings", "theme", theme)

            with open(path_usersettings, "w") as file:
                usersettingsconfig.write(file)
        else:
            usersettingsconfig.read(path_usersettings)
            usersettingsconfig["UserSettings"]["theme"] = theme
            
            with open(path_usersettings, "w") as file:
                usersettingsconfig.write(file)

    def retrieve_theme():
        if isfile(path_usersettings):
            usersettingsconfig.read(path_usersettings)
            return str(usersettingsconfig["UserSettings"]["theme"])
        else:
            return "dark"
  
        
miscconfig = ConfigParser()
path_miscconfig = getenv("APPDATA") + "\\ezres\\MiscConfig.ini"

class MiscConfig():
    def check_if_config_exists():
        if isfile(path_miscconfig):
            return True
        else:
            miscconfig.add_section("MiscSettings")
            miscconfig.set("MiscSettings", "exclusivefullscreen", "false")
            
            with open(path_miscconfig, 'w') as file:
                miscconfig.write(file)
    
    def retrieve():
        miscconfig.read(path_miscconfig)
        exclusivefullscreen = miscconfig["MiscSettings"]["exclusivefullscreen"]
        return exclusivefullscreen

    def apply(exclusivefullscreen):
        try:
            key = OpenKey(HKEY_CURRENT_USER, r'System\GameConfigStore', 0, KEY_WRITE)
            SetValueEx(key, "GameDVR_DXGIHonorFSEWindowsCompatible", 0, REG_DWORD, 1)
            SetValueEx(key, "GameDVR_EFSEFeatureFlags", 0, REG_DWORD, 0)
            SetValueEx(key, "GameDVR_Enabled", 0, REG_DWORD, 0)   
            SetValueEx(key, "GameDVR_FSEBehaviorMode", 0, REG_DWORD, 2)  
            SetValueEx(key, "GameDVR_HonorUserFSEBehaviorMode", 0, REG_DWORD, 1)
        except Exception as ex:
            print(ex)

        miscconfig["MiscSettings"]["exclusivefullscreen"] = str(exclusivefullscreen)

        with open(path_miscconfig, 'w') as file:
                miscconfig.write(file)

    def undo():
        try:
            key = OpenKey(HKEY_CURRENT_USER, r'System\GameConfigStore', 0, KEY_WRITE)
            SetValueEx(key, "GameDVR_DXGIHonorFSEWindowsCompatible", 0, REG_DWORD, 0)
            SetValueEx(key, "GameDVR_EFSEFeatureFlags", 0, REG_DWORD, 0)
            SetValueEx(key, "GameDVR_Enabled", 0, REG_DWORD, 0)   
            SetValueEx(key, "GameDVR_FSEBehaviorMode", 0, REG_DWORD, 1)  
            SetValueEx(key, "GameDVR_HonorUserFSEBehaviorMode", 0, REG_DWORD, 1)
        except Exception as ex:
            print(ex)

        miscconfig["MiscSettings"]["exclusivefullscreen"] = "false"

        with open(path_miscconfig, 'w') as file:
                miscconfig.write(file)
            