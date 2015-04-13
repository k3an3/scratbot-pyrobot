import sender

def parseStatus(string, mysender=sender.getDefaultSender()):
    if string[0] != '!':
        return None
    parts = string.split(',')
    cmd_type = parts[0][1:]
    command = mysender.getCommandByID(parts[1])
    if command:
        if cmd_type == 'mvfwd':
            if not len(parts) == 4:
                return None
            return MoveForwardStatus(int(parts[2]), parts[3])
        elif cmd_type == 'mvrev':
            if not len(parts) == 4:
                return None
            return MoveForwardStatus(int(parts[2]), parts[3])
        elif cmd_type == 'rtclk':
            if not len(parts) == 4:
                return None
        elif cmd_type == 'rtctc':
            if not len(parts) == 4:
                return None


class Status:

    def __init__(self, command_id):
        self.command = getCommandByID(id)

class MoveForwardStatus(Status):

    def __init__(self, distance, abort_reason):
        self.distance_actually_moved = distance
        self.abort_reason = abort_reason

class MoveForwardStatus(Status):

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
