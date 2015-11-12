import mimetypes as mime
from repo_scraper import checker

class FileChecker:
    def __init__(self, path):
        self.path = path
        self.mimetype = mime.guess_type(path, strict=False)[0]
        #Should we open all files? What do we do with big or binary files?
        with open(path, 'r') as f:
            self.content = f.read()
    def check(self):
        #Apply rules, should we apply all rules to all kinds of files?
        #checkers as instance methods?
        #print self.content
        has_password, matches = checker.has_password(self.content)
        #return '%s is %s and has %s' % (self.path, self.mimetype, result)
        return has_password, matches
