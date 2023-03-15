from glob import glob


def count_frame(original_images_path):
    """
    Function to count the number of images extracted from the original video one frame at a time.
    The argument is the path to the images extracted one frame at a time from the original video.
    """
    frame_list = glob(original_images_path + '/*.png')
    number_of_frame = len(frame_list)
    return number_of_frame
