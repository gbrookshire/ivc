# ivc

ivc is a small Python module to compute the Instantaneous Visual Change of videos.

Described in: Brookshire, Lu, Nusbaum, Goldin-Meadow, Casasanto (In Press) Visual cortex entrains to sign language. *Proceedings of the National Academy of Sciences*.


# Algorithm
The IVC represents a time-series of aggregated visual change between video frames, and is computed as the sum of squared differences in each pixel across sequential frames:

![alt text](https://github.com/gbrookshire/ivc/blob/master/ivc-eq.png "IVC")

where *x* is the grayscale value of pixel *i* at time *t*.


# Requiements

- python 2.7+
- numpy
- [ffmpeg](https://ffmpeg.org/download.html)
- [OpenCV3](http://opencv.org/releases.html)

Only tested with python 2.7, but it should also work python 3+.

OpenCV must be installed using the `--with-ffmpeg` option.

To install OpenCV3 on a Mac:
```
brew install opencv3 --with-ffmpeg
```


# Usage

ivc can either be imported into python or run in the terminal:
`python ivc.py <input_filename>`.
Calling the `ivc.py` directly will save a file with the same name as the video, replacing the suffix with `.csv`.

This module includes functions to compute the IVC over an array of video frames, and over
