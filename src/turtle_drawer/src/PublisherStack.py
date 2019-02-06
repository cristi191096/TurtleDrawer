#!/usr/bin/env python

class PublisherStack:
    
    
    
    def __init__(self):
        #TODO
        self.publishers = []

    def PushPublisher(self, pub):
        if pub not in self.publishers:
            self.publishers.append(pub)
        
    def PopPublisher(self, pub):
        if pub in self.publishers:
            self.publishers.remove(pub)
