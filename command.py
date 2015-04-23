"""
Command Module

Contains classes for command objects, which represent different types of commands that can be sent to the robot.
"""

class Command:
    """
    Base class for all command objects.
    """

    last_command_id = 0

    def __init__(self):
        """
        Instantiates command objects with a unique id.
        """
        self.command_id = Command.last_command_id + 1
        Command.last_command_id += 1

    def toCommandString(self):
        """
        Return a command string that can be sent to the robot.
        """
        return ""

class MoveForwardCommand(Command):
    """
    Command to move the robot forward by a given distance.
    """

    def __init__(self, distance=200):
        self.distance = distance
        Command.__init__(self)

    def toCommandString(self):
        return '!mvfwd,' + str(self.command_id) + ',' + str(self.distance) + '$'

class MoveReverseCommand(Command):
    """
    Command to move the robot backwards by a given distance.
    """

    def __init__(self, distance=200):
        self.distance = distance
        Command.__init__(self)

    def toCommandString(self):
        return '!mvrev,' + str(self.command_id) + ',' + str(self.distance) + '$'

class RotateClockwiseCommand(Command):
    """
    Command to rotate the robot clockwise by a given number of degrees.
    """

    def __init__(self, degrees=90):
        self.degrees = degrees
        Command.__init__(self)

    def toCommandString(self):
        return '!rtclk,' + str(self.command_id) + ',' + str(self.degrees) + '$'

class RotateCounterclockwiseCommand(Command):
    """
    Command to rotate the robot counterclockwise by a given number of degrees.
    """

    def __init__(self, degrees=90):
        self.degrees = degrees
        Command.__init__(self)

    def toCommandString(self):
        return '!rtctc,' + str(self.command_id) + ',' + str(self.degrees) + '$'

class BeginScanCommand(Command):
    """
    Command to have the robot begin scanning for obstacles.
    """

    def __init__(self):
        Command.__init__(self)

    def toCommandString(self):
        return '!scan,' + str(self.command_id) + '$'

class PlayMusicCommand(Command):
    """
    Command to have the robot start playing a certain preloaded song identified by number.
    """

    def __init__(self, song_no=0):
        self.song_no = song_no
        Command.__init__(self)

    def toCommandString(self):
        return '!music,' + str(self.command_id) + str(self.song_no) + '$'
