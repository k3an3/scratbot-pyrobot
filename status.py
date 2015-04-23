"""
Status Module

Contains classes for status objects, which represent statuses returned by the robot.
"""

import sender

def parseStatus(string, mysender):
    """
    Parses the raw string from the receiver and creates a status object based on the type of status
    after validating that the string is correct and the corresponding command exists.
    """
    if string[0] != '!':
        return None
    if string.endswith('$'):
        string = string[:-1]
    parts = string.split(',')
    cmd_type = parts[0][1:]
    command = mysender.getCommandById(int(parts[1]))
    if command:
        if cmd_type == 'mvfwd':
            if not len(parts) == 4:
                return None
            return MoveForwardStatus(command, int(parts[2]), int(parts[3]))
        elif cmd_type == 'mvrev':
            if not len(parts) == 4:
                return None
            return MoveReverseStatus(command, int(parts[2]), int(parts[3]))
        elif cmd_type == 'rtclk':
            if not len(parts) == 4:
                return None
            return RotateClockwiseStatus(command, int(parts[2]), int(parts[3]))
        elif cmd_type == 'rtctc':
            if not len(parts) == 4:
                return None
            return RotateCounterclockwiseStatus(command, int(parts[2]), int(parts[3]))
        elif cmd_type == 'scan':
            if not len(parts) == 5:
                return None
            return ScanDataStatus(command, int(parts[2]),
                    int(parts[3]),int(parts[4]))
    return None


class Status:
    """
    Base class for status objects.
    """

    def __init__(self, command):
        self.command = command
        self.isDataStatus = False

        self.strings = {}
        self.strings[0] = "Movement fully completed"
        self.strings[1] = "Left bumper collision"
        self.strings[2] = "Right bumper collision"
        self.strings[3] = "Right wheeldrop detected"
        self.strings[4] = "Left wheeldrop detected"
        self.strings[5] = "Caster wheeldrop detected"
        self.strings[6] = "Mystery wall detected"
        self.strings[7] = "Left cliff detected"
        self.strings[8] = "Right cliff detected"
        self.strings[9] = "Front left cliff detected"
        self.strings[10] = "Front right cliff detected"
        self.strings[11] = "Virtual wall detected"
        self.strings[12] = "Left white floor detected"
        self.strings[13] = "Right white floor detected"
        self.strings[14] = "Front left white floor detected"
        self.strings[15] = "Front right white floor detected"
        self.strings[100] = "Weird abort reason"

    def abortReasonString(self):
        """
        Return the string represented by the abort reason number.
        """
        return self.strings[self.abort_reason]

    def actualResultString(self):
        """
        Unimplemented base class. Subclasses can override so that the method prints out a formatted
        status string which can be displayed to the user.
        """
        return "Base Class. Not implemented."

class MoveForwardStatus(Status):
    """
    Status class containing the results of a move forward command.
    """
    def __init__(self, command, distance, abort_reason):
        self.distance_actually_moved = distance
        self.abort_reason = abort_reason
        Status.__init__(self, command)

    def actualResultString(self):
        return "Actually moved {} mm".format(self.distance_actually_moved)

class MoveReverseStatus(Status):
    """
    Status class containing the results of a move reverse command.
    """
    def __init__(self, command, distance, abort_reason):
        self.distance_actually_moved = distance
        self.abort_reason = abort_reason
        Status.__init__(self, command)

    def actualResultString(self):
        return "Actually moved {} mm".format(self.distance_actually_moved)

class RotateClockwiseStatus(Status):
    """
    Status class containing the results of a rotate clockwise command.
    """
    def __init__(self, command, degrees, abort_reason):
        self.degrees_actually_turned = degrees
        self.abort_reason = abort_reason
        Status.__init__(self, command)

    def actualResultString(self):
        return "Actually turned {} degrees".format(self.degrees_actually_turned)

class RotateCounterclockwiseStatus(Status):
    """
    Status class containing the results of a rotate counterclockwise command.
    """
    def __init__(self, command, degrees, abort_reason):
        self.degrees_actually_turned = degrees
        self.abort_reason = abort_reason
        Status.__init__(self, command)

    def actualResultString(self):
        return "Actually turned {} degrees".format(self.degrees_actually_turned)

#Format: "!scan,cmd_id,angle,distance(cm),size(cm)$"
class ScanDataStatus(Status):
    """
    Status class containing information about a single scanned object.
    """
    def __init__(self, command, angle, distance, size):
        self.size = size
        self.angle = angle
        self.distance = distance
        Status.__init__(self, command)
        self.isDataStatus = True
