import cv2
import numpy as np


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

    X = []
    y = []

    with open(fpath) as f:
        for row in f:
            impath, score = row.split(';')

            im = load_and_pad_images(impath, max_height, max_width)

            X.append(im)
            y.append(float(score))

    X = np.array(X)
    y = np.array(y)

    return X, y



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

    print('Max height:', max_height)
    print('Max width :', max_width)

    return max_height, max_width


def load_and_pad_images(impath, max_height, max_width):
    '''
    Iterate though all of the image filepaths, load the 
    images, then pad them with black, if necessary
    '''
    imBGR = cv2.imread(impath)
    im = cv2.cvtColor(imBGR, cv2.COLOR_BGR2RGB)

    height_needed, width_needed = determine_pad_amount(im, max_height,
                                                       max_width)

    im = np.pad(im, ((0, height_needed), (0, width_needed), (0, 0)),
                mode='constant', constant_values=0)

    return im


def determine_pad_amount(image_array, max_height, max_width):
    '''
    Given an image and desired max height/width,
    find how much height and width is needed to make
    the image the appropriate size
    '''

    height, width, _ = image_array.shape

    height_needed = max_height - height
    width_needed = max_width - width

    return height_needed, width_needed
