import magic
import mimetypes

#This script wraps the mimetype functionality
#if python-magic is installed uses it, since it's more reliable
#than the built-in python function since the latter uses the extension
#to guess the mimetype

def from_file(path):
    return mimetypes.guess_type(path)[0]
    #return magic.from_file(path, mime=True)