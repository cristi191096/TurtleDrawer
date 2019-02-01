import rospy
from PublisherStack import PublisherStack


class Application:
    
    __node = None
    __publisherStack = None
    __running = False
    
    def __init__(self):
        self. __node = rospy.init_node('turtle_drawer', anonymous = False)
        self.__publisherStack = PublisherStack()
        self.__running = not rospy.is_shutdown()

    
    
    
    def Run(self):
        
        while self.__running:
            for publisher in self.__publisherStack:
                publisher.Publish()
            
    

