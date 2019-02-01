#!/usr/bin/env python

class PublisherStack:
    
    
    
    def __init__(self):
        #TODO
        self.publishers = []
        self.dummy = 0

    def PushPublisher(self, pub):
        if pub not in self.__publishers:
            self.publishers.append(pub)
        
    def PopPublisher(self, pub):
        if pub in self.__publishers:
            self.publishers.remove(pub)