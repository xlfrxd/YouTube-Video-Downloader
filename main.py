from pytube import YouTube # YouTube API
from tkinter import StringVar
import customtkinter # GUI Library from CustomTkinter by tomschimansky

import ssl # SSL Certificate Verification


def downloadVideo():

    yt = YouTube(link_var.get())

    updateStatus("Downloading video: \"" + yt.title + "\"")

    try:
    
        yt.streams.get_highest_resolution().download("./videos")

    except:
        updateStatus("Download failed!")

    updateStatus("Download complete!")

def updateStatus(updated_txt):
    statusLbl.configure(text=updated_txt)

# Main Loop

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context # Bypasses Certificate Verification Clearance

# Root window
root = customtkinter.CTk()
root.geometry("500x350")


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

# Root Window Properties
root.title("YouTube Video Downloader by xlfrxd")
root.geometry('400x250')


# Main Frame
mainFrame = customtkinter.CTkFrame(master=root)
mainFrame.grid()

# Widgets

# Title Label
titleLbl = customtkinter.CTkLabel(mainFrame, text = "YouTube Video Downloader")
titleLbl.grid(row=0,column=1)

# Link Label
linkLbl = customtkinter.CTkLabel(mainFrame, text = "Link: ")
linkLbl.grid(row=1,column=0)

# Link Textbox
link_var = StringVar()
linkEntry = customtkinter.CTkEntry(mainFrame, textvariable=link_var)
link_var.set("")
linkEntry.grid(row=1,column=1)

# Download Button
downloadBtn = customtkinter.CTkButton(mainFrame, text = "Download", command=downloadVideo)
downloadBtn.grid(row=2, column=1)

# Status Label
statusLbl = customtkinter.CTkLabel(mainFrame, text = "")
statusLbl.grid(row=3,column=1)


# Start GUI
root.mainloop()