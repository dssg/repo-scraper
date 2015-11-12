import os
import mimetypes as mime

def list_files_and_types_in(directory):
    '''This function receives a path to a directory and returns
    paths to all files along with each mimetype'''
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    files_and_mimetypes = [(f, mime.guess_type(f)[0]) for f in file_list]
    return files_and_mimetypes



mime.guess_type('/Users/Edu/Desktop/20151105201530.jpg')