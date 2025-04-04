# -*- coding: utf-8 -*-

from twisted.internet import protocol, reactor

class Knock(protocol.Protocol):
    def dataReceived(self, data):
        print("Client:", data)
        if data.startswith("Knock knock".encode('ascii')):
            response = "Who's there?"
        else:
            response = str(data) + " who?"
        print("Server:", response)
        self.transport.write(response.encode('ascii'))
        
class KnockFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Knock()

reactor.listenTCP(8000, KnockFactory())
reactor.run()