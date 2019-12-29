from ParseFile import Clip
import subprocess

def extractclip(clip: Clip, dir: str, count: int):
    # get clip information
    length = clip.length
    time = clip.time
    name = clip.name
    file = clip.file

    # call ffmpeg to process
    subprocess.call(['ffmpeg', '-i', dir + file, '-c', 'copy', '-ss', time, '-t', str(length), f'./{str.lower(name)}/{name}_{count}.mp4'])
