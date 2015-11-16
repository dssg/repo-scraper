import mime
from repo_scraper import matchers
import os
import re


ALERT = 'ALERT'
WARNING = 'WARNING'
NOTHING = 'NOTHING'

BIG_FILE = 'BIG_FILE'
NOT_PLAIN_TEXT = 'NOT_PLAIN_TEXT'
MATCH = 'MATCH'
NOT_MATCH = 'NOT_MATCH'

dic = {BIG_FILE: WARNING, NOT_PLAIN_TEXT: WARNING, MATCH: ALERT, NOT_MATCH: NOTHING}

class Result:
    def __init__(self, file_path, reason, matches=None):
        self.file_path = file_path
        self.reason = reason
        self.matches = matches
        self.result_type = dic[reason]
    def __str__(self):
        return '%s\n%s - %s %s\n' % (self.file_path, self.result_type, self.reason, self.matches)

class FileChecker:
    def __init__(self, path):
        self.path = path
        self.mimetype = mime.from_file(path)
    def check(self):
        #Check file size if it's more than 1MB
        #send just a warning and do not open the file,
        #since pattern matching is going to be really slow
        f_size = os.stat(self.path).st_size
        if f_size > 1048576L:
            return Result(self.path, BIG_FILE)
  
        #Then, filter all non-plain text files
        #also send a warning for those, if they are non-plain text
        #and less than 1MB they are probably xlsx, pdfs, pngs, zips, ppt, pptx
        if not self.mimetype.startswith('text/'):
            #Add checks for certain files? (word, excel, powerpoint...)
            return Result(self.path, NOT_PLAIN_TEXT)

        #Now, filter all files which mimetype could not be determined

        #At this point you only have plain text files, smaller than 1MB
        #open the file and then apply all rules
        with open(self.path, 'r') as f:
            content = f.read()

        #Last check: search for potential base64 strings and remove them, send a warning
        base64images = re.compile('(?:"|\')[A-Za-z0-9\\+\\\=\\/]{100,}(?:"|\')').findall(content)
        if len(base64images):
            print 'REMOVING BASE64 images'
            content = re.sub('(?:"|\')[A-Za-z0-9\\+\\\=\\/]{100,}(?:"|\')', '""',content)

        #Maybe send warnings for data files (even if they are less than 1MB)?

        #First matcher: passwords
        password_matcher, matches = matchers.password_matcher(content)

        if password_matcher:
            return Result(self.path, MATCH, matches)
        else:
            return Result(self.path, NOT_MATCH)