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

Only tested with python 2.7, but it should also work with python 3+.

OpenCV must be installed using the `--with-ffmpeg` option.

To install OpenCV3 on a Mac:
```
brew install opencv3 --with-ffmpeg
```


# Usage

ivc can either be imported into python or run directly in the terminal.

## Calling `ivc.py` in the terminal

Calling `ivc.py` directly will save a file with the same name as the video, replacing the suffix with `.csv`.

`python ivc.py <input_filename>`.

## Importing ivc as a python module

This module includes functions to compute the IVC over an array of video frames, and given a filename. If you need to save the IVC for an entire video, use the filename method - it's faster and requires much less memory.

### Given a filename
```python
import ivc

video_filename = '/path/to/your/video'
output_filename = '/path/to/your/saved/csv'

ivc_arr = ivc.ivc_from_file(video_filename)
# Save as a csv
f = file(output_filename, 'wb')
f.writelines(str(e) + '\n' for e in ivc_arr)
f.close()
```

### Given an array of video frames
```python
import ivc
vid_frames = ... # Make sure this is a 3D numpy array (time * width * height)
ivc_arr = ivc.ivc_from_array(vid_frames)
```
