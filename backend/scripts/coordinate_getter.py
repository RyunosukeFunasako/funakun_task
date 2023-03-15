import pandas as pd
import re
from glob import glob


def get_coordinate(path_to_dat_directory):
    """
    Function to extract frame number and coordinate data from a Dat file.
    The argument is the path to read the Dat file.
    """
    # read dat files as data frames delimited by whitespace
    readed_dat = pd.read_csv(path_to_dat_directory, delim_whitespace=True, header=None)
    # delete missing columns
    normalized_columns = readed_dat.dropna(how='all', axis=1)
    # change column name
    renamed_columns = normalized_columns.rename(columns={normalized_columns.columns[0]: 'frame_number', normalized_columns.columns[1]: 'x_position', normalized_columns.columns[2]: 'y_position'})
    # extraction of required columns
    required_columns = renamed_columns[['frame_number', 'x_position', 'y_position']]
    # extraction of required values (as ndarray)
    required_value = required_columns.values
    return required_value.astype(int)


def generate_dict_of_molecules_info(path_to_dat_directory):
    molecules_info_dict = {}
    for dat_file_path in glob(path_to_dat_directory + "/*.dat"):
        molecule_id_regrex = r'(.+).dat'
        molecule_id = int(re.search(molecule_id_regrex, dat_file_path.split('_')[-1]).group(1))
        coordinate_info_list = get_coordinate(dat_file_path)
        molecules_info_dict[molecule_id] = {}
        for coordinate_list in coordinate_info_list:
            molecules_info_dict[molecule_id][int(coordinate_list[0])] = {
                'x': int(coordinate_list[1]),
                'y': int(coordinate_list[2])
            }
    return molecules_info_dict


def generate_default_frame_edit_option_dict(path_to_dat_directory):
    molecules_info_dict = generate_dict_of_molecules_info(path_to_dat_directory)
    default_frame_edit_option_dict = {}
    for molecule_id in molecules_info_dict.keys():
        for frame_id in molecules_info_dict[molecule_id]:
            if frame_id not in default_frame_edit_option_dict.keys():
                default_frame_edit_option_dict[frame_id] = {}
            default_frame_edit_option_dict[frame_id][molecule_id] = {
                'molecule_id': molecule_id,
                'frame_index': frame_id,
                'x': molecules_info_dict[molecule_id][frame_id]['x'],
                'y': molecules_info_dict[molecule_id][frame_id]['y'],
                'does_draw_figure': False,
                'figure_shape': 'circle',
                'figure_color': 'yellow',
                'does_draw_trajectory': False,
                'trajectory_color': 'yellow',
                'frame_index_until_which_trajectory_is_drawn': 0,
                'figure_edit_box_id': -1,
                'trajectory_edit_box_id': -1
            }
    return default_frame_edit_option_dict
