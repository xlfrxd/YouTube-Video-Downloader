from pytube import YouTube # YouTube API
from tkinter import StringVar
import customtkinter # GUI Library from CustomTkinter by tomschimansky

import ssl # SSL Certificate Verification
import traceback # To print the error stack trace

def downloadVideo(link):
    try:
        yt = YouTube(link)

        updateStatus("Downloading video: \"" + yt.title + "\"")
    
        yt.streams.get_highest_resolution().download("./videos")

        updateStatus("Download complete!")  
    except Exception as e:
        updateStatus("Download failed!")
        print("Error occurred:", e)  # Print error message to the terminal
        traceback.print_exc()  # Print the full error stack trace

def updateStatus(updated_txt):
    statusLbl.configure(text=updated_txt)

def downloadClicked():
    downloadVideo(linkEntry.get())
    linkEntry.focus()

# Main Loop

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context # Bypasses Certificate Verification Clearance

# Root 
root = customtkinter.CTk()

# Main Properties
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

# Root Window Properties
root.title("YouTube Video Downloader by xlfrxd")
root.geometry('400x250')

# Main Frame
mainFrame = customtkinter.CTkFrame(master=root)
mainFrame.pack(padx=0, pady=0, expand=True, fill="both")

# Widgets

# Title Label
titleLbl = customtkinter.CTkLabel(mainFrame, text = "YouTube Video Downloader (.mp4)", font=("Helvetica Neue",20))
titleLbl.pack(padx=5, expand=True, fill="both")

# Subtitle Label
subtitleLbl = customtkinter.CTkLabel(mainFrame, text = "by xlfrxd", font=("Helvetica Neue",12))
subtitleLbl.pack(padx=5, pady=0, expand=True, fill="both")

# Link Textbox
linkEntry = customtkinter.CTkEntry(mainFrame, placeholder_text="YouTube Link")
linkEntry.pack(padx=5, pady=10, expand=True, fill="both")

# Download Button
downloadBtn = customtkinter.CTkButton(mainFrame, text = "Download", command=downloadClicked)
downloadBtn.pack(padx=5, pady=10, expand=True, fill="both")

# Status Label
statusLbl = customtkinter.CTkLabel(mainFrame, text = "")
statusLbl.pack(padx=5, pady=10, expand=True, fill="both")

# Start GUI
root.mainloop()
