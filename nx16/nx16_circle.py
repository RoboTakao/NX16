#!/usr/bin/env python
import sys, rospy, tf, moveit_commander, random, math
from geometry_msgs.msg import Pose, Point, Quaternion
from math import pi

orient = Quaternion(*tf.transformations.quaternion_from_euler(pi , -pi/2 , 0)) 
pose = Pose(Point( 0.08, 0, 0.08), orient) 
moveit_commander.roscpp_initialize(sys.argv) 
rospy.init_node('nx16_circle',anonymous=True)
group = moveit_commander.MoveGroupCommander("single")

while not rospy.is_shutdown():
  for i in range(0, 360, 15):
    pose.position.y =  0 + 0.04 * math.sin(pi*i/180)
    pose.position.z =  0.06 + 0.04 * math.cos(pi*i/180)
    group.set_pose_target(pose)
    group.go(True)

moveit_commander.roscpp_shutdown()
