from wpilib.command import Command

class Eat(Command):
    def __init__(self):

        Command.__init__(self, "Eat")
        self.requires(self.getRobot().feeder)

    def execute(self):
        self.getRobot().feeder.feed()
    
    def isFinished(self):
        return False

class StopEat(Command):
    def __init__(self):

        Command.__init__(self, "StopEat")
        self.requires(self.getRobot().feeder)

    def execute(self):
        self.getRobot().feeder.starve()
    
    def isFinished(self):
        return False