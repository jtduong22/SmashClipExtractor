# class for locating clip location
class Clip:
    def __init__(self):
        self.name = ''
        self.time = ''
        self.file = ''
        self.length = 3

    def initialize(self, name: str, time: str, file: str, length: int = 3):
        self.name = name
        self.time = time
        self.file = file
        self.length = length

    def setname(self, name:str):
        self.name = name

    def settime(self, time:str):
        self.time = time

    def setfile(self, file:str):
        self.file = file

    def setlength(self, length: int = 3):
        self.length = length

def parsemove(move_string: str) -> Clip:
    # clip to return
    clip = Clip()

    # split string
    args = move_string.split()

    # get size to increment to
    arg_count = len(args)
    i = 0

    # loop through string
    while i < arg_count:
        try:
            #  move name
            if args[i] == '-m':
                clip.setname(args[i+1])
                i += 1
            # time clip starts at
            elif args[i] == '-i':
                clip.settime(args[i+1])
                i += 1
            # set clip length
            elif args[i] == '-t':
                clip.setlength(int(args[i+1]))
                i += 1
            # unknown parameter
            else:
                print(f'Unknown parameter: {args[i]}')
        except IndexError:
            raise Exception(f'Missing input after {args[i]}. Discarding line')

        # increment i
        i += 1

    return clip

def parsefile(filename: str, moves: dict) -> int:
    # number of clips
    clip_count = 0

    # attempt to open file
    try:
        file = open(filename, 'r')

        movie_file = ''

        for line in file:
            print(line.split(), end=' ')
            try:
                # is comment
                if line[0] == '#':
                    print()
                    continue

                args = line.split()

                # input file name
                if args[0] == '-f':
                    print(f'File: {args[1]}')
                    movie_file = args[1]

                # parse move
                elif args[0] == '-m':
                    move_info = parsemove(line)

                    # add to dictionary
                    key = str.lower(move_info.name)
                    if key not in moves.keys():     # new entry
                        moves[key] = [move_info]
                    else:
                        moves[key] = moves[key] + [move_info]   # existing entry, append

            except Exception as e:
                print()
                print(f'\nError: {e}')

            print('Not a comment')


    # open failure
    except Exception as e:
        print(f'error: {e}')
        # print(f"error: could not open {filename}")
        # pass
    return clip_count



