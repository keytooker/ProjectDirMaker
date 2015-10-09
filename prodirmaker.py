import os
import sys
import argparse
 
def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--root_dir_name', default = 'MyProject')
    parser.add_argument('-b', '--base_project_name', default = 'MyProject')
 
    return parser 

def makeCatalogueStructure (rootDir):
    dirList = []
    dirList.append(baseDir + "/bin/debug")
    dirList.append(baseDir + "/bin/release")
    dirList.append(baseDir + "/build/debug")
    dirList.append(baseDir + "/build/release")
    dirList.append(baseDir + "/import")
    dirList.append(baseDir + "/include")
    dirList.append(baseDir + "/lib.linux")
    dirList.append(baseDir + "/lib.win32")
    dirList.append(baseDir + "/src/include")
    dirList.append(baseDir + "/tests")
    return dirList
    
if __name__ == '__main__':
    parser = createParser()
    projectStructure = parser.parse_args(sys.argv[1:])

    print(projectStructure.root_dir_name)
    baseDir = str(projectStructure.root_dir_name)
    dirList = makeCatalogueStructure(baseDir)
    
    try:
        for catalog in dirList:
            os.makedirs(catalog)
    except OSError:
        pass
