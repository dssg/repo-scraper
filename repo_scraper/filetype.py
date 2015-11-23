#import magic
#import mimetypes
import re

#def mime_from_file(path):
#    return magic.from_file(path, mime=True)

#def mime_from_name(filename):
#    return mimetypes.guess_type(path)[0]

def get_extension(filename):
    try:
        return re.compile('.*\.(\S+)$').findall(filename)[0].lower()
    except:
        return None

