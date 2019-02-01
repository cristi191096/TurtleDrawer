import rospy

class Publisher:
    
    __rosPublisher = None
    
    def __init__(self, topic, message, queueSize):
        #TODO
        self.topic = topic
        self.message = message
        self.queueSize = queueSize
        self.__rosPublisher = rospy.Publisher(self.topic, self.message, self.queueSize)
        
        
        
    def Publish(self):
        self.__rosPublisher.publish(self.message)
        
        
        
        
        
        
class VelocityPublisher(Publisher):
    
    def __init__(self, turtleID, vector):
        topic = '/turtle' + str(turtleID) + '/cmd_vel'
        msg = vector.Twist
        qs = 10
        super().__init__(topic, msg, qs)
    
    
    
