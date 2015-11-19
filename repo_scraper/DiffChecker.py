from repo_scraper import matchers
from repo_scraper.Result import * #need to find a better way to do this
from repo_scraper import mime

class DiffChecker:
    def __init__(self, filename, content, error):
        self.filename = filename
        self.content = content
        self.error = error
    def check(self):
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
        if mime.from_file(self.filename) is None:
            return Result(self.filename, NOT_PLAIN_TEXT)

        #Check if extension/mimetype is allowed
        
        #Start applying rules...
        #First check if additions contain base64, if there is remove it
        has_base64, self.content = matchers.base64_matcher(self.content, remove=True)
        if has_base64:
            print 'Base64 additions, removing them...'
        
        #Now check for passwords
        has_pwd, matches = matchers.password_matcher(self.content)

        if has_pwd:
            return Result(self.filename, MATCH, matches)
        else:
            return Result(self.filename, NOT_MATCH)