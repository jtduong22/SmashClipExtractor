import ParseFile as pf
import ClipExtractor as ce
import os
import subprocess

# filename = 'TestFormat.txt'
filename = 'Clips.txt'
moves = {}
pf.parsefile(filename, moves)

dir = os.getcwd() + '/04/'
os.chdir(dir)

# cycle through each move
for key in moves.keys():

    # create directory if it doesn't already exist
    try:
        os.mkdir(key)
    except:
        print('error: cannot create directory')

    count = 0
    # cycle through each clip of each move
    for clip in moves[key]:
        ce.extractclip(clip, dir, count)
        count += 1

        
