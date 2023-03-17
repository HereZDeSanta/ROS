#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def overflow_listener():
    rospy.init_node('overflow_listener', anonymous=True)
    rospy.Subscriber('overflow', Int32, overflow_callback)
    rospy.spin()

def overflow_callback(data):
    rospy.loginfo("Counter has overflowed! Value: %d", data.data)

if __name__ == '__main__':
    overflow_listener()
