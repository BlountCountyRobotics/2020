import wpilib, ctre, rev, constants
from wpilib.command import Command, Scheduler

class Shoot(Command):
    def __init__(self):
        super().__init__("Shoot")
        #tells the robot that the shooter is running, and that nothing else should run on the shooter.
        self.requires(self.getRobot().shooter)
   
    def initalize(self):
        pass

    #Execute is what is sending output to the motors.
    def execute(self):
        self.getRobot().shooter.shoot()



class StopShooting(Command):
    def __init__(self):
        super().__init__("StopShooting")
        #tells the robot that the shooter is running, and that nothing else should run on the shooter.
        self.requires(self.getRobot().shooter)
   
    def initalize(self):
        pass

    #Execute is what is sending output to the motors.
    def execute(self):
        self.getRobot().shooter.stop()
