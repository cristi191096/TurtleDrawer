#!/usr/bin/env python

class PublisherStack:
    
    __publishers = []
    
    def __init__(self):
        #TODO
        pass

    def PushPublisher(self, pub):
        self.__publishers.append(pub)
        
    def PopPublisher(self, pub):
        self.__publishers.remove(pub)