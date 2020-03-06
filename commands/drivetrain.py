from wpilib.command import Command

class FollowJoystick(Command):
    def __init__(self):
        
        Command.__init__(self, "Follow Joystick")
        self.requires(self.getRobot().drivetrain)

    def execute(self):
        self.getRobot().drivetrain.drive_with_joystick(self.getRobot().controller)

    def isFinished(self):
        return False

class AimBot(Command):
    def __init__(self):
        Command.__init__(self, "AimBot")
        self.requires(self.getRobot().drivetrain)
        self.chamelion = self.getRobot().networkTable.getSubTable("chamelion-vision/USB Camera-B4.09.24.1")
        self.aimYawTarget = 0
        self.aimYawP = 0.01
#       self.aimYawD = 0.2
        self.aimPitchTarget = 0
        self.aimPitchP = 0.005
#       self.aimPitchD = 0.5

    def execute(self):
        self.chamelion.putNumber("pipeline", 4)
        move = self.aimPitchP * (self.aimPitchTarget - self.chamelion.getNumber("targetPitch", self.aimPitchTarget))
        rotation = self.aimYawP * (self.aimYawTarget - self.chamelion.getNumber("targetYaw", self.aimYawTarget))

        left = move + rotation
        right = move - rotation

        self.getRobot().drivetrain.set_motors(left, right)

    def isFinished(self):
        return False

class EmergencyStop(Command):
    def __init__(self):
        Command.__init__(self, "EmergencyStop")
        self.requires(self.getRobot().drivetrain)

    def isFinished(self):
        return False

    def execute(self):
        self.getRobot().drivetrain.set_motors(0.0, 0.0)
