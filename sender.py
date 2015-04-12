from command import *

class Sender:
    def __init__(self):
        self.sent_commands = {}
    
    def storeSentCommand(self, command):
        self.sent_commands[command.command_id] = command
        
    def getCommandById(self, command_id):
        return self.sent_commands[command_id]
        
