from wpilib import command
import commands, robot_map, wpilib, subsystems
                                     
#    _/  _/    _/_/_/_/    _/    _/  _/   
#   _/  _/    _/        _/  _/  _/  _/    
#  _/_/_/_/  _/_/_/    _/  _/  _/_/_/_/   
#     _/          _/  _/  _/      _/      
#    _/    _/_/_/      _/        _/  

class GRAPE(wpilib.TimedRobot):
    def robotInit(self):
        wpilib.TimedRobot.__init__(self)

        command.Command.getRobot = lambda: self

        self.compressor = wpilib.Compressor()
        self.controller = wpilib.Joystick(0)
        self.indefector = wpilib.Solenoid(1)

        self.drivetrain = subsystems.DriveTrain()

        self.initOI()

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        pass

    def autonomousInit(self):
        pass

    def disabledInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def disabledPeriodic(self):
        pass

    def initOI(self):
        wpilib.buttons.JoystickButton(self.controller, robot_map.ds4["share"]).whenPressed(commands.drivetrain.EmergencyStop())

if __name__ == "__main__":
    wpilib.run(GRAPE)
