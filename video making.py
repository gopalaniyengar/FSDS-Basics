import sys, os
fsds_lib_path = os.path.join(os.path.expanduser("~"), "Formula-Student-Driverless-Simulator", "python")
sys.path.insert(0, fsds_lib_path)
import time
import fsds
from PIL import Image
import cv2
from moviepy.editor import *

# connect to the simulator
client = fsds.FSDSClient()

# Check network connection, exit if not connected
client.confirmConnection()

#get dimensions of iamge
[image] = client.simGetImages(
    [fsds.ImageRequest(camera_name='cam1', image_type=fsds.ImageType.Scene, pixels_as_float=False,
                       compress=True)],
    vehicle_name='FSCar')
testimg="example.png"
fsds.write_file(os.path.normpath(testimg), image.image_data_uint8)
frame = cv2.imread(testimg)
height, width, layers = frame.shape
#print(height,width,layers)


def ms():
    return time.time_ns()//1000000

def frames_gen():
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

def vid_gen_from_frames():
    os.chdir("D:\\Python Projects\\FSD Sim\\images")
    image_folder = '.'  # make sure to use your folder
    video_name = 'video30fps.avi'

    images = [img for img in os.listdir(image_folder)
              if img.endswith(".jpg") or
              img.endswith(".jpeg") or
              img.endswith("png")]

    # Array images should only consider
    # the image files ignoring others if any
    #print(images)

    frame = cv2.imread(os.path.join(image_folder, images[0]))

    # setting the frame width, height width
    # the width, height of first image
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 30, (width, height))


    # Appending the images to the video one by one
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
    # Deallocating memories taken for window creation
    cv2.destroyAllWindows()
    video.release()  # releasing the video generated


fps=60

def video_direct():
    video_name = f"video_direct_{fps}.avi"
    os.chdir("D:\\Python Projects\\FSD Sim\\images")
    count=0
    tstart=ms()
    tend=ms()

    video = cv2.VideoWriter(video_name, 0, fps, (width, height))

    while (tend-tstart)<60000:
    #while count<(fps*15):
        [image] = client.simGetImages(
            [fsds.ImageRequest(camera_name='cam1', image_type=fsds.ImageType.Scene, pixels_as_float=False,
                               compress=True)],
            vehicle_name='FSCar')
        fname = f"{count}.png"
        fsds.write_file(os.path.normpath(fname), image.image_data_uint8)
        video.write(cv2.imread(os.path.normpath(fname)))

        count+=1
        tend=ms()

    cv2.destroyAllWindows()
    video.release()

def slow_vid():
    video_name = f"video_direct_{fps}.avi"
    os.chdir("D:\\Python Projects\\FSD Sim\\images")
    clip = VideoFileClip(video_name)

    os.chdir("D:\\Python Projects\\FSD Sim\\video_output")
    #clip = clip.subclip(0, 5)
    final = clip.fx(vfx.speedx, 0.5)
    final.write_videofile(f"video_direct_slow_{fps}.mp4", fps=clip.fps)

video_direct()
slow_vid()