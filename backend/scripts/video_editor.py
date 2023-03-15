import video_info_getter
import video_splitter
import figure_drawer
import trajectory_drawer
import video_writer


class MoleculeEditOption:
    def __init__(self, molecule_id, molecule_edit_option):
        self.molecule_id = molecule_id
        self.frame_index = molecule_edit_option['frame_index']
        self.x = molecule_edit_option['x']
        self.y = molecule_edit_option['y']
        self.does_draw_figure = molecule_edit_option['does_draw_figure']
        self.figure_shape = molecule_edit_option['figure_shape']
        self.figure_color = molecule_edit_option['figure_color']
        self.does_draw_trajectory = molecule_edit_option['does_draw_trajectory']
        self.trajectory_color = molecule_edit_option['trajectory_color']
        self.frame_index_until_which_trajectory_is_drawn = molecule_edit_option['frame_index_until_which_trajectory_is_drawn']
        self.figure_edit_box_id = molecule_edit_option['figure_edit_box_id']
        self.trajectory_edit_id = molecule_edit_option['trajectory_edit_box_id']


class FrameEditOptions:
    def __init__(self, frame_edit_options_dict):
        self.frame_edit_options = {}
        for frame_index in frame_edit_options_dict.keys():
            self.frame_edit_options[frame_index] = {}
            for molecule_id in frame_edit_options_dict[frame_index]:
                self.frame_edit_options[frame_index][molecule_id] = MoleculeEditOption(molecule_id, frame_edit_options_dict[frame_index][molecule_id])


def get_molecule_edit_options(frame_edit_options_dict):
    frame_edit_options = FrameEditOptions(frame_edit_options_dict)
    molecule_edit_options_dict = {}
    for frame_index in frame_edit_options.frame_edit_options.keys():
        for molecule_id in frame_edit_options.frame_edit_options[frame_index].keys():
            if molecule_id not in molecule_edit_options_dict:
                molecule_edit_options_dict[molecule_id] = []
            molecule_edit_options_dict[molecule_id].append(frame_edit_options.frame_edit_options[frame_index][molecule_id])
    return molecule_edit_options_dict


def generate_edited_video(path_to_original_video_file, path_to_edited_video_file, path_to_dir_of_dat_files, frame_edit_options_dict):
    fps, width, height = video_info_getter.get_video_info(path_to_original_video_file)
    frame_edit_options = FrameEditOptions(frame_edit_options_dict)
    molecule_edit_options_dict = get_molecule_edit_options(frame_edit_options_dict)
    images = video_splitter.video_split_without_IO(path_to_original_video_file)
    edited_images = []
    for frame_i in range(len(images)):
        image = images[frame_i]
        for molecule_id in molecule_edit_options_dict.keys():
            if molecule_id in frame_edit_options.frame_edit_options[str(frame_i)].keys():
                image = figure_drawer.draw_figure_without_IO(image, frame_edit_options.frame_edit_options[str(frame_i)][molecule_id])
                image = trajectory_drawer.draw_trajectory_without_IO(image, frame_i, molecule_edit_options_dict[molecule_id])
        edited_images.append(image)
    video_writer.video_write(path_to_edited_video_file, fps, width, height, edited_images)


def generate_edited_video_with_IO(path_to_original_video_file, path_to_edited_video_file, path_to_dir_of_dat_files, frame_edit_options_list):
    pass
