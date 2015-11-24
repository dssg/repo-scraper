from repo_scraper.constants.result import *

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
        return '%s - %s in %s\n%s\n' % (self.result_type, self.reason, self.identifier, self.matches)