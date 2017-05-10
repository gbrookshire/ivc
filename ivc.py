#!/usr/bin/env python

"""
Compute the Instantaneous Visual Change (IVC) from videos.

This module can either be imported into python or called directly:
> ./ivc.py <input_filename>
This will save a file with the same name as the video, replacing the
suffix with .csv.

This module relies on OpenCV and ffmpeg.
Install OpenCV3 (much faster than v2) with ffmpeg enabled.
On Mac, download using Homebrew: brew install opencv3 --with-ffmpeg
"""

__author__ = 'Geoffrey Brookshire'
__email__ = "geoff.brookshire@gmail.com"
__license__ = "MIT"

from __future__ import print_function
import warnings
import numpy as np
import cv2
if cv2.__version__ < '3.0':
    warnings.warn('This code will run much faster if you upgrade to OpenCV 3.')


def greyscale(image):
    """ Convert an OpenCV video frame to greyscale.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def ivc_from_array(video_frames):
    """
    Calculates the IVC given an array of video frames.
    This function requires loading the whole video into memory. For large
    video filess, this can be difficult. If you're directly computing the
    IVC of a video file, it's better to use the function ivc.ivc_from_file.

    video_frames: a 3-D array of greyscale video (time * width * height)
    """
    x = np.sum(np.diff(video_frames, axis=0) ** 2, axis=(1,2))
    x = np.append(0, x) # Make x the same length as the video
    return x


def ivc_from_file(filename):
    """
    Calculates the IVC given a video filename.

    To reduce memory load, this implementation only holds two
    video frames in memory at a time.
    """

    def ivc_frames(f1, f2):
        """ Helper function to compute VME on two adjacent frames.
        """
        x = np.sum(np.diff([f1.astype(np.int64),
                            f2.astype(np.int64)], axis=0) ** 2,
                   axis=(1,2))
        return x

    video_reader = cv2.VideoCapture(filename)

    # It's faster to append values to an empty list and then convert to array
    # than to use np.vstack, and faster than pre-allocating a numpy array.
    ivc_arr = np.array([0]) # array to hold the IVC

    prev_frame = None
    next_frame = None

    gotImage, image = video_reader.read()
    next_frame = greyscale(image)

    while True:
        gotImage, image = video_reader.read()
        if gotImage:
            prev_frame = next_frame
            next_frame = greyscale(image)
            x = ivc_frames(prev_frame, next_frame)
            ivc_arr = np.append(ivc_arr, x)
        else:
            break

    video_reader.release()
    return ivc_arr


if __name__ == '__main__':
    """ If called directly, compute IVC of videos and save a new .csv file.
    """
    import sys
    import os.path

    if len(sys.argv) == 2:
        inname = sys.argv[1]
        outname = os.path.splitext(inname)[0] + '.csv'
        ivc_arr = ivc_from_file(inname)
        f = file(outname, 'wb')
        f.writelines(str(e) + '\n' for e in ivc_arr)
        f.close()
    else:
        print("Usage:\n> ./ivc.py <input_filename>")
