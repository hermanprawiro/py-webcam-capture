import argparse

import cv2

"""
Camera ID:
- 0: Ganzin Eye Camera
- 1: Ganzin Scene Camera

Resolution:
Ganzin Eye Camera: 400 x 400
Ganzin Scene Camera:
- 560 x 480 (Default)
- 704 x 600
- 848 x 768
- 1328 x 1200
"""

def build_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("camera_id", type=int, default=0, help="Camera ID (Default=0)")
    parser.add_argument("--width", type=int, default=0, help="Width of the webcam frame (Default=0, device default)")
    parser.add_argument("--height", type=int, default=0, help="Height of the webcam frame (Default=0, device default)")
    return parser

def main(camera_id: int = 0, camera_width: int = 0, camera_height: int = 0):
    # Open the webcam
    cap = cv2.VideoCapture(camera_id)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()

    # Print the webcam properties
    print(f"Webcam Default Properties:")
    out_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    out_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out_fps = cap.get(cv2.CAP_PROP_FPS)
    print(f" - Width: {out_width}")
    print(f" - Height: {out_height}")
    print(f" - FPS: {out_fps}")

    # Set the webcam resolution
    if camera_width > 0 and camera_height > 0:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)
        print(f"Set webcam resolution to {camera_width} x {camera_height}")
        # Print the webcam properties
        print(f"Current Webcam Properties:")
        out_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        out_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out_fps = cap.get(cv2.CAP_PROP_FPS)
        print(f" - Width: {out_width}")
        print(f" - Height: {out_height}")
        print(f" - FPS: {out_fps}")

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # If frame is read correctly, ret is True
        if not ret:
            print("Error: Can't receive frame (stream end?). Exiting ...")
            break

        # Display the resulting frame
        cv2.imshow('Webcam Video', frame)
        
        # Press 'q' on the keyboard to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    args = build_argparser().parse_args()

    if args.camera_id < 0:
        print("Error: Camera ID must be a positive integer.")
        exit()

    if args.width < 0:
        print("Error: Width must be a positive integer.")
        exit()
    
    if args.height < 0:
        print("Error: Height must be a positive integer.")
        exit()

    main(args.camera_id, args.width, args.height)