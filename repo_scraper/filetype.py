import re

def get_extension(filename):
    try:
        return re.compile('.*\.(\S+)$').findall(filename)[0].lower()
    except:
        return None

