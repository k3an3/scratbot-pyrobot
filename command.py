class Command:
    last_command_id = 0

    def __init__(self):
        self.command_id = Command.last_command_id + 1
        Command.last_command_id += 1

    def toCommandString():
        return ""

class MoveForwardCommand(Command):

    def __init__(self, distance=200):
        self.distance = distance
        super(Subclass, self).__init__()

    def toCommandString():
        return '!mvfwd,' + self.command_id + ',' + str(self.distance) + '$'

class MoveReverseCommand(Command):

    def __init__(self, distance=200):
        self.distance = distance
        super(Subclass, self).__init__()

    def toCommandString():
        return '!mvrev,' + self.command_id + ',' + str(self.distance) + '$'

class RotateClockwiseCommand(Command):

    def __init__(self, degrees=90):
        self.degrees = degrees
        super(Subclass, self).__init__()

    def toCommandString():
        return '!rtclk,' + self.command_id + ',' + str(self.degrees) + '$'

class RotateCounterclockwiseCommand(Command):

    def __init__(self, degrees=90):
        self.degrees = degrees
        super(Subclass, self).__init__()

    def toCommandString():
        return '!rtctc,' + self.command_id + ',' + str(self.degrees) + '$'
