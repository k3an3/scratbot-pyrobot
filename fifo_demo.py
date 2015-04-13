import sender
import receiver
from command import *
from status import *

# Use from a separate python instance!
def sendStatus(status):
    fifo = file("tmpfifo", 'w')
    fifo.write(status)
    fifo.close()
    
def sendMoveCommand(ms, dist=200):
    ms.sendCommand(MoveForwardCommand(dist))
    
def receiveLoop(mr):
    while True:
        mr.receive()
        if mr.isNewStatusAvailable():
            s = mr.getStatus()
            print ("Command: %s Actual: %s" % (s.command.dist,
                s.distance_actually_moved))
            
def makeDefaultStuff():
    ms = sender.DebugSender()
    return ms, receiver.FifoReceiver(ms, "tmpfifo")
