import os
import sys
import argparse
 
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-p', '--project_dir', default='base')
 
    return parser 
 
if __name__ == '__main__':
    parser = createParser()
    proname = parser.parse_args(sys.argv[1:])

    print(proname.project_dir)
    baseDir = str(proname.project_dir)
    dirBin = baseDir + "/bin";
    try:
        os.makedirs(dirBin)
    except OSError:
        pass
