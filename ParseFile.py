# class for locating clip location
class Clip:
    def __init__(self, name: str, time: str, file: str, length: int = 3):
        self.name = name
        self.time = time
        self.file = file
        self.length = length


def parsefile(filename: str, moves: dict) -> int:
    # number of clips
    clip_count = 0

    # attempt to open file
    try:
        file = open(filename, 'r')

        for line in file:
            print(line.split())

    # open failure
    except:
        print(f"error: could not open {filename}")
        pass
    return clip_count



