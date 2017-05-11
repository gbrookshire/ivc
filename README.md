# ivc

ivc is a small Python module to compute the Instantaneous Visual Change of videos.

++++ CITATION

# Requiements

- python 2.7+
- numpy
- ffmpeg
- OpenCV3

Only tested with python 2.7, but it should work with few or no changes in python 3+.

To install OpenCV3 on a Mac:
```
brew install opencv3 --with-ffmpeg
```

# Usage

ivc can either be imported into python or run in the terminal:
`python ivc.py <input_filename>`.
Calling the `ivc.py` directly will save a file with the same name as the video, replacing the suffix with `.csv`.
