ALERT = 'ALERT'
WARNING = 'WARNING'
NOTHING = 'NOTHING'

BIG_FILE = 'BIG_FILE'
NOT_PLAIN_TEXT = 'NOT_PLAIN_TEXT'
MATCH = 'MATCH'
NOT_MATCH = 'NOT_MATCH'
FILETYPE_NOT_ALLOWED = 'FILETYPE_NOT_ALLOWED'

dic = {
        BIG_FILE: WARNING,
        NOT_PLAIN_TEXT: WARNING,
        MATCH: ALERT,
        NOT_MATCH: NOTHING,
        FILETYPE_NOT_ALLOWED: WARNING
       }

class Result:
    def __init__(self, filename, reason, matches=None):
        self.filename = filename
        self.reason = reason
        self.matches = matches
        self.result_type = dic[reason]
    def __str__(self):
        return '%s\n%s - %s %s\n' % (self.filename, self.result_type, self.reason, self.matches)