"""
Sender Module

Facilitates the sending of commands to the robot over serial.
"""

import serial

class Sender:
    """
    Base class for all senders.
    """
    def __init__(self):
        self.sent_commands = {}

    def sendCommand(self, command):
        """
        Base method keeps track of sent commands so the corresponding status can be validated upon reciept.
        Method can be overridden by subclasses in order to send commands over an actual medium.
        """
        self.sent_commands[command.command_id] = command

    def getCommandById(self, command_id):
        """
        Fetch a stored command by its unique id.
        """
        return self.sent_commands[command_id]

class DebugSender(Sender):
    """
    Sender class for debugging purposes only.
    """
    def sendCommand(self, command):
        print("DEBUG: -->  %s" % command.toCommandString())
        Sender.sendCommand(self, command)

class FifoSender(Sender):
    """
    File-based sender class for debugging purposes only.
    """
    def __init__(self, fifo):
        Sender.__init__(self)
        self.fifo = file(fifo, "w")

    def sendCommand(self, command):
        fifo.write("DEBUG: -->  %s" % command.toCommandString())
        Sender.sendCommand(self, command)

class PySerialSender(Sender):
    """
    Sender class used in conjunction with pyserial to send commands to the robot.
    """
    def __init__(self, ser):
        Sender.__init__(self)
        self.ser = ser

    def sendCommand(self, command):
        """
        Send command over pyserial.
        """
        print "DEBUG--> " + command.toCommandString()
        self.ser.write(command.toCommandString())
        Sender.sendCommand(self, command)
