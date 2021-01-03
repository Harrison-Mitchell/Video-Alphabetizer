# Video Alphabetizer
Put any video into alphabetical order, be it a [Taylor Swift music video](https://www.youtube.com/watch?v=8-4_mPJxAlU) or the [entire Star Wars franchise](https://www.youtube.com/watch?v=5GFW-eEWXlc).

### Dependencies
* Python >= 3.5
* FFMPEG (`sudo apt install ffmpeg`)

### Usage
1. Select a video local to your disk or obtain one from online e.g Youtube via `youtube-dlc`
2. Obtain the raw lyrics/words to that video via Youtube auto-captioning, a .srt caption file, or just Googleing for the lyrics
3. Submit the Youtube video or extracted audio and raw lyrics to [AutoLyrixAlign](https://autolyrixalign.hltnus.org/) (they also have a version you can run / script locally if you have 20+ GB of RAM)
4. Finally, pass the video and AutoLyrixAlign JSON output to `AlphabetizeVideo.py` to generate your `Alphabetized.mp4` output e.g
`python3 AlphabetizeVideo.py BlankSpace.mp4 BlankSpace.json`

### Alternative Lyric Aligners
* https://github.com/emirdemirel/Audio2LyricsAlignment_MIREX2019
* https://github.com/SwagLyrics/autosynch
* https://github.com/readbeyond/aeneas
