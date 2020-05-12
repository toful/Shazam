#!/bin/sh

#music_library contains both folders: library1 and library2 with all songs
python3 builddb.py ../music_library songs.db

#music_test contains all sample folders: clean_samples, filtered_samples, noisy_filtered_samples and noisy_samples with all subfolders and songs
for entry in "../music_test/noisy_samples/01_Bourgade_samples_noisy"/*; do
    python3 identify.py songs.db $entry
done
