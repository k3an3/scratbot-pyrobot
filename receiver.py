"""
Receiver Module

Facilitates the receiving of statuses from the robot over serial.
"""

import serial
import status
import os
import errno

class Receiver:
    """
    Base class for all recievers.
    """
    def __init__(self, mysender):
        self.received_statuses = []
        self.sender = mysender

    def getStatus(self):
        """
        Return the last (most recent) status added to the stack.
        """
        return self.received_statuses.pop()

    def pushStatus(self, status):
        """
        Add a received status onto the stack.
        """
        self.received_statuses.append(status)

    def isNewStatusAvailable(self):
        """
        Return whether or not there is a new status on the stack.
        """
        return len(self.received_statuses) > 0

    def receive(self, string):
        """
        When a status is recieved, makes sure it is valid and push it if so.
        """
        stat = status.parseStatus(string, self.sender)
        print("DEBUG--> rx: " + string)
        if stat != None:
            self.pushStatus(stat)
        else:
            print("ERR: INVALID STATUS STRING '%s'" % string)

class DebugReceiver(Receiver):
    """
    A dummy receiver for debugging purposes only.
    """
    def __init__(self, mysender):
        Receiver.__init__(self, mysender)

    def receive(self, string):
        Receiver.receive(self, string)

class PySerialReceiver(Receiver):
    """
    Receiver class used in conjunction with pyserial to receive statuses from the robot.
    """
    def __init__(self, sender, ser):
        Receiver.__init__(self, sender)
        self.ser = ser
        self.serbuffer = ""

    def receive(self):
        """
        Continuously wait for and validate syntax of input received over pyserial.
        """
        while True:
            r = self.ser.read(1)
            if r == "!":
                self.serbuffer = "!"
            elif r == "$":
                self.serbuffer += "$"
                Receiver.receive(self, self.serbuffer)
            else:
                self.serbuffer += r

            if len(r) == 0:
                break

class FifoReceiver(Receiver):
    """
    File-based receiver for debugging purposes only.
    """
    def __init__(self, sender, fifo):
        Receiver.__init__(self, sender)

        try:
            os.mkfifo(fifo, 0777)
        except OSError as err:
            if err.errno == errno.EEXIST:
                pass
            else:
                raise

        self.fifo = os.open(fifo, os.O_RDONLY|os.O_NONBLOCK)

        self.fifobuffer = ""

    def receive(self):
        while True:
            try:
                r = os.read(self.fifo, 1)
            except OSError as err:
                if err.errno == errno.EAGAIN or\
                        err.errno == EWOULDBLOCK:

                    r = None
                else:
                    raise

            if r is None or r == '':
                break

            if r == "!":
                self.fifobuffer = "!"
            elif r == "$":
                self.fifobuffer += "$"
                Receiver.receive(self, self.fifobuffer)
            else:
                self.fifobuffer += r
