from copyrightAnalyzerLib import *
import glob, sys, os

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print( "ERROR: Few Arguments. Args: songs-folder, database-file" )
        exit( 1 )

    db = Database( sys.argv[2] )
    f = Fingerprint()

    for song in glob.glob( sys.argv[1]+'/**/*.wav', recursive=True ):
        song_name = os.path.basename( song[:-4] )
        print( "Processing song: ", song_name )
        song_hashes = f.fingerprint_file( song )
        db.insert_song( song_name, song_hashes )

    exit( 0 )