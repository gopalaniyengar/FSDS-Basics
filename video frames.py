import sys, os
fsds_lib_path = os.path.join(os.path.expanduser("~"), "Formula-Student-Driverless-Simulator", "python")
sys.path.insert(0, fsds_lib_path)
import time
import fsds

# connect to the simulator
client = fsds.FSDSClient()

# Check network connection, exit if not connected
client.confirmConnection()

def ms():
    return time.time_ns()//1000000

count=0
tframe=1000/30
t1=ms()
t2=t1+tframe
while count<900:
    if t2-t1>=tframe:
        [image] = client.simGetImages(
            [fsds.ImageRequest(camera_name='cam1', image_type=fsds.ImageType.Scene, pixels_as_float=False, compress=True)],
            vehicle_name='FSCar')
        fname=f"images/{count}.png"
        fsds.write_file(os.path.normpath(fname), image.image_data_uint8)
        count+=1
        t1=t2
        t2=ms()
    else:
        t2=ms()



