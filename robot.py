from wpilib import command
import commands, robot_map, wpilib, subsystems
import wpilib.buttons as buttons
from commandbased import CommandBasedRobot

#    _/  _/    _/_/_/_/    _/    _/  _/   
#   _/  _/    _/        _/  _/  _/  _/    
#  _/_/_/_/  _/_/_/    _/  _/  _/_/_/_/   
#     _/          _/  _/  _/      _/      
#    _/    _/_/_/      _/        _/  

class Lyra(CommandBasedRobot):
    def robotInit(self):
        command.Command.getRobot = lambda x: self

        self.compressor = wpilib.Compressor()
        self.controller = wpilib.Joystick(0)

        self.drivetrain = subsystems.DriveTrain()

        self.initOI()

    def robotPeriodic(self):
        CommandBasedRobot.robotPeriodic(self)
        wpilib.SmartDashboard.putString("Drivetrain", self.drivetrain.getCurrentCommand().__class__.__name__)

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        CommandBasedRobot.teleopPeriodic(self)

    def autonomousInit(self):
        pass

    def disabledInit(self):
        pass

    def autonomousPeriodic(self):
        CommandBasedRobot.autonomousPeriodic(self)

    def initOI(self):
        buttons.JoystickButton(self.controller, robot_map.ds4["share"]).whenPressed(commands.drivetrain.EmergencyStop())

if __name__ == "__main__":
    wpilib.run(Lyra)
