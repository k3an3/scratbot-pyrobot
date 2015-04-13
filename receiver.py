import serial
import status
import os
import errno

class Receiver:
    def __init__(self, mysender):
        self.received_statuses = []
        self.sender = mysender
        
    def getStatus(self):
        return self.received_statuses.pop()
    
    def pushStatus(self, status):
        self.received_statuses.append(status)
        
    def isNewStatusAvailable(self):
        if len(self.received_statuses) > 0:
            return True
        else:
            return False
        
    def receive(self, string):   
        stat = status.parseStatus(string, self.sender)
        if stat != None:
            self.pushStatus(stat)
        else:
            print("ERR: INVALID STATUS STRING '%s'" % string)

class DebugReceiver(Receiver):
    def __init__(self, mysender):
        Receiver.__init__(self, mysender)
    
    def receive(self, string):
        Receiver.receive(self, string)
            
class PySerialReceiver(Receiver):
    def __init__(self, sender, ser)
        Receiver.__init__(self, sender)
        self.ser = ser
        self.serbuffer = ""
        
    def receive(self):
        keep_reading = True
        while keep_reading:
            r = self.ser.read(1)
            if r == "!":
                self.serbuffer = "!"
            elif r == "$":
                self.serbuffer += "$"
                Receiver.receive(self, self.serbuffer)
            else:
                self.serbuffer += r
                
            if len(r) == 0:
                keep_reading = False
                
class FifoReceiver(Receiver):
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
