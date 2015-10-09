import os
import sys
import argparse
import urllib.request
 
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

    projectName = str(projectStructure.base_project_name)
    projectNamePath = baseDir + "/" + projectName + ".pro"
    try:
        with open(projectNamePath, "w") as outfile:
            outfile.write('TEMPLATE = subdirs')
    except IOError:
        print("Can't create file")

    # Download the file from `url` and save it locally under `file_name`:
    url = "https://dl.dropboxusercontent.com/s/w1g602bxi29cmnl/common.pri?dl=0"
    urllib.request.urlretrieve(url, "common.pri")
