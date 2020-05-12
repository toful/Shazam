from copyrightAnalyzerLib import *
import sys

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print( "ERROR: Few Arguments. Args: database-file, song" )
        exit( 1 )

    db = Database( sys.argv[1] )
    c = Compare(db)
    f = Fingerprint()

    song_hashes = f.fingerprint_file( sys.argv[2] )
    c.compare_songs( song_hashes )

    exit( 0 )