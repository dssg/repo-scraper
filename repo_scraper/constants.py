#Add extensions here (lowercase)
DEFAULT_EXTENSIONS = ["py", "ipynb", "json", "sql", "sh", "txt", "r", "md", "log"]
DEFAULT_EXTENSIONS_FORMAT = reduce(lambda x,y: x+', '+y, DEFAULT_EXTENSIONS)

#Result class constants with ANSI colors
ALERT = '\033[91mAlert!\033[0m'
WARNING = '\033[93mWarning\033[0m'
NOTHING = '\033[92mNothing\033[0m'

BIG_FILE = 'Big file found'
NOT_PLAIN_TEXT = 'File is not plain text'
MATCH = 'Match found'
NOT_MATCH = 'Match not found'
FILETYPE_NOT_ALLOWED = 'Extension not allowed'