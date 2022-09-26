# Import the required library
from tkinter import *
import time
import playsound
import customtkinter


# Modes: system (default), light, dark
customtkinter.set_appearance_mode("System")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("green")

# Create an instance of tkinter frame

win = customtkinter.CTk()  # create CTk window like you do with the Tk window
win.geometry('310x100')
win.resizable(1, 1)

text_font = ("Neucha", 38)
background = "black"
foreground = "#363529"
border_width = 25

# Configure the background
win.config(bg=background)
# Create Entry Widgets for HH MM SS
sec = StringVar()
Entry(win, textvariable=sec, width=2, font=text_font).place(x=240, y=20)
sec.set('00')
mins = StringVar()
Entry(win, textvariable=mins, width=2, font=text_font).place(x=170, y=20)
mins.set('00')
hrs = StringVar()
Entry(win, textvariable=hrs, width=2, font=text_font).place(x=100, y=20)
hrs.set('00')
# Define the function for the timer


def countdowntimer():
    times = int(hrs.get())*3600 + int(mins.get())*60 + int(sec.get())
    while times > -1:
        minute, second = (times // 60, times % 60)
        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
        # Update the time
        win.update()
        time.sleep(1)
        if (times == 0):
            sec.set('00')
            mins.set('00')
            hrs.set('00')
        times -= 1
    playsound('alarm.mp3')


label = Label(win, font=text_font, bg=background,
              fg=foreground, bd=border_width)
label.grid(row=0, column=1)


button = customtkinter.CTkButton(
    master=win, width=30, text="START", command=countdowntimer)
button.place(relx=0.2, rely=0.3, anchor=CENTER)


button = customtkinter.CTkButton(
    master=win, width=30, text="STOP", command=countdowntimer)
button.place(relx=0.2, rely=0.6, anchor=CENTER)

win.attributes('-topmost', True)

win.mainloop()
