#!/bin/sh

#music_library contains both folders: library1 and library2 with all songs
python3 builddb.py ../music_library songs.db

#music_test contains all sample folders: clean_samples, filtered_samples, noisy_filtered_samples and noisy_samples with all subfolders and songs
for entry in "../music_library/library1"/*; do
    python3 -W ignore identify.py songs.db "${entry}" "test"
done
