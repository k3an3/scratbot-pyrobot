class Sender:
    def __init__(self):
        self.sent_commands = {}
    
    def storeSentCommand(self, command):
        self.sent_commands[command.command_id] = command
        
    def getCommandById(self, command_id):
        return self.sent_commands[command_id]
    
    def sendCommand(self):
        sent_commands[command.command_id] = command

class DebugSender(Sender):
    def sendCommand(self, command):
        print("DEBUG: -->  %s" % command.toCommandString)
        Sender.sendCommand(self, command)
