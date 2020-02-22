import wpilib, ctre, rev, constants
from wpilib.command import InstantCommand, Scheduler

class Toggle(Instant)
    def color_wheel(self):
        self.motor = rev.CANSparkMax(1, rev.MotorType.kBrushless)
        self.controller = wpilib.Joystick(0)

        if self.controller.getRawButtonPressed(robot_map.ds4["triangle"]):
            self.motor.setPosition(360)