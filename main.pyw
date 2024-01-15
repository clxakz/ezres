#ivoxprojects 2024

import customtkinter
from customtkinter import *
from tkinter import messagebox
import config

customtkinter.set_appearance_mode("dark")

root = CTk()
root.geometry("300x300")
root.resizable(False, False)
root.title("EzRes")
try:
    root.iconbitmap("./ezres.ico")
except Exception as ex:
    print(str(ex))
root.eval('tk::PlaceWindow . center')

font = CTkFont("Roboto", 15, "normal")

frame = CTkFrame(root, fg_color="grey12", border_width=1, border_color="white")
frame.pack(fill="both", expand=True, padx=5, pady=5)

labels = ["Width", "Height", "FPS"]
for x in labels:
    lbl = CTkLabel(frame, text=x, font=font)
    lbl.grid(column=labels.index(x), row=0, pady=(5,0))

widget_entries = []
entries = ["resx", "resy", "FPS"]
for x in entries:
    entry = CTkEntry(frame, width=90, corner_radius=5, fg_color="grey12", border_color="white", border_width=1, font=font, justify="center")
    entry.grid(row=1, column=entries.index(x), padx=5 if x==0 or x==1 else (5,0), pady=(0,5))
    widget_entries.append(entry)

frame2 = CTkFrame(frame, border_width=1, border_color="white", fg_color="grey12")
frame2.grid(row=2, columnspan=3, sticky="nsew", padx=(5,0), pady=5)

radio_var = customtkinter.IntVar()
windowmodes = ["Fullscreen", "Windowed Fullscreen", "Windowed"]
for x in windowmodes:
    radiobtn = CTkRadioButton(frame2, text=x, variable=radio_var, value=windowmodes.index(x), font=font, border_width_checked=3, fg_color="white", hover_color="grey30")
    radiobtn.pack(pady=5, padx=5 if windowmodes.index(x)==0 or windowmodes.index(x)==1 else (5,0), anchor="w")

frame3 = CTkFrame(frame, border_width=1, border_color="white", fg_color="grey12")
frame3.grid(row=3, columnspan=3, sticky="nsew", padx=(5,0))

def slider_event(value):
    sliderlabel.configure(text=f"Resolution Scale {value:.0f}%")

sliderlabel = CTkLabel(frame3, font=font)
sliderlabel.pack(pady=(5,0), anchor="w", padx=10)

slider = CTkSlider(frame3, from_=0, to=100, height=25, command=slider_event, button_color="white", button_hover_color="grey30", fg_color="grey20", progress_color="grey40")
slider.pack(pady=(0,5), fill="x", padx=5)

def check_if_entries_are_valid():
    resx = widget_entries[0].get() 
    resy = widget_entries[1].get()
    fps = widget_entries[2].get()
    windowmode = radio_var.get() 
    resscale = slider.get()

    try:
        config.apply(resx if resx else widget_entries[0]._placeholder_text, 
                    resy if resy else widget_entries[1]._placeholder_text, 
                    fps if fps else widget_entries[2]._placeholder_text, 
                    windowmode, resscale)
        messagebox.showinfo("EzRes", "Config saved")
    except Exception as ex:
        messagebox.showerror("EzRes Error", "Error Message: " + str(ex))

applybutton = CTkButton(frame, text="APPLY", height=45, font=(font, 18), fg_color="#39ad50", hover_color="grey30", command=check_if_entries_are_valid)
applybutton.grid(row=4, columnspan=3, padx=(5,0), sticky="we", pady=(5,0))

if __name__ == "__main__":
    if config.check_if_config_exists():
        for x in widget_entries:
            x.configure(placeholder_text=config.retrieve_resolutionfps()[widget_entries.index(x)])

        radio_var.set(config.retrieve_windowmode())
        slider.set(config.retrieve_resolutionscale())
        sliderlabel.configure(text=f"Resolution Scale {slider.get():.0f}%")

        root.mainloop()
    else:
        messagebox.showerror("EzRes Error", "Config file could not be located or does not exist")