from customtkinter import *
from CTkToolTip import CTkToolTip
from customtkinter import set_appearance_mode
from time import sleep
from sys import exit
from PIL.Image import open
from os import getenv
from tkinter import messagebox

import icons; icons.download_icons() # < -- Check If Icons Are Installed
import config

root = CTk()
root.geometry("350x360+800+300")
root.overrideredirect(True)
root.attributes("-alpha", 0.1)
root.configure(fg_color="gray1")
root.wm_attributes("-transparentcolor", "gray1")

color_text = ["black", "white"]
color_background = ["gray90", "gray20"]
color_placeholder = ["gray80", "gray16"]
color_selected = ["gray60", "gray17"]

path_appdata = getenv("APPDATA") + "\\ezres"
try: root.iconbitmap(path_appdata + "\\ico.ico")
except: pass

class window():
    def get_position(event):
        global xwin
        global ywin

        xwin = event.x
        ywin = event.y

    def move_window(event):
        root.geometry(f'+{event.x_root - xwin}+{event.y_root - ywin}')

    class play_animation():
        def open(root=root):
            transparency = -0.2
            while True:
                transparency += 0.1
                root.attributes("-alpha", transparency)
                root.update()
                sleep(0.015)
                if transparency >= 1.0:
                    break
            
        def close(root=root):
            transparency = 1.0
            while True:
                transparency -= 0.1
                root.attributes("-alpha", transparency)
                root.update()
                sleep(0.015)
                if transparency <= 0.0:
                    root.destroy()
                    exit(0)
                    break

        def change_theme(root=root, theme="dark"):
            transparency = 1.0
            while True:
                transparency -= 0.1
                root.attributes("-alpha", transparency)
                root.update()
                sleep(0.01)
                if transparency <= 0.0:
                    set_appearance_mode(theme)
                    root.update()
                    break
            transparency = 0
            while True:
                transparency += 0.1
                root.attributes("-alpha", transparency)
                root.update()
                sleep(0.01)
                if transparency >= 1.0:
                    break

# < -- PlaceHolder Frame
TitleBar = CTkFrame(root, fg_color=color_background)
TitleBar.pack(fill="x")
TitleBar.bind("<B1-Motion>", window.move_window)
TitleBar.bind("<Button-1>", window.get_position)

# < -- Titlebar : Define Icon Images
try: image_icon = CTkImage(open(f"{path_appdata}\\icon.png"), open(f"{path_appdata}\\icon.png"), [25,25])
except: image_icon = None

# < -- TitleBar : Icon, Title, Close Button
CloseButton = CTkButton(TitleBar, text="☓", font=("", 15), width=15, text_color=color_text, fg_color=color_background, hover_color="#c50000", command=window.play_animation.close)
Icon = CTkLabel(TitleBar, text="", image=image_icon)
Title = CTkLabel(TitleBar, text="ezres", font=("", 20, "bold"), text_color=color_text)
CloseButton.pack(padx=3, pady=3, side="right")
Icon.pack(side="left", padx=3, pady=3)
Title.pack(padx=3, pady=3, anchor="center")

# <-- MainFrame
MainFrame = CTkFrame(root, fg_color=color_background)
MainFrame.pack(pady=(3,0), fill="both", expand=True)
 

# < -- PlaceHolder Frame
placeholder_usersettings = CTkFrame(MainFrame, fg_color=color_placeholder)
placeholder_usersettings.pack(padx=5, pady=5, fill="both")

# < -- PlaceHolder Frame : Defince Icon Images
try: image_theme = CTkImage(open(f"{path_appdata}\\theme_light.png"), open(f"{path_appdata}\\theme_dark.png"), [25,25])
except: image_theme = None

# < -- PlaceHolder Frame : Switch, Image, Func
def toggle_theme():
    match(switchtoggletheme_var.get()):
        case "dark":
            window.play_animation.change_theme(theme="dark")
            config.UserSettings.apply(theme="dark")
        case "light":
            window.play_animation.change_theme(theme="light")
            config.UserSettings.apply(theme="light")

toggletheme_image = CTkLabel(placeholder_usersettings, text="", image=image_theme)
switchtoggletheme_var = StringVar()
switch_toggletheme = CTkSwitch(placeholder_usersettings, text="", variable=switchtoggletheme_var, onvalue="light", offvalue="dark", font=("", 15, "bold"), button_color=color_text, command=toggle_theme)
label_version = CTkLabel(placeholder_usersettings, text="2.0.3", font=("", 15, "bold"))
toggletheme_image.pack(pady=5, padx=(10,0), side="left")
switch_toggletheme.pack(padx=10, pady=5, side="left")
label_version.pack(side="right", padx=10, pady=5)


# <-- PlaceHolder Frame
placeholder_resentries = CTkFrame(MainFrame, fg_color=color_placeholder)
placeholder_resentries.pack(padx=5, pady=(0,5), fill="both")

# < -- PlaceHolder Frame : Define Icon Images
try: image_width = CTkImage(open(f"{path_appdata}\\width_light.png"), open(f"{path_appdata}\\width_dark.png"), [20,20])
except: image_width = None

try: image_height = CTkImage(open(f"{path_appdata}\\height_light.png"), open(f"{path_appdata}\\height_dark.png"), [16,16])
except: image_height = None

try: image_lock = CTkImage(open(f"{path_appdata}\\lock_light.png"), open(f"{path_appdata}\\lock_dark.png"), [14,14])
except: image_lock = None

# <-- PlaceHolder Frame : Labels
labels = ["Width", "Height", "FPS"]
for x in labels:
    label = CTkLabel(placeholder_resentries, text=x, font=("", 15, "bold"), compound="right", image=image_width if x=="Width" else image_height if x=="Height" else image_lock if x=="FPS" else None)
    label.grid(column=labels.index(x), row=0, pady=(1,0), padx=10 if x==0 or x==1 else (10,0))

# <-- PlaceHolder Frame : Entries
entry_widgets = []
entries = ["resx", "resy", "FPS"]
for x in entries:
    entry = CTkEntry(placeholder_resentries, width=100, corner_radius=5, justify="center", font=("", 15))
    entry.grid(row=1, column=entries.index(x), padx=10 if x==0 or x==1 else (10,0), pady=(0,10))
    entry_widgets.append(entry)


# <-- PlaceHolder Frame
placeholder_winmodes = CTkFrame(MainFrame, fg_color=color_placeholder)
placeholder_winmodes.pack(padx=5, pady=(0,5), fill="both")

# < -- PlaceHolder Frame : Define Icon Images
try: image_fullscreen = CTkImage(open(f"{path_appdata}\\fullscreen_light.png"), open(f"{path_appdata}\\fullscreen_dark.png"), [20,20])
except: image_fullscreen = None

try: image_windowedfullscreen = CTkImage(open(f"{path_appdata}\\windowedfullscreen_light.png"), open(f"{path_appdata}\\windowedfullscreen_dark.png"), [20,20])
except: image_windowedfullscreen = None

try: image_windowed = CTkImage(open(f"{path_appdata}\\windowed_light.png"), open(f"{path_appdata}\\windowed_dark.png"), [25,34])
except: image_windowed = None

# <-- PlaceHolder Frame : Window Modes
radio_var = IntVar()
windowmodes = ["Fullscreen", "Windowed Fullscreen", "Windowed"]
for x in windowmodes:
    radiobtn = CTkRadioButton(placeholder_winmodes, text=x, variable=radio_var, value=windowmodes.index(x), font=("", 15, "bold"), text_color=color_text, border_width_checked=3, fg_color="#3c97ff", border_color="gray50")
    radiobtn.grid(column=1, row=windowmodes.index(x), sticky="w", pady=5)

    windowmode_image = CTkLabel(placeholder_winmodes, text="", image=image_fullscreen if x=="Fullscreen" else image_windowedfullscreen if x=="Windowed Fullscreen" else image_windowed if x=="Windowed" else None)
    windowmode_image.grid(column=0, row=windowmodes.index(x), padx=10)


# < -- PlaceHolder Frame
placeholder_misc = CTkFrame(MainFrame, fg_color=color_placeholder)
placeholder_misc.pack(padx=5, pady=(0,5), fill="both")

# < -- PlaceHolder Frame : Misc Options
switchexclusivefullscreen_var = StringVar()
switch_exclusivefullscreen = CTkSwitch(placeholder_misc, variable=switchexclusivefullscreen_var, offvalue="false", onvalue="true", font=("", 15, "bold"), text="Exclusive Fullscreen", progress_color="#3c97ff", button_color=color_text)
switch_exclusivefullscreen.grid(padx=10, pady=5, row=0, sticky="w")

button_help = CTkButton(placeholder_misc, text="?", font=("", 15, "bold"), width=25, height=25, fg_color="#3c97ff", cursor="question_arrow", state="disabled", text_color_disabled=color_text)
tooltip_text = "When Exclusive-Fullscreen is enabled, your game is being rendered directly to your screen, allocating more system resources to your game resulting in better performance."
tooltip = CTkToolTip(button_help, tooltip_text, 0.2, True, corner_radius=5, font=("", 15, "bold"), wraplength=370, justify="left")
button_help.grid(padx=5, pady=5, row=0, column=1, sticky="e")

placeholder_misc.grid_columnconfigure(0, weight=1)


# < -- PlaceHolder Frame
placeholder_apply = CTkFrame(MainFrame, fg_color=color_placeholder)
placeholder_apply.pack(padx=5, pady=(0,5), fill="both")

# < -- PlaceHolder Frame : Apply Button, Func
def validate_entries():
    resx = entry_widgets[0].get() 
    resy = entry_widgets[1].get()
    fps = entry_widgets[2].get()
    windowmode = radio_var.get() 
    exclusivefullscreen = switchexclusivefullscreen_var.get()

    try:
        config.GameConfig.apply(resx if resx else entry_widgets[0]._placeholder_text, 
                    resy if resy else entry_widgets[1]._placeholder_text, 
                    fps if fps else entry_widgets[2]._placeholder_text, 
                    windowmode)
        
        if exclusivefullscreen == "true":
            config.MiscConfig.apply(exclusivefullscreen)
        else: 
            config.MiscConfig.undo()

        messagebox.showinfo("ezres", "Config Saved")
    except Exception as ex:
        messagebox.showerror("ezres", str(ex))

button_apply = CTkButton(placeholder_apply, text="APPLY", font=("", 15, "bold"), height=45, command=validate_entries)
button_apply.pack(fill="both", padx=5, pady=5)

# <-- MainLoop
if __name__ == "__main__":
    if config.GameConfig.check_if_config_exists():
        for x in entry_widgets:
            x.configure(placeholder_text=config.GameConfig.retrieve_resolutionfps()[entry_widgets.index(x)])

        radio_var.set(config.GameConfig.retrieve_windowmode())

    else:
        messagebox.showerror("ezres", "Fortnite game config could not be located")
        root.destroy()
        exit(0)


    if config.MiscConfig.check_if_config_exists():
        switchexclusivefullscreen_var.set(config.MiscConfig.retrieve())

    match(config.UserSettings.retrieve_theme()):
        case "dark":
            set_appearance_mode("dark")
            switchtoggletheme_var.set("dark")
        case "light":
            set_appearance_mode("light")
            switchtoggletheme_var.set("light")

    window.play_animation.open()
    root.focus()
    root.mainloop()