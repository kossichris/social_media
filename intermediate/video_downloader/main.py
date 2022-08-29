import pytube

link = input('Enter Youtbe Video URL: ')

yt = pytube.YouTube(link)
yt.streams.first().download()
print('downloaded', link)
