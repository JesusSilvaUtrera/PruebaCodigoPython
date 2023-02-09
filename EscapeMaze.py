from Robot_control_class import RobotControl
import time

rc = RobotControl()
num_turns = 0
while num_turns < 3:
    laser_front = rc.get_front_laser()
    if laser_front > 0.75:
        rc.move_straight()
    else:
        rc.stop_robot()
        laser_left = rc.get_laser(719)
        laser_right = rc.get_laser(0)
        if laser_right < laser_left:
            rc.rotate(-90)
        else:
            rc.rotate(90)
        num_turns += 1
# Last straight movement before stopping the robot outside the maze
rc.move_straight_time('forward', 0.5, 10)
rc.stop_robot()
