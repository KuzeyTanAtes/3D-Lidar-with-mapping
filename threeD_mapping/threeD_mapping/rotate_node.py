#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
import os
import subprocess
import signal

def euler_from_quaternion(x, y, z, w):
        """
        Convert a quaternion into euler angles (roll, pitch, yaw)
        roll is rotation around x in radians (counterclockwise)
        pitch is rotation around y in radians (counterclockwise)
        yaw is rotation around z in radians (counterclockwise)
        """
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)
     
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)
     
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)
     
        return roll_x, pitch_y, yaw_z # in radians


class Feedback(Node):

    flag = True
    def __init__(self):
        super().__init__('rotate_me')
        self.declare_parameter('theta', rclpy.Parameter.Type.DOUBLE)
        self.get_logger().info("rotate_me launched")
        self.odomReader = self.create_subscription(Odometry, '/odom', self.sub_callback, 10)
        self.odomReader
        self.angularZpub = self.create_publisher(Twist, '/cmd_vel', 10)


    def sub_callback(self, msgReceived: Odometry):

        msgToSend = Twist()

        quat = [msgReceived.pose.pose.orientation.x, msgReceived.pose.pose.orientation.y, msgReceived.pose.pose.orientation.z, msgReceived.pose.pose.orientation.w]
        current_theta = euler_from_quaternion(quat[0], quat[1], quat[2], quat[3])
        theta = math.radians(self.get_parameter('theta').value)

        difference = current_theta[2]-theta
        if (abs(difference) < math.radians(0.5)):
             msgToSend.angular.z = 0.0
             self.angularZpub.publish(msgToSend)
             self.destroy_node()
             rclpy.shutdown()
        if (difference > math.radians(3)):
             msgToSend.angular.z = -0.3
        elif (difference < -math.radians(3)):
             msgToSend.angular.z = 0.3  

        self.angularZpub.publish(msgToSend)

def main(args = None):
    rclpy.init(args=args)
    rotate_me = Feedback()
    rclpy.spin(rotate_me)
    rotate_me.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
