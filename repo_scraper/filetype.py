import magic
import mimetypes

#This script wraps the mimetype functionality
#if python-magic is installed uses it, since it's more reliable
#than the built-in python function, the later uses the extension
#to guess the mimetype

def mime_from_file(path):
    return magic.from_file(path, mime=True)

def mime_from_name(filename):
    return mimetypes.guess_type(path)[0]

def is_plain_text(f):
    #Guess based on extension only
    pass

def get_extension(filename):
    try:
        return filename.split('.')[1]
    except:
        return None
