#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def even_publisher():
    pub = rospy.Publisher('even_numbers', Int32, queue_size=10)
    rospy.init_node('even_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    count = 0
    while not rospy.is_shutdown():
        if count % 2 == 0:
            pub.publish(count)
            rospy.loginfo(count)
        count += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        even_publisher()
    except rospy.ROSInterruptException:
        pass
