import rospy
from nav_msgs.msg import Odometry


rospy.init_node("Speed_Controller") # Node Intialization

def newOdom(msg):
    


sub = rospy.Subscriber("/Odometry", Odometry, newOdom) # Node Subscription