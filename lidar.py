#Args:
#   lidar_name (str, optional): Name of Lidar to get data from, specified in settings.json. With no name provided selects the last lidar in the settings.json.
#   vehicle_name (str, optional): Name of vehicle to which the sensor corresponds to, by default FSCar.

#Returns:
#   point_cloud (array of float): The points in the pointcloud.
#   time_stamp (np.uint64): nanosecond timestamp of when the gps position was captured
#   pose (Pose): position (Vector3r) and orientation (Quaternionr) of the location of the lidar at the moment of capture in global reference frame

import sys, os
fsds_lib_path = os.path.join(os.path.expanduser("~"), "Formula-Student-Driverless-Simulator", "python")
sys.path.insert(0, fsds_lib_path)

import time
import fsds
import numpy

# connect to the AirSim simulator
client = fsds.FSDSClient()

# Check network connection
client.confirmConnection()

client.enableApiControl(True)
client.reset()
car_controls = fsds.CarControls()
car_controls.throttle = 1
client.setCarControls(car_controls)
time.sleep(0.25)
car_controls.throttle = 0
client.setCarControls(car_controls)

lidardata = client.getLidarData(lidar_name = 'Lidar1')

# nanosecond timestamp of when the imu frame was captured
print("lidardata nano: ", lidardata.time_stamp)

# the location of the lidar at the moment of capture in global reference frame
print("lidar pose: ", lidardata.pose)

def parse_lidarData(pointcloud):
    """
    Takes an array of float points and converts it into an array with 3-item arrays representing x, y and z
    """
    points = numpy.array(pointcloud, dtype=numpy.dtype('f4'))
    return numpy.reshape(points, (int(points.shape[0]/3), 3))

points = parse_lidarData(lidardata.point_cloud)

print("number of hit points: ", len(points))

for i,point in enumerate(points):
    x = point[0]
    y = point[1]
    z = point[2]
    print("point %i- X: %f, Y: %f, Z: %f" % (i,x,y,z))