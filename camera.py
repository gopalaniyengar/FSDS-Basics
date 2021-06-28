import sys, os
fsds_lib_path = os.path.join(os.path.expanduser("~"), "Formula-Student-Driverless-Simulator", "python")
sys.path.insert(0, fsds_lib_path)
import time
import fsds

# connect to the simulator 
client = fsds.FSDSClient()

# Check network connection, exit if not connected
client.confirmConnection()

# Get the image
#   color
[image] = client.simGetImages([fsds.ImageRequest(camera_name = 'cam1', image_type = fsds.ImageType.Scene, pixels_as_float = False, compress = True)], vehicle_name = 'FSCar')
#   depth
#[image] = client.simGetImages([fsds.ImageRequest(camera_name = 'cam2', image_type = fsds.ImageType.DepthPerspective, pixels_as_float = False, compress = True)], vehicle_name = 'FSCar')

#print("Image width: ", image.width)
#print("Image height: ", image.height)

# write to png 
fsds.write_file(os.path.normpath('example.png'), image.image_data_uint8)