import cv2


def video_split_without_IO(path_to_video_file):
    """
    Function to extract the original video as an image one frame at a time.
    The first argument is the path to the original video.
    The second argument is the path to save the extracted images.
    This function does not save split images in order to minimize the time to generate edited videos.
    """

    # load a video file
    capture = cv2.VideoCapture(path_to_video_file)

    images = []
    while True:
        is_image, frame_img = capture.read()
        if is_image:
            images.append(frame_img)
        else:
            break
    # when everything done, release the capture
    capture.release()
    return images


def video_split_with_IO(path_to_video_file, path_to_save_image):
    """
    Function to extract the original video as an image one frame at a time.
    The first argument is the path to the original video.
    The second argument is the path to save the extracted images.
    """

    # load a video file
    images = video_split_without_IO(path_to_video_file)

    capture = cv2.VideoCapture(path_to_video_file)
    digit = len(str(int(capture.get(cv2.CAP_PROP_FRAME_COUNT))))

    for i in range(len(images)):
        cv2.imwrite(path_to_save_image + '/image' + str(i).zfill(digit) + '.png', images[i])

    # when everything done, release the capture
    capture.release()
    return images
