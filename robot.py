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
        self.shooter = subsystems.Shooter()
        self.feeder = subsystems.Feeder()

        self.initOI()

    def robotPeriodic(self):
        CommandBasedRobot.robotPeriodic(self)
        wpilib.SmartDashboard.putString("Drivetrain", self.drivetrain.getCurrentCommand().__class__.__name__)
        wpilib.SmartDashboard.putString("Shooter", self.shooter.getCurrentCommand().__class__.__name__)
        wpilib.Feeder.putString("Feeder", self.feeder.getCurrentCommand().__class__.__name__)

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
        buttons.JoystickButton(self.controller, robot_map.ds4["l1"]).whileHeld(commands.shooter.Shoot())
        buttons.JoystickButton(self.controller, robot_map.ds4["circle"]).whenPressed(commands.feeder.Eat())
        buttons.JoystickButton(self.controller, robot_map.ds4["cross"]).whenPressed(commands.intakeRoller.Intake())
        buttons.JoystickButton(self.controller, robot_map.ds4["r1"]).whenPressed(commands.dropfeeder.Toggle())

if __name__ == "__main__":
    wpilib.run(Lyra)
