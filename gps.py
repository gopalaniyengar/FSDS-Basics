# Args:
#   gps_name (str, optional): Name of GPS to get data from, specified in settings.json. When no name is provided the last gps will be used.
#   vehicle_name (str, optional): Name of vehicle to which the sensor corresponds to.
# Returns:
#   time_stamp (np.uint64): nanosecond timestamp of when the gps position was captured
#   gnss:
#     eph (float): Standard deviation of horizontal position error (meters)
#     epv (float): Standard deviation of vertical position error (meters)
#     geo_point: The altitude, latitude and longitude of the gps
#       latitude (float)
#       longitude (float)
#       altitude (float)
#     velocity (Vector3r): Velocity in three directions (x_val, y_val and z_val) in meter/second
#     time_utc (np.uint64): UTC millisecond timestamp of when the gps position was captured

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
    gps = client.getGpsData(gps_name = 'Gps', vehicle_name = 'FSCar')

    print("timestamp nano: ", gps.time_stamp)
    print("timestamp utc:  ", gps.gnss.time_utc)
    print("eph: ", gps.gnss.eph)
    print("epv: ", gps.gnss.epv)
    print("geo point: ", gps.gnss.geo_point)
    print("velocity: ", gps.gnss.velocity)
    print()

    time.sleep(1)
    t+=1

client.reset()