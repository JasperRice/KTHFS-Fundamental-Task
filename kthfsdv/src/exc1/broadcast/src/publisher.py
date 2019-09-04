#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

k = 1
n = 4

def talker():
    global k, n
    pub = rospy.Publisher("/Jiang", Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        k += n
        rospy.loginfo(k)
        pub.publish(k)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
