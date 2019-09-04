#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

pub = rospy.Publisher("/kthfs/results", Float64, queue_size=10)
q = 0.15

def callback(data):
    global pub, q
    rospy.loginfo(rospy.get_caller_id() + "recieve: %f" % data.data)
    data.data /= q
    pub.publish(data)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/Jiang", Float64, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
