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
    def __init__(self, identifier, reason, matches=None, comments=None):
        self.identifier = identifier
        self.reason = reason
        self.matches = matches
        self.result_type = dic[reason]
        self.comments = comments
    def __str__(self):
        return '%s\n%s - %s %s\n' % (self.identifier, self.result_type, self.reason, self.matches)