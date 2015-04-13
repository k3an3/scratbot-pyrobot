import sender

def parseStatus(string, mysender):
    if string[0] != '!':
        return None
    parts = string.split(',')
    cmd_type = parts[0][1:]
    command = mysender.getCommandById(parts[1])
    if command:
        if cmd_type == 'mvfwd':
            if not len(parts) == 4:
                return None
            return MoveForwardStatus(int(parts[2]), int(parts[3]))
        elif cmd_type == 'mvrev':
            if not len(parts) == 4:
                return None
            return MoveReverseStatus(int(parts[2]), int(parts[3]))
        elif cmd_type == 'rtclk':
            if not len(parts) == 4:
                return None
            return MoveClockwiseStatus(int(parts[2]), int(parts[3]))
        elif cmd_type == 'rtctc':
            if not len(parts) == 4:
                return None
            return MoveCounterclockwiseStatus(int(parts[2]), int(parts[3]))
    return None


class Status:

    def __init__(self, command_id):
        self.command = getCommandById(command_id)

class MoveForwardStatus(Status):

    def __init__(self, distance, abort_reason):
        self.distance_actually_moved = distance
        self.abort_reason = abort_reason

class MoveReverseStatus(Status):

    def __init__(self, distance, abort_reason):
        self.distance_actually_moved = distance
        self.abort_reason = abort_reason

class RotateClockwiseStatus(Status):

    def __init__(self, degrees, abort_reason):
        self.degrees_actually_turned = degrees
        self.abort_reason = abort_reason

class RotateCounterclockwiseStatus(Status):

    def __init__(self, degrees, abort_reason):
        self.degrees_actually_turned = degrees
        self.abort_reason = abort_reason
