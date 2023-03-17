#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def even_publisher():
    pub = rospy.Publisher('my_topic', Int32, queue_size=10)
    overflow_pub = rospy.Publisher('overflow', Int32, queue_size=10)
    rospy.init_node('overflow_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    count = 0
    while not rospy.is_shutdown():
        if count % 2 == 0:
            pub.publish(count)
        count += 2
        if count == 100:
            overflow_pub.publish(count)
            count = 0
        rate.sleep()
        rospy.loginfo(count)

if __name__ == '__main__':
    try:
        even_publisher()
    except rospy.ROSInterruptException:
        pass
