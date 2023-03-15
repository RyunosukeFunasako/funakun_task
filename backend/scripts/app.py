import os
import tempfile
from datetime import datetime
import pytz
from glob import glob
from video_editor import generate_edited_video


path_to_original_video_file = './data/original/video/'
path_to_edited_video_file = './data/edited/video/'
path_to_dat_files = './data/dat_files/'
path_to_molecule_coordinates_json = './data/json/'


def generate_video_without_IO():
    for file_to_delete in glob(path_to_edited_video_file + '*'):
        if os.path.isfile(file_to_delete):
            os.remove(file_to_delete)
    frame_edit_options_dict = {}
    file_to_original_video = ''
    for path_to_file in glob(path_to_original_video_file + '*'):
        if os.path.isfile(path_to_file):
            file_to_original_video = path_to_file
    now = datetime.now(pytz.timezone('Asia/Tokyo'))
    file_name = now.strftime("%Y%m%d_%H-%M-%S")
    with tempfile.TemporaryDirectory() as temp_dir:
        # 一時ディレクトリに動画書き出し
        generate_edited_video(file_to_original_video, temp_dir + ".mp4", path_to_dat_files, frame_edit_options_dict)
        # codecをh264に変更
        os.system(f"ffmpeg -i {temp_dir}.mp4 -vcodec libx264 -f mp4 {path_to_edited_video_file + file_name}.mp4")
    return

generate_video_without_IO()
