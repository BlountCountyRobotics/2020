import wpilib
import subsystems

class GRAPE(wpilib.TimedRobot):
    def robotInit(self):
        self.compressor = wpilib.Compressor()
        self.controller = wpilib.Joystick(0)
        self.indefector = wpilib.Solenoid(1)

        self.drivetrain = subsystems.DriveTrain()

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

if __name__ == "__main__":
    wpilib.run(GRAPE)
        
        
