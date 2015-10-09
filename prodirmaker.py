import os
import sys
import argparse
 
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-p', '--project_dir', default='мир')
 
    return parser 
 
if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    try:
        os.makedirs(namespace.project_dir)
    except OSError:
        pass
