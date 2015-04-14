import sender

def parseStatus(string, mysender):
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
    return None


class Status:

    def __init__(self, command):
        self.command = command

class MoveForwardStatus(Status):

    def __init__(self, command, distance, abort_reason):
        self.distance_actually_moved = distance
        self.abort_reason = abort_reason
        Status.__init__(self, command)

class MoveReverseStatus(Status):

    def __init__(self, command, distance, abort_reason):
        self.distance_actually_moved = distance
        self.abort_reason = abort_reason
        Status.__init__(self, command)

class RotateClockwiseStatus(Status):

    def __init__(self, command, degrees, abort_reason):
        self.degrees_actually_turned = degrees
        self.abort_reason = abort_reason
        Status.__init__(self, command)

class RotateCounterclockwiseStatus(Status):

    def __init__(self, command, degrees, abort_reason):
        self.degrees_actually_turned = degrees
        self.abort_reason = abort_reason
        Status.__init__(self, command)
