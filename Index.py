from time import ctime
from threading import Thread
from os import listdir, remove
from os.path import join
from typing import List
from pytube import YouTube
from moviepy.editor import VideoFileClip

PATH: str = '~\Musica'

def DownloaderVideo(link):
    yt: YouTube = YouTube(link)
    stream: stream = yt.streams.get_lowest_resolution()
    stream.download(PATH)
    print("downloaded")


def Converter(Videomp4):
    Videomp3: str = Videomp4.replace(".mp4", ".mp3")
    video: VideoFileClip = VideoFileClip(join(PATH, Videomp4))
    video.audio.write_audiofile(join(PATH, Videomp3))

    video.close()
    remove(join(PATH, Videomp4))

T: List[Thread] = []
T1: List[Thread] = []
url: List[str] = [
    'https://www.youtube.com/',
    'https://www.youtube.com/',
    'https://www.youtube.com/',
    'https://www.youtube.com/',
    'https://www.youtube.com/',
    'https://www.youtube.com/',
    'https://www.youtube.com/',
    'https://www.youtube.com/',
    'https://www.youtube.com/',
    'https://www.youtube.com/',
    'https://www.youtube.com/',
    'https://www.youtube.com/',
    'https://www.youtube.com/',
    'https://www.youtube.com/'
]

print("--------------------------------------")
print("Start: " + ctime())
print("--------------------------------------")

for i, link in enumerate(url, 1):
    T.append(Thread(target=DownloaderVideo, args=[link]))
    T[i-1].start()

for t in T:
    t.join()

for j, Video in enumerate(listdir(PATH), 1):
    if Video.endswith(".mp4"):
        T1.append(Thread(target=Converter, args=[Video]))
        T1[j-1].start()

for t1 in T1:
    t1.join()

print("--------------------------------------")
print("End: " + ctime())
print("--------------------------------------")
