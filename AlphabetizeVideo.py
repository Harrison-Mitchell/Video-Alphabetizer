from os import popen, mkdir
from sys import argv
from json import loads

lyrics = []
seenWords = []
words = []

# Ignore already created dir
try: mkdir("slices")
except: pass

print(f"Using video file `{argv[1]}` on timed lyrics `{argv[2]}`")

# Read JSON file into plain Python list to simply format and iron edge cases
with open(argv[2]) as lyricFile:
	lyricJSON = loads(lyricFile.read())
	for i in lyricJSON:
		# Lyrics are nested into song "phrases", this flattens the array
		for ii in i:
			# Remove punctuation
			word = "".join([c for c in ii["text"].upper() if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"])
			words.append(word)
			lyrics.append([ii["start"], ii["end"], word])

for word in lyrics:
	seenWords.append(word[2])
	# Slice output name e.g `slices/HELLO_03_of_12.ts`
	# .ts as I find ffmpeg plays nicely with them when slices are slim
	out = f"slices/{word[2]}_{seenWords.count(word[2]):0>2}_of_{words.count(word[2]):0>2}.ts"

	print(f"ffmpeg -i {argv[1]} -ss {word[0]} -to {word[1]} {out}")
	_ = popen(f"ffmpeg -i {argv[1]} -ss {word[0]} -to {word[1]} {out}").read()

# Finally, smash all the alphabetical bits together and reencode the video
popen("ffmpeg -safe 0 -f concat -i <(find slices/ -type f -name '*.ts' -printf "file '$PWD/%p'\n\" | sort) -c:v libx264 -crf 18 -preset slow -c:a copy Alphabetized.mp4")