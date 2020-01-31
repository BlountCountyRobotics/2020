from wpilib.command import Command

class FollowJoystick(Command):
    def __init__(self):
        super().__init__("Follow Joystick")
        self.requires(self.getRobot().drivetrain)

    def execute(self):
        self.getRobot().drivetrain.drive_with_joystick(self.getRobot().controller)

class EmergencyStop(Command):
    def __init__(self):
        super().__init__("EmergencyStop")
        self.requires(self.getRobot().drivetrain)

    def execute(self):
        self.getRobot().drivetrain.set_motors(0.0, 0.0)
