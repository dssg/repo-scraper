import filesystem as fs
from FileChecker import FileChecker


def scrap_folder(path):
    #List all files in directory
    files = fs.list_files_in(path)
    #Ignore all inside .git/
    files = filter(lambda x: '.git/' not in x,  files)
    #Apply gitignore rules? don't rely too much on this since it could have been changed
    #How to manage pyc files?
    #Apply relevant checks for each file
    results = [FileChecker(f).check() for f in files]
    #Output results
    return zip(files, results)