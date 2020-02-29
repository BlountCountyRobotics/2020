import rev
import ctre
import wpilib
from wpilib.command import Subsystem
from commands.drivetrain import FollowJoystick
from commands.shooter import StopShooting
import robot_map

class DriveTrain(Subsystem):
    def __init__(self):
        Subsystem.__init__(self, "DriveTrain")

        self.left1 = ctre.TalonSRX(robot_map.drivetrain_motors["left1"])
        self.left2 = ctre.TalonSRX(robot_map.drivetrain_motors["left2"])
        self.left3 = ctre.TalonSRX(robot_map.drivetrain_motors["left3"])

        self.right1 = ctre.TalonSRX(robot_map.drivetrain_motors["right1"])
        self.right2 = ctre.TalonSRX(robot_map.drivetrain_motors["right2"])
        self.right3 = ctre.TalonSRX(robot_map.drivetrain_motors["right3"])

       # self.gearshift = wpilib.Solenoid(1)

    def drive_with_joystick(self, controller):
        left_trigger  = (controller.getRawAxis(robot_map.ds4["l2_axis"]) + 1) / 2
        right_trigger = (controller.getRawAxis(robot_map.ds4["r2_axis"]) + 1) / 2

        multiplier = .40 + (left_trigger * .30) + (right_trigger * .30)
        
        left  = controller.getRawAxis(robot_map.ds4["l-y_axis"]) * multiplier
        right = controller.getRawAxis(robot_map.ds4["r-y_axis"]) * multiplier

        #if controller.getRawButtonPressed(robot_map.ds4["r1"]):
            #self.gearshift.set(not self.gearshift.get())
        
        self.set_motors(left, right)

    def set_motors(self, left, right):

        self.left1.set(ctre.ControlMode.PercentOutput, left)
        self.left2.set(ctre.ControlMode.PercentOutput, left)
        self.left3.set(ctre.ControlMode.PercentOutput, left)

        self.right1.set(ctre.ControlMode.PercentOutput, -right)
        self.right2.set(ctre.ControlMode.PercentOutput, -right)
        self.right3.set(ctre.ControlMode.PercentOutput, -right)

    def initDefaultCommand(self):
        self.setDefaultCommand(FollowJoystick())


class Shooter(Subsystem):
    def __init__(self):
        Subsystem.__init__(self, "Shooter")

        self.motor1 = rev.SparkMax(robot_map.shooter_motors["motor1"])
        self.motor2 = rev.SparkMax(robot_map.shooter_motors["motor2"])

    def shoot(self):
        self.motor1.set(robot_map.shooter_output)
        self.motor1.set(robot_map.shooter_output)

    def stop(self):
        self.motor1.set(0.0)
        self.motor2.set(0.0)

    def initDefaultCommand(self):
        self.setDefaultCommand(StopShooting())

class IntakeRoller(Subsystem):
    def __init__(self):
        Subsystem.__init__(self, "IntakeRoller")

        self.roller_motor = ctre.TalonSRX(robot_map.IntakeRoller_motors["Roller_Motor"])

    def takeIn(self):
        self.roller_motor.set(robot_map.roller_output)

    def stop(self):
        self.roller_motor.set(0.0)

    def initDefaultCommand(self):
        self.setDefaultCommand()