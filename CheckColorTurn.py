from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

def main():
    """Main function - color detection and turn program"""
    # Initialize both motors. The left motor turns counterclockwise to make the robot go forward.
    left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    right_motor = Motor(Port.E)
    
    # Initialize the drive base. Wheel diameter is 86mm, axle track is 130mm.
    drive_base = DriveBase(left_motor, right_motor, wheel_diameter=86, axle_track=146)
    
    # Initialize the color sensor on Port B
    color_sensor_b = ColorSensor(Port.B)
    
    # Optionally, use the gyro for improved accuracy (uncomment if available).
    # drive_base.use_gyro(True)
    
    # Set a driving speed (e.g., 100 mm/s)
    drive_base.drive(100, 0)  # Move forward at 100 mm/s with 0 steering
    
    # Move forward until the color sensor on Port B detects non-white
    while color_sensor_b.color() != Color.GREEN:
        pass  # Loop continues until non-white is detected
    
    # Stop the drive base when non-white is detected
    drive_base.stop()
    
    # Wait for 1 second
    wait(1000)
    
    # Turn left 90 degrees
    drive_base.turn(-90)  # Negative angle for left turn
    
    # Move straight for 50 cm (500 mm)
    drive_base.straight(500)

if __name__ == "__main__":
    main()
