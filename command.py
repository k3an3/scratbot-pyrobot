from sender import get_sent_commands

global last_id

class Command:
    id = 0

    def __init__(self):
        self.id = last_id + 1
        last_id += 1

    def toCommandString():
        return ""

class MoveForwardCommand(Command):
    distance = 200

    def __init__():
        super(Subclass, self).__init__()

    def toCommandString():
        return '!mvfwd,' + self.id + ',' + str(self.distance) + '$'

class MoveReverseCommand(Command):
    distance = 200

    def __init__():
        super(Subclass, self).__init__()

    def toCommandString():
        return '!mvrev,' + self.id + ',' + str(self.distance) + '$'

class RotateClockwiseCommand(Command):
    degrees = 90

    def __init__():
        super(Subclass, self).__init__()

    def toCommandString():
        return '!rtclk,' + self.id + ',' + str(self.degrees) + '$'

class RotateCounterclockwiseCommand(Command):
    degrees = 90

    def __init__():
        super(Subclass, self).__init__()

    def toCommandString():
        return '!rtctc,' + self.id + ',' + str(self.degrees) + '$'
