import cv2


color = {
    'pink': [255, 0, 255],
    'purple': [128, 0, 128],
    'blue': [255, 0, 0],
    'yellow': [0, 255, 255],
    'red': [0, 0, 255],
}


def parse_to_int(num):
    if (type(num) == str):
        return int(num)
    else:
        return num


def draw_trajectory_without_IO(image, current_frame_index, frame_edition_options_of_specific_molecule):
    for edit_option_i in range(len(frame_edition_options_of_specific_molecule)):
        if edit_option_i == 0:
            difference_of_frame_indexes_between_start_and_end_to_draw_line = 0
        else:
            frame_index_difference = frame_edition_options_of_specific_molecule[edit_option_i].frame_index - frame_edition_options_of_specific_molecule[edit_option_i-1].frame_index
            is_previous_trajectory_drawn_in_frame = frame_edition_options_of_specific_molecule[edit_option_i-1].does_draw_trajectory
            if frame_index_difference == 1 and is_previous_trajectory_drawn_in_frame:
                difference_of_frame_indexes_between_start_and_end_to_draw_line = 1
            else:
                difference_of_frame_indexes_between_start_and_end_to_draw_line = 0
        if frame_edition_options_of_specific_molecule[edit_option_i].does_draw_trajectory:
            is_current_frame_before_end = current_frame_index <= parse_to_int(frame_edition_options_of_specific_molecule[edit_option_i].frame_index_until_which_trajectory_is_drawn)
            is_edit_option_i_before_currrent_frame = edit_option_i <= current_frame_index
            if is_current_frame_before_end and is_edit_option_i_before_currrent_frame:
                cv2.line(
                    image,
                    (
                        frame_edition_options_of_specific_molecule[edit_option_i - difference_of_frame_indexes_between_start_and_end_to_draw_line].x,
                        frame_edition_options_of_specific_molecule[edit_option_i - difference_of_frame_indexes_between_start_and_end_to_draw_line].y
                    ),
                    (
                        frame_edition_options_of_specific_molecule[edit_option_i].x,
                        frame_edition_options_of_specific_molecule[edit_option_i].y
                    ),
                    (
                        color[frame_edition_options_of_specific_molecule[edit_option_i].trajectory_color][0],
                        color[frame_edition_options_of_specific_molecule[edit_option_i].trajectory_color][1],
                        color[frame_edition_options_of_specific_molecule[edit_option_i].trajectory_color][2],
                    ),
                    1
                )
    return image


def draw_trajectory_with_IO(image, current_frame_index, frame_edition_options_of_specific_molecule, path_to_save):
    pass
