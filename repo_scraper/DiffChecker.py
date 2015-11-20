from repo_scraper import matchers
from repo_scraper.Result import * #need to find a better way to do this
from repo_scraper import filetype

class DiffChecker:
    def __init__(self, commit_hash, filename, content, error, allowed_extensions):
        self.commit_hash = commit_hash
        self.filename = filename
        self.content = content
        self.error = error
        self.allowed_extensions = allowed_extensions
    def check(self):
        #The commments is a list to keep track of useful information
        #encountered when checking, right now, its only being used
        #to annotate when base64 code was removed
        commments = []

        #Git is smart enough to detect changes binary files when doing diff,
        #will not show any differences, only a message similar to this:
        #Binary files /dev/null and b/img.JPG differ 

        #Check the number of additions, if there are too many
        #send a warning and skip, this may be due to a big data file addition
        #print 'Characters %d' % len(self.content)
        if self.error:
            return Result(self.filename, self.error)
    
        #Check file extension, if it's a text file continue, if it's not,
        #send a warning and skip
        #if filetype.mime_from_name(self.filename) is None:
        #    return Result(self.filename, NOT_PLAIN_TEXT)

        #Check if extension/mimetype is allowed
        if filetype.get_extension(self.filename) not in self.allowed_extensions:
            return Result(self.filename+' in '+self.commit_hash, FILETYPE_NOT_ALLOWED)
        
        #Start applying rules...
        #First check if additions contain base64, if there is remove it
        has_base64, self.content = matchers.base64_matcher(self.content, remove=True)
        if has_base64:
            commments.append('BASE64_REMOVED')
        
        #Now check for passwords
        has_pwd, matches = matchers.password_matcher(self.content)

        if has_pwd:
            return Result(self.filename+' in '+self.commit_hash, MATCH, matches=matches, comments=commments)
        else:
            return Result(self.filename+' in '+self.commit_hash, NOT_MATCH, comments=commments)