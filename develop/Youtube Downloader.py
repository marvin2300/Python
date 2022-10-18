from pytube import YouTube

url = input("Insert a Youtube URL: \n")

ytt = YouTube(url)
title = ytt.title

print(f"Downloading {title}...")


yt = YouTube(url)


yt.streams.get_highest_resolution()\
    .download("/Users/marvinquirmbach/Documents/YouTube Downloads").title()




