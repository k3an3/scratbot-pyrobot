from sender import *

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


