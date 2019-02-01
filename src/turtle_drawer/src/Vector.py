import rospy
from geometry_msgs.msg import Twist


class Vector:
    
    __twist = Twist()
    
    def __init__(self, x, y, z = 0, w = 0):
        self.__twist.linear.x = self.x = x
        self.__twist.linear.y = self.y = y
        self.__twist.linear.z = self.z = z
        self.w = w
        
        
    def SetEulerAngles(self, x = 0, y = 0, z):
        self.__twist.angular.x = x
        self.__twist.angular.y = y
        self.__twist.angular.z = z
        
    def SetVector(self, x, y, z = 0, w = 0):
        self.__twist.linear.x = self.x = x
        self.__twist.linear.y = self.y = y
        self.__twist.linear.z = self.z = z
       
    @property
    def Twist(self):                         #Use this for publishers
        return self.__twist
        
    def __repr__(self, category):
        if category == 'linear':
            return "('{}', '{}', {}')".format(self.__twist.linear.x, self.__twist.linear.y, self.__twist.linear.z)
        elif category == 'angular':
            return "('{}', '{}', {}')".format(self.__twist.linear.x, self.__twist.linear.y, self.__twist.linear.z)
        

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        self.w += other.w
        
        self.__twist.linear.x = self.x
        self.__twist.linear.y = self.y
        self.__twist.linear.z = self.z
        
        return self
    
    
    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        self.w -= other.w
        
        self.__twist.linear.x = self.x
        self.__twist.linear.y = self.y
        self.__twist.linear.z = self.z
        
        return self
    
    def __mul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        self.w *= scalar
        
        self.__twist.linear.x = self.x
        self.__twist.linear.y = self.y
        self.__twist.linear.z = self.z
        
        return self
    
    
    
    
    
    
    
    
    
    