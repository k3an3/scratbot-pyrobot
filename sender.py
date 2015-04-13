class Sender:
    def __init__(self):
        self.sent_commands = {}
    
    def storeSentCommand(self, command):
        self.sent_commands[command.command_id] = command
        
    def getCommandById(self, command_id):
        return self.sent_commands[command_id]
    
    def sendCommand(self, command):
        self.sent_commands[command.command_id] = command

class DebugSender(Sender):
    def sendCommand(self, command):
        print("DEBUG: -->  %s" % command.toCommandString())
        Sender.sendCommand(self, command)
        
class FifoSender(Sender):
    def __init__(self, fifo):
        self.fifo = file(fifo, "w")
        Sender.__init__(self)
        
    def sendCommand(self, command):
        fifo.write("DEBUG: -->  %s" % command.toCommandString())
        Sender.sendCommand(self, command)
