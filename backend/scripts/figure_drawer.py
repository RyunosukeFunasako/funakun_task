import cv2


color = {
    'pink': [255, 0, 255],
    'purple': [128, 0, 128],
    'blue': [255, 0, 0],
    'yellow': [0, 255, 255],
    'red': [0, 0, 255],
}


def draw_figure_without_IO(image, molecule_edit_option):
    if molecule_edit_option.does_draw_figure:
        if molecule_edit_option.figure_shape == 'circle':
            cv2.circle(
                image,
                (
                    molecule_edit_option.x,
                    molecule_edit_option.y
                ),
                8,
                (
                    color[molecule_edit_option.figure_color][0],
                    color[molecule_edit_option.figure_color][1],
                    color[molecule_edit_option.figure_color][2]
                ),
                thickness=1,
                lineType=cv2.LINE_AA
            )
        elif molecule_edit_option.figure_shape == 'square':
            cv2.rectangle(
                image,
                (
                    molecule_edit_option.x - 8,
                    molecule_edit_option.y + 8
                ),
                (
                    molecule_edit_option.x + 8,
                    molecule_edit_option.y - 8
                ),
                (
                    color[molecule_edit_option.figure_color][0],
                    color[molecule_edit_option.figure_color][1],
                    color[molecule_edit_option.figure_color][2]
                ),
                thickness=1,
                lineType=cv2.LINE_AA
            )
    return image


def draw_figure_with_IO(image, molecule_edit_option, path_to_save):
    pass
