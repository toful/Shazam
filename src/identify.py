from copyrightAnalyzerLib import *
import sys, os

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print( "ERROR: Few Arguments. Args: database-file, song" )
        exit( 1 )

    db = Database( sys.argv[1] )
    c = Compare(db)
    f = Fingerprint()

    song = sys.argv[2]
    song_hashes = f.fingerprint_file( song )
    result = c.compare_songs( song_hashes )

    if len(sys.argv) == 4:
        if len(result) > 0:
            song_name = os.path.basename( song[:-4] )
            if( song_name == result[0][1] ):
                print("1")
            else:
                print("0")
    else:
        if len(result) > 0:
            print("The given song coincides with the following songs in decrasing preference:")
            for song in result[:3]:
                print( "\t", song[1] )
        
    exit( 0 )