from time import ctime
from threading import Thread
from os import listdir, remove
from os.path import join
from typing import List
from pytube import YouTube
from moviepy.editor import VideoFileClip

PATH: str = '~\Musica'

def DownloaderVideo(link):
    if link.startswith("h"):
        yt: YouTube= YouTube(link)
        stream = yt.streams.get_lowest_resolution()
        stream.download(PATH)
        print("downloaded")


def Converter(Videomp4):
    Videomp3: str = Videomp4.replace(".mp4", ".mp3")
    video: VideoFileClip = VideoFileClip(join(PATH, Videomp4))
    video.audio.write_audiofile(join(PATH, Videomp3))

    video.close()
    remove(join(PATH, Videomp4))

T:  List[Thread] = []
T1: List[Thread] = []
LPath: List[str] = []
YOUTUBE_URL: List[str] = open(r'list.txt', 'r').read().splitlines()

print("--------------------------------------")
print("Start: " + ctime())
print("--------------------------------------")

for i, link in enumerate(YOUTUBE_URL, 1):
    T.append(Thread(target=DownloaderVideo, args=[link]))
    T[i-1].start()

for t in T:
    t.join()

for i in listdir(PATH):
    if i.endswith(".mp4"):
        LPath.append(i)

for j, Video in enumerate(LPath, 1):
    T1.append(Thread(target=Converter, args=[Video]))
    T1[j-1].start()

for t1 in T1:
    t1.join()

print("--------------------------------------")
print("End: " + ctime())
print("--------------------------------------")
