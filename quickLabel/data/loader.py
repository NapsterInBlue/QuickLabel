import cv2


def load_image_data(fpath):
    '''
    Given a csv with columns (image filepath, numeric score)

    Note: Also resolves inconsistencies in image size per

    Parameters
    ----------
    fpath: str, pathlike
        Location of the csv you want to read from
    
    Returns
    -------
    X: numpy.array
        The numpy representation for each image in (R, G, B)
    y: 
    '''

    max_height, max_width = get_max_image_dims(fpath)

    print(max_height, max_width)

def get_max_image_dims(fpath):
    '''
    Open up all of the images to see their heights and widths.
    Keep a running max for each, which is returned at the end.
    '''

    max_height = 0
    max_width = 0

    with open(fpath) as f:
        for row in f:
            im_path = row.split(';')[0]
            im = cv2.imread(im_path)
            height, width, _ = im.shape

            if height > max_height:
                max_height = height

            if width > max_width:
                max_width = width

    return max_height, max_width
