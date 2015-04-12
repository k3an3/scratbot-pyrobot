class Command:
    last_command_id = 0

    def __init__(self):
        self.command_id = Command.last_command_id + 1
        Command.last_command_id += 1

    def toCommandString():
        return ""

class MoveForwardCommand(Command):
    distance = 200

    def __init__():
        super(Subclass, self).__init__()

    def toCommandString():
        return '!mvfwd,' + self.command_id + ',' + str(self.distance) + '$'

class MoveReverseCommand(Command):
    distance = 200

    def __init__():
        super(Subclass, self).__init__()

    def toCommandString():
        return '!mvrev,' + self.command_id + ',' + str(self.distance) + '$'

class RotateClockwiseCommand(Command):
    degrees = 90

    def __init__():
        super(Subclass, self).__init__()

    def toCommandString():
        return '!rtclk,' + self.command_id + ',' + str(self.degrees) + '$'

class RotateCounterclockwiseCommand(Command):
    degrees = 90

    def __init__():
        super(Subclass, self).__init__()

    def toCommandString():
        return '!rtctc,' + self.command_id + ',' + str(self.degrees) + '$'
