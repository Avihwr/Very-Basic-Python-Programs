from pytube import YouTube
link = input(">>")
url = YouTube(link)
print(url.title)