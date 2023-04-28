from Phidget22.Phidget import *
from Phidget22.Devices.Accelerometer import *
from Phidget22.Devices.Gyroscope import *
from Phidget22.Devices.Magnetometer import *
import time

import rospy
from geometry_msgs.msg import Twist

def messagePublisher():
    # define topic
    imu_pub = rospy.Publisher('imuTopic', Twist, queue_size=10)
    
    # initialize publisher node
    rospy.init_node('imuPubNode')

    # set rate to __ messages per second
    rate = rospy.Rate(10)

    msg = Twist()

    while not rospy.is_shutdown():
        # read in accelerometer and gyro data
        acc = getAcceleration()
        gyro = getAngularRate()

        # set message for acceleration
        msg.linear.x = acc[0]
        msg.linear.y = acc[1]
        msg.linear.z = acc[2]

        # set message for gyro
        msg.angular.x = gyro[0]
        msg.angular.y = gyro[1]
        msg.angular.z = gyro[2]

        # display message in terminal
        rospy.loginfo("Published IMU data")

        # publish the message
        imu_pub.publish(msg)

        # sleep for desired time
        rate.sleep()

def main():
    accelerometer0 = Accelerometer()
    gyroscope0 = Gyroscope()
    #magnetometer0 = Magnetometer()

    accelerometer0.openWaitForAttachment(5000)
    gyroscope0.openWaitForAttachment(5000)
    #magnetometer0.openWaitForAttachment(5000)

    try:
        messagePublisher()
    except rospy.ROSInterruptException:
        pass

    accelerometer0.close()
    gyroscope0.close()
    #magnetometer0.close()

main()
