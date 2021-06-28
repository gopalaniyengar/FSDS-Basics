# Args:
#   vehicle_name (str, optional): Name of vehicle to which the sensor corresponds to.
# Returns:
#   time_stamp (np.uint64): nanosecond timestamp of when the gss data was captured
#   linear_velocity (Vector3r): velocity in m/s of the car in world reference frame

import sys, os
fsds_lib_path = os.path.join(os.path.expanduser("~"), "Formula-Student-Driverless-Simulator", "python")
sys.path.insert(0, fsds_lib_path)

import time
import fsds

# connect to the AirSim simulator
client = fsds.FSDSClient()

# Check network connection
client.confirmConnection()


client.enableApiControl(True)
client.reset()
car_controls = fsds.CarControls()
car_controls.throttle = 1
client.setCarControls(car_controls)

t=0
while t<5:
    gss = client.getGroundSpeedSensorData(vehicle_name='FSCar')

    print("timestamp nano: ", gss.time_stamp)
    print("linear_velocity: ", gss.linear_velocity)
    print()

    time.sleep(1)
    t+=1
client.reset()