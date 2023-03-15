import sys
import cv2


def video_write(path_to_write_video, fps, width, height, edited_images):
    """
    Function to create a video from the plotted images.
    The first argument is the number of images extracted from the original video one frame at a time.
    The second argument is the path to save the created video.
    The third argument is the path to the plotted images.
    The fourth argument is the fps of the video to create.
    The fifth argument is the width of the video to create.
    The sixth argument is the height of the video to create.
    """
    # define the codec and create VideoWriter object
    # ↓Webブラウザ上で再生するにはh264のcodecが必要
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(path_to_write_video, fourcc, fps, (width, height))
    # terminate the system if the video cannot be loaded properly
    if not video.isOpened():
        print("can't be opened")
        sys.exit()
    for image in edited_images:
        # create a video from the plotted images
        video.write(image)
    # when everything done, release the video
    video.release()