from pytube import YouTube # YouTube API
from sys import argv # Command line argument reader
from tkinter import * # GUI Library
import ssl # SSL Certificate Verification

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context # Bypasses Certificate Verification Clearance

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

# Root window
root = Tk()

# Root Window Properties
root.title("YouTube Video Downloader by xlfrxd")
root.geometry('400x250')

# Widgets

# Title Label
titleLbl = Label(root, text = "YouTube Video Downloader")
titleLbl.grid(row=0,column=0)

# Link Label
linkLbl = Label(root, text = "Link: ")
linkLbl.grid(row=1,column=0)

# Link Textbox
link_var = StringVar()
linkEntry = Entry(root, textvariable=link_var)
link_var.set("")
linkEntry.grid(row=1,column=1)

# Download Button
downloadBtn = Button(root, text = "Download", command=downloadVideo)
downloadBtn.grid(row=2, column=1)

# Status Label
statusLbl = Label(root, text = "")
statusLbl.grid(row=3,column=1)


# Start GUI
root.mainloop()