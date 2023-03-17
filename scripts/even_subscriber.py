#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def even_listener():
    rospy.init_node('even_listener', anonymous=True)
    rospy.Subscriber('my_topic', Int32, even_callback)
    rospy.spin()

def even_callback(data):
    rospy.loginfo("Value: %d", data.data)

if __name__ == '__main__':
    even_listener()
