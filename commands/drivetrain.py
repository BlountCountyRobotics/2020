from wpilib.command import Command

class FollowJoystick(Command):
    def __init__(self):
        
        Command.__init__(self, "Follow Joystick")
        self.requires(self.getRobot().drivetrain)

    def execute(self):
        self.getRobot().drivetrain.drive_with_joystick(self.getRobot().controller)

    def isFinished(self):
        return False

class EmergencyStop(Command):
    def __init__(self):
        Command.__init__(self, "EmergencyStop")
        self.requires(self.getRobot().drivetrain)

    def execute(self):
        self.getRobot().drivetrain.set_motors(0.0, 0.0)
