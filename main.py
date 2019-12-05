import ParseFile as pf
import ClipExtractor as ce

filename = 'TestFormat.txt'
moves = {}
pf.parsefile(filename, moves)
ce.extractclip()

print(moves)