def get_trajectory_ids(dat_files):
    """
    Function to get a list of trajectory ids from Dat files.
    The argument is the path to read Dat files.
    """
    molecule_ids = []
    for dat_file in dat_files:
        try:
            molecule_ids.append(dat_file.split('/Mov2_')[1].split('.dat')[0])
        except IndexError:
            print("index is out of range")
        except AttributeError:
            print("attribute error")
    return molecule_ids
