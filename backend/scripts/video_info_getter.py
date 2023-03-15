import cv2


def get_video_info(video_path):
    """
    Function to extract the fps, width, and height of a video

    Returns fps, width, and height
    """
    # load a video file
    capture = cv2.VideoCapture(video_path)

    # get the fps of the loaded video file
    fps = capture.get(cv2.CAP_PROP_FPS)

    # get the width and height of a video
    while True:
        is_image, frame_img = capture.read()
        if is_image:
            # get the size of the image
            height, width = frame_img.shape[:2]
            break

    # when everything done, release the capture
    capture.release()
    return fps, width, height
