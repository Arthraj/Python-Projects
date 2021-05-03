from pytube import YouTube
url=input("Enter url:")
my_video=YouTube(url)

print(my_video.title)

stream=my_video.streams.first()
stream.download()