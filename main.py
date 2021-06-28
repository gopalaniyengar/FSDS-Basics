# This code adds the fsds package to the python path.
# It assumes the fsds repo is cloned in the home directory.
# Replace fsds_lib_path with a path to wherever the python directory is located.
import sys, os
fsds_lib_path = os.path.join(os.path.expanduser("~"), "Formula-Student-Driverless-Simulator", "python")
sys.path.insert(0, fsds_lib_path)

import time
import fsds

# connect to the AirSim simulator
client = fsds.FSDSClient()

# Check network connection
client.confirmConnection()

# After enabling api control only the api can control the car.
# Direct keyboard and joystick into the simulator are disabled.
# If you want to still be able to drive with the keyboard while also
# control the car using the api, call client.enableApiControl(False)
client.enableApiControl(True)

# Instruct the car to go full-speed forward
car_controls = fsds.CarControls()
car_controls.throttle = 1
client.setCarControls(car_controls)

time.sleep(2.5)
state = client.getCarState()

# velocity in m/s in the car's reference frame
print(state.speed)

# nanosecond timestamp of the latest physics update
print(state.timestamp)

# position (meter) in global reference frame.
print(state.kinematics_estimated.position)

# orientation (Quaternionr) in global reference frame.
print(state.kinematics_estimated.orientation)

# m/s
print(state.kinematics_estimated.linear_velocity)

# rad/s
print(state.kinematics_estimated.angular_velocity)

# m/s^2
print(state.kinematics_estimated.linear_acceleration)

# rad/s^2
print(state.kinematics_estimated.angular_acceleration)

time.sleep(2.5)

# Places the vehicle back at it's original position
client.reset()