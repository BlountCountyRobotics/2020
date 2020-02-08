import ctre
import wpilib
from wpilib.command import Subsystem
from commands.drivetrain import FollowJoystick
import robot_map

class DriveTrain(Subsystem):
    def __init__(self):
        Subsystem.__init__(self, "DriveTrain")

        self.left1 = ctre.WPI_TalonSRX(robot_map.drivetrain_motors["left1"])
        self.left2 = ctre.WPI_TalonSRX(robot_map.drivetrain_motors["left2"])
        self.left3 = ctre.WPI_TalonSRX(robot_map.drivetrain_motors["left3"])

        self.right1 = ctre.WPI_TalonSRX(robot_map.drivetrain_motors["right1"])
        self.right2 = ctre.WPI_TalonSRX(robot_map.drivetrain_motors["right2"])
        self.right3 = ctre.WPI_TalonSRX(robot_map.drivetrain_motors["right3"])

        self.gearshift = wpilib.Solenoid(1)

    def drive_with_joystick(self, controller):
        left_trigger  = (controller.getRawAxis(robot_map.ds4["l2_axis"]) + 1) / 2
        right_trigger = (controller.getRawAxis(robot_map.ds4["r2_axis"]) + 1) / 2

        multiplier = .40 + (left_trigger * .30) + (right_trigger * .30)
        
        left  = controller.getRawAxis(robot_map.ds4["l-y_axis"]) * multiplier
        right = controller.getRawAxis(robot_map.ds4["r-y_axis"]) * multiplier

        if controller.getRawButtonPressed(robot_map.ds4["r1"]):
            self.gearshift.set(not self.gearshift.get())
        
        self.set_motors(left, right)

    def set_motors(self, left, right):
        self.left1.set(left)
        self.left2.set(left)
        self.left3.set(left)

        self.right1.set(-right)
        self.right2.set(-right)
        self.right3.set(-right)

    def initDefaultCommand(self):
        self.setDefaultCommand(FollowJoystick())
