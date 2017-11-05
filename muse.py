import os
import subprocess
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
mp3DirName = "path/to/your/music/directory"

#print(EasyID3.valid_keys.keys())


# Loop through mp3s and get metadata.
# Then add Album name for missing Album name Title -> Album name

for root, dirs, files in os.walk(mp3DirName, topdown=True):
    for name in files:
        # complete MP3 path, simply using "name" does not work
        audio = EasyID3(os.path.join(root, name))
        # using 'albumartist' in audio instead of audio["albumartist"]
        if not 'albumartist' in audio:
            print(str(audio["title"]) + "does not have an Artist Title, needs to be set")
            audio["albumartist"] = audio["artist"]
            print("Album Artist set successfully")
            audio.save()

        # using "".join to convert List element to a proper string instead of ["Title"]
        audio["album"] = "{} - Single".format("".join(audio["title"]))
        print("{} has been renamed to {} - Single".format(audio["album"], audio["title"]))
        audio.save()