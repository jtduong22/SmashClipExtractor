filename='TestFormat.txt'

# class for locating clip location
class clip:
    def __init__(self, name: str, time: str, file: str):
        self.name = name
        self.time = time
        self.file = file

def ParseFile(filename: str, moves: dict) -> int:
    # number of clips
    clip_count = 0

    # attempt to open file
    try:
        file = open(filename, 'r')

        for line in file:
            print(line)

    # open failure
    except:
        print(f"error: could not open {filename}")
        pass
    return clip_count

ParseFile('TestFormat.txt', {})