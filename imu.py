# Args:
#   imu_name (str, optional): Name of IMU to get data from, specified in settings.json. When no name is provided the last imu will be used.
#   vehicle_name (str, optional): Name of vehicle to which the sensor corresponds to.
#
# Returns:
#   time_stamp (np.uint64) nanosecond timestamp of when the imu data was captured
#   orientation (Quaternionr) rotation of the sensor, relative to the northpole. It's like a compass
#   angular_velocity (Vector3r) how fast the car is rotating along it's three axis in radians/second
#   linear_acceleration (Vector3r) how fast the car is accelerating in meters/s2^m

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
    imu = client.getImuData(imu_name = 'Imu', vehicle_name = 'FSCar')

    print("timestamp nano: ", imu.time_stamp)
    print("orientation: ", imu.orientation)
    print("angular velocity: ", imu.angular_velocity)
    print("linear acceleration: ", imu.linear_acceleration)
    print()
    time.sleep(1)
    t+=1
client.reset()
