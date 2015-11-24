from repo_scraper import filetype
from repo_scraper import matchers as m
from repo_scraper.Result import *
import os
import re

class FileChecker:
    def __init__(self, path, allowed_extensions, max_file_size_bytes=1048576):
        self.path = path
        self.max_file_size_bytes = max_file_size_bytes
        self.allowed_extensions = allowed_extensions
    def check(self):
        #The comments is a list to keep track of useful information
        #encountered when checking, right now, its only being used
        #to annotate when base64 code was removed
        comments = []

        #Check file size if it's more than max_file_size_bytes (default is 1MB)
        #send just a warning and do not open the file,
        #since pattern matching is going to be really slow
        f_size = os.stat(self.path).st_size
        if f_size > self.max_file_size_bytes:
            return Result(self.path, BIG_FILE)
  
        #Check if extension is allowed
        if filetype.get_extension(self.path) not in self.allowed_extensions:
            return Result(self.path, FILETYPE_NOT_ALLOWED)

        #At this point you only have files with allowed extensions and
        #smaller than max_file_size_bytes
        #open the file and then apply all rules
        with open(self.path, 'r') as f:
            content = f.read()

        #Last check: search for potential base64 strings and remove them, send a warning
        has_base64, content = m.base64_matcher(content, remove=True)
        if has_base64:
            comments.append('BASE64_REMOVED')

        #Apply matchers: password and ips
        match, matches = m.multi_matcher(content, m.password_matcher, m.ip_matcher)

        if match:
            return Result(self.path, MATCH, matches=matches, comments=comments)
        else:
            return Result(self.path, NOT_MATCH, comments=comments)