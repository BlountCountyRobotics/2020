from wpilib.command import InstantCommand, Scheduler
import wpilib

class Toggle(InstantCommand):
    def __init__(self):
        Command.__init__(self, "DropFeeder")

        self.requires(self.getRobot().DropFeeder)
    def initialize(self):
        pass
    def execute(self):
        self.getRobot().DropFeeder.set(not self.getRobot().DropFeeder.get())
