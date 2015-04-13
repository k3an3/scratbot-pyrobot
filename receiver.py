import serial
import status

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
    
    def debugReceive(self, string):
        Receiver.receive(self, string)
            
class PySerialReceiver(Receiver):
    def __init__(self, sender, comport, 
            baud=56700, timeout=None):
        
        Receiver.__init__(self, sender)
        self.ser = serial(
                port=comport, 
                baudrate=baud, 
                timeout=timeout,
                writeTimeout=timeout)
        self.serbuffer = ""
        
    def serialReceive(self):
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
        pass
