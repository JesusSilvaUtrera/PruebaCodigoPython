from Robot_control_class import RobotControl

rc = RobotControl(robot_name='summit')
rc.move_straight_time("forward", 0.3, 4)
rc.turn("counter-clockwise", 0.3, 7)
rc.move_straight_time("forward", 0.3, 6)
rc.turn("counter-clockwise", 0.3, 7)
rc.move_straight_time("forward", 0.3, 7)

class RobotMovement():
    def __init__(self, motion, clockwise, speed, time):
        self.robot_control = RobotControl(robot_name='summit')
        self.motion = motion
        self.clockwise = clockwise
        self.speed = speed
        self.time = time
        self.time_rotate = 7.0  # approximate time to rotate 90 degrees

    def squareMovement(self):
        i = 0
        while i < 4:
            self.move_straight()
            self.turn()
            i += 1

    def move_straight(self):
        self.robot_control.move_straight_time(
            self.motion, self.speed, self.time)

    def turn(self):
        self.robot_control.turn(self.clockwise, self.speed, self.time_rotate)


motionRobot1 = RobotMovement('forward', 'clockwise', 0.3, 4)
motionRobot1.squareMovement()
motionRobot2 = RobotMovement('forward', 'clockwise', 0.3, 8)
motionRobot2.squareMovement()