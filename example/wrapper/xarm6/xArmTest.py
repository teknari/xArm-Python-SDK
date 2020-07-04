#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2019, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

"""
Description: Move Joint
"""

import os
import sys
import time
import math

sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from xarm.wrapper import XArmAPI


ip = '192.168.99.80'
arm = XArmAPI(ip)
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)

def PrintPosition():
    arrPos = arm.get_position()
    arrJoint = arm.get_servo_angle()
    print("X {:>14,.2f}mm".format(arrPos[1][0]))
    print("Y {:>14,.2f}mm".format(arrPos[1][1]))
    print("Z {:>14,.2f}mm".format(arrPos[1][2]))
    print()
    print("Roll  {:>10,.2f}".format(arrPos[1][3]) + u'\u00B0')
    print("Pitch {:>10,.2f}".format(arrPos[1][4]) + u'\u00B0')
    print("Yaw   {:>10,.2f}".format(arrPos[1][5]) + u'\u00B0')
    print()
    for i in range(6):
        print("Joint " + str(i) + "{:>10,.2f}".format(arrJoint[1][i]) + u'\u00B0')
    print()
    return



arm.reset(wait=True)

speed = 50

# arm.set_servo_angle(angle=[-45, 90, -180, 0, 90, 0], speed=speed, wait=True)
# print(arm.get_servo_angle())
# # print(arm.get_servo_angle(), arm.get_servo_angle(is_radian=True))

# print(arm.get_position())
print()
PrintPosition()

# arm.set_position(x=500,y=-100,z=500,speed=speed,wait=True)
# print(arm.get_position())
# arm.set_position(roll=-170,speed=speed,wait=True)
# print(arm.get_position())

# arm.reset(wait=True) # Sets back to home position
arm.disconnect()
