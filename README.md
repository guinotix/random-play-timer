<center>
    <strong>
        <span style="font-size: 2.8em">
            Random Play Timer
        </span>
    </strong>
</center>

### Table of Contents
- [About RPT](#about-rpt)
- [Features](#features)
- [Usage](#usage)
- [Future Improvements](#future-improvements)

## About RPT

RPT is a simple Python script that generates a random timestamp of a song.

## Features

RPT uses TinyTag to access metadata of the songs.  
Also Python 3.7+ is used.

## Usage

1. Create a `files` folder in the project directory and move the audio files there.
2. Then, open a terminal from the project directory and execute the script:
```
python .\rpt.py
```

3. This will produce an output like this (I used a Suns of the Tundra album as an example):
```
[Murmuration, Duration: 5:34, Play from: 2:41]
[Each of Us, Duration: 5:03, Play from: 3:16]
[Sunflower, Duration: 8:27, Play from: 1:45]
[Four Corners, Duration: 6:32, Play from: 2:49]
[Echo of an Angel, Duration: 6:14, Play from: 4:11]
[Survive Just Fine, Duration: 5:26, Play from: 1:29]
[Pond Life (Bonus Track), Duration: 4:21, Play from: 1:58]
```

## Future Improvements
- Get songs from an external API (in order to not require having the files)
- Create a simple GUI
- ... (WIP)