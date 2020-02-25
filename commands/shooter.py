import wpilib, ctre, rev
from wpilib.command import Command, Scheduler

class Shoot(Command):
    def __init__(self):
        #super().__init__("Shoot")

        Command.__init__(self, "Shoot")

        #tells the robot that the shooter is running, and that nothing else should run on the shooter.
        self.requires(self.getRobot().shooter)
   
    def initalize(self):
        pass

    #Execute is what is sending output to the motors.
    def execute(self):
        self.getRobot().shooter.shoot()

    def isFinished(self):
        return False


class StopShooting(Command):
    def __init__(self):
        #super().__init__("StopShooting")

        Command.__init__(self, "StopShooting")

        #tells the robot that the shooter is running, and that nothing else should run on the shooter.
        self.requires(self.getRobot().shooter)
   
    def initalize(self):
        pass

    #Execute is what is sending output to the motors.
    def execute(self):
        self.getRobot().shooter.stop()

    def isFinished(self):
        return False
