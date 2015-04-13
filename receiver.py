from status import Status

class Receiver:
    def __init__(self):
        self.received_statuses = []
        
    def getStatus(self):
        return received_statuses.pop()
    
    def pushStatus(self, status):
        self.received_statuses.push(status)
        
    def isNewStatusAvailable(self):
        if len(received_statuses) > 0:
            return True
        else:
            return False

class DebugReceiver(Receiver):
    def __init__(self):
        Receiver.__init__(self)
    
    def fakeReceive(self, string):
        stat = Status.parseStatus(string)
        if stat != None:
            self.pushStatus(stat)
        else:
            print("ERR: INVALID STATUS STRING '%s'" % string)
            
class PySerialReceiver(Receiver):
    def __init__(self, comport, baud=56700):
        Receiver.__init__(self)
        #create and start receive thread
        

