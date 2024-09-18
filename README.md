# Capture Webcam Video

## Environment
The code is tested on the following environment:
- Python 3.10
- OpenCV 4.7.0.72
- pygrabber 0.2 (optional, for checking available cameras in check_devices.py)

## Usage (Quick)
1. Run `check_devices.py` to check available cameras. The script will print out the available cameras and their IDs.
2. Run `main.py <camera_id>` to start capturing video from the camera. By default, the camera ID is 1 and the resolution is 1920 x 1080.

Press `q` to exit the video capture, press `r` or `space bar` to start/stop recording. 

The recorded video will be saved in the `output` folder (will be created if not exist).

Example:
```bash
python main.py # Default camera ID is 1 and resolution is 1920 x 1080

python main.py 0 # Use camera with ID 0 and resolution is 1920 x 1080
python main.py 1 --width 1328 --height 1200 # Use camera with ID 1 and set resolution to 1328 x 1200
```

## Usage (Detailed)
1. Run `check_devices.py` to check available cameras. The script will print out the available cameras and their IDs.
2. Run `check_opencv.py` with the camera ID to check if the camera is working properly. Press `q` to exit the video capture.
3. Run `main.py` to start capturing video from the camera. Press `q` to exit the video capture, press `r` or `space bar` to start/stop recording. The recorded video will be saved in the `output` folder (will be created if not exist).

### Step 1: Check Available Cameras
```bash
# Check available cameras
python check_devices.py

# Device Index: 0, Device Name: Ganzin Eye Camera
# Device Index: 1, Device Name: Ganzin Scene Camera
# Device Index: 2, Device Name: OBS Virtual Camera
```
It will print out the available cameras and their IDs. In this case, we have 3 cameras with IDs 0, 1, and 2. We want to use the Scene Camera (RGB) with device index 1.


### Step 2: Check Camera and OpenCV
Next, we will check if the camera and OpenCV are working properly.
```bash
python check_opencv.py 1

# Webcam Default Properties:
#  - Width: 560
#  - Height: 480
#  - FPS: 30.0
```
It will print out the default properties of the camera. In this case, the Scene Camera has a resolution of 560x480 pixels and a frame rate of 30 FPS. We can now start capturing video from the camera. However, the Scene Camera has different resolution settings, listed below:
* 560 x 480 (Default)
* 704 x 600
* 848 x 768
* 1328 x 1200

We can test the camera with different resolutions by changing the `width` and `height` variables in the `main.py` and `check_opencv.py` script. For example, to use the 1328 x 1200 resolution, we can set the `width` and `height` variables as follows:
```bash
python check_opencv.py 1 --width 1328 --height 1200

# Webcam Default Properties:
#  - Width: 560
#  - Height: 480
#  - FPS: 30.0
# Set webcam resolution to 1328 x 1200
# Current Webcam Properties:
#  - Width: 1328
#  - Height: 1200
#  - FPS: 30.0
```

Actually, we can select arbitrary resolution and the closest resolution will be selected by the camera. For example, if we set the resolution to 1920 x 1080, the camera will select the closest resolution available, which is 1328 x 1200.

### Step 3: Capture Video
Finally, we can start capturing video from the camera using the `main.py` script. 

Press `q` to exit the video capture, press `r` or `space bar` to start/stop recording. The recorded video will be saved in the `output` folder (will be created if not exist).

```bash
python main.py # Default camera ID is 1 and resolution is 1920 x 1080

python main.py 0 # Use camera with ID 0 and resolution is 1920 x 1080
python main.py 1 --width 1328 --height 1200 # Use camera with ID 1 and set resolution to 1328 x 1200
```