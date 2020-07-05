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



# arm.reset(wait=True)

speed = 100

# arm.set_servo_angle(angle=[0, 0, -20, 0, 0, 0], speed=speed, wait=True)
# print(arm.get_servo_angle())
# # print(arm.get_servo_angle(), arm.get_servo_angle(is_radian=True))

# print(arm.get_position())
print()
PrintPosition()

# arm.set_position(x=280, y=100, z=110, roll=180, pitch=0, yaw=0,speed=speed, wait=True)

Z_Up = 110
Z_Down = 95
# X = 260

# arm.set_position(x=265, y=100, z=Z_Up, roll=180, pitch=0, yaw=0,speed=speed, wait=True)

for X in range(225,265,3):
    for Y in range(-80,100,5):
        arm.set_position(x=X, y=Y, z=Z_Up, roll=180, pitch=0, yaw=0,speed=speed, wait=False)
        arm.set_position(x=X, y=Y, z=Z_Down, roll=180, pitch=0, yaw=0,speed=speed, wait=False)
        arm.set_position(x=X, y=Y, z=Z_Up, roll=180, pitch=0, yaw=0,speed=speed, wait=False)
        PrintPosition()

# arm.reset(wait=True) # Sets back to home position
arm.disconnect()
