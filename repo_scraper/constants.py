#Add extensions here (lowercase)
DEFAULT_EXTENSIONS = ["py", "ipynb", "json", "sql", "sh", "txt", "r", "md", "log"]
DEFAULT_EXTENSIONS_FORMAT = reduce(lambda x,y: x+', '+y, DEFAULT_EXTENSIONS)

#Result class constants with ANSI colors
ALERT = '\033[91mALERT\033[0m'
WARNING = '\033[93mWARNING\033[0m'
NOTHING = '\033[92mNOTHING\033[0m'

BIG_FILE = 'BIG_FILE'
NOT_PLAIN_TEXT = 'NOT_PLAIN_TEXT'
MATCH = 'MATCH'
NOT_MATCH = 'NOT_MATCH'
FILETYPE_NOT_ALLOWED = 'FILETYPE_NOT_ALLOWED'