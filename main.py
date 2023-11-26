from pytube import YouTube # YouTube API
from sys import argv # Command line argument reader
import ssl # SSL Certificate Verification

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context # Bypasses Certificate Verification Clearance


yt_link = argv[1] # Second argument -> Youtube video link

yt = YouTube(yt_link)

print("Downloading video: \"", yt.title, "\"")

yt.streams.get_highest_resolution().download("./videos")

print("Download complete!")

