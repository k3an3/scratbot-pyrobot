class Command:
    last_command_id = 0

    def __init__(self):
        self.command_id = Command.last_command_id + 1
        Command.last_command_id += 1

    def toCommandString(self):
        return ""

class MoveForwardCommand(Command):

    def __init__(self, distance=200):
        self.distance = distance
        Command.__init__(self)

    def toCommandString(self):
        return '!mvfwd,' + str(self.command_id) + ',' + str(self.distance) + '$'

class MoveReverseCommand(Command):

    def __init__(self, distance=200):
        self.distance = distance
        Command.__init__(self)

    def toCommandString(self):
        return '!mvrev,' + str(self.command_id) + ',' + str(self.distance) + '$'

class RotateClockwiseCommand(Command):

    def __init__(self, degrees=90):
        self.degrees = degrees
        Command.__init__(self)

    def toCommandString(self):
        return '!rtclk,' + str(self.command_id) + ',' + str(self.degrees) + '$'

class RotateCounterclockwiseCommand(Command):

    def __init__(self, degrees=90):
        self.degrees = degrees
        Command.__init__(self)

    def toCommandString(self):
        return '!rtctc,' + str(self.command_id) + ',' + str(self.degrees) + '$'
        
class BeginScanCommand(Command):

    def __init(self):
        Command.__init__(self)
        
    def toCommandString(self):
        return '!scan,' + str(self.command_id) + '$'
