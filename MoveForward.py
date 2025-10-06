from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)

# Initialize the drive base. In this example, the wheel diameter is 56mm.
# The distance between the two wheel-ground contact points is 112mm.
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=86, axle_track=130)

# Optionally, uncomment the line below to use the gyro for improved accuracy.
drive_base.use_gyro(True)

# Set a driving speed (e.g., 100 mm/s)
drive_base.drive(100, 0)  # Move forward at 100 mm/s with 0 steering

# Drive forward by 500mm (half a meter).
drive_base.straight(100)

# Wait for 1 second
wait(1000)

# Turn left 90 degrees
drive_base.turn(-90)  # Negative angle for left turn

# Move straight for 50 cm (500 mm)
drive_base.straight(500)
