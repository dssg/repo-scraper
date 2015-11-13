import mime
from repo_scraper import checker
import os
import re

#Types of results
#ALERT
ALERT = 'Alert'
#WARNING
WARNING = 'Warning'

#Explanation
#BIG_FILE
BIG_FILE = 'File is too big to scan'
#FILETYPE


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
            return self.path, 'Too big', None
  
        #Then, filter all non-plain text files
        #also send a warning for those, if they are non-plain text
        #and less than 1MB they are probably xlsx, pdfs, pngs, zips, ppt, pptx
        if not self.mimetype.startswith('text/'):
            #Add checks for certain files? (word, excel, powerpoint...)
            return self.path, 'Not a plain text file', None

        #Now, filter all files which mimetype could not be determined

        #At this point you only have plain text files, smaller than 1MB
        #open the file and then apply all rules
        with open(self.path, 'r') as f:
            content = f.read()

        #Last check: search for base64 images and remove they, send a warning
        base64images = re.compile('"image/png": ".+"').findall(content)
        if len(base64images):
            print 'REMOVING BASE64 images'
            content = re.sub('"image/png": ".+"', '',content)

        #Maybe emit warnings for data files (even if they are less than 1MB)
        #has_password, matches = None, None
        has_password, matches = checker.has_password(content)
        return self.path, has_password, matches
