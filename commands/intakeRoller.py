import wpilib, ctre, rev
from wpilib.command import Command, Scheduler

class Intake(Command):
    def __init__(self):
        Command.__init__(self, "Intake")
        
        self.requires(self.getRobot().IntakeRoller)
   
    def initalize(self):
        pass

    #Execute is what is sending output to the motors.
    def execute(self):
        self.getRobot().IntakeRoller.takeIn()

    def isFinished(self):
        return False


class StopIntake(Command):
    def __init__(self):
        #super().__init__("StopShooting")

        Command.__init__(self, "StopIntake")

        #tells the robot that the shooter is running, and that nothing else should run on the shooter.
        self.requires(self.getRobot().intakeRoller)
   
    def initalize(self):
        pass

    #Execute is what is sending output to the motors.
    def execute(self):
        self.getRobot().IntakeRoller.stop()

    def isFinished(self):
        return False
