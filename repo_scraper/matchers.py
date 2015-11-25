import re

def multi_matcher(s, *matchers):
    '''Receives matchers as parameters and applies all of them'''
    results = [m(s) for m in matchers]
    #Get the flag that indicates wether there was a match for each matcher
    has_match = [r[0] for r in results]
    #Check if there was at least one match
    at_least_one = reduce(lambda x,y: x or y, has_match)
    #Get list of matches for each matcher, delete Nones
    list_of_lists = [r[1] for r in results if r[1] is not None]
    #Flatten list of matches, ignore None
    matches = [match for single_list in list_of_lists for match in single_list]
    #If the list is empty, return None
    matches = None if len(matches)==0 else matches
    return at_least_one, matches

def base64_matcher(s, remove=False):
    regex = '(?:"|\')[A-Za-z0-9\\+\\\=\\/]{50,}(?:"|\')'
    base64images = re.compile(regex).findall(s)
    has_base64 = len(base64images) > 0
    if remove:
        return has_base64, re.sub(regex, '""', s)
    else:
        return has_base64

def password_matcher(s):
    #Case 1: hardcoded passwords assigned to variables (python, r, etc) 
    #or values (json, csv, etc)
    #match variable names such as password, PASSWORD, pwd, pass,
    #SOMETHING_PASSWORD assigned to strings (match = and <-)

    #Matches p_w_d='something' and similar
    pwd = re.compile('(\S*\\\*(?:\'|\")*(?:p|P)\S*(?:w|W)\S*(?:d|D)\\\*(?:\'|\")*\s*(?:=|<-|:)\s*\\\*(?:\'|\").*\\\*(?:\'|\"))')
    #Matches pass='something' and similar
    pass_ = re.compile('(\S*\\\*(?:\'|\")*(?:pass|PASS)\S*\\\*(?:\'|\")*\s*(?:=|<-|:)\s*\\\*(?:\'|\").*\\\*(?:\'|\"))')

    #Case 2: URLS (e.g. SQLAlchemy engines)
    #http://docs.sqlalchemy.org/en/rel_1_0/core/engines.html
    #Note that validating URls is really hard...
    #http://stackoverflow.com/questions/827557/how-do-you-validate-a-url-with-a-regular-expression-in-python
    urls = re.compile('\\\*(?:\'|\")*[a-zA-Z0-9-_]+://[a-zA-Z0-9-_]+:[a-zA-Z0-9-_]+@[a-zA-Z0-9-_]+:[a-zA-Z0-9-_]+/[a-zA-Z0-9-_]+\\\*(?:\'|\")*')

    #Case 3: Passwords in bash files (bash, psql, etc) bash parameters

    #Case 5: Pgpass
    #http://www.postgresql.org/docs/9.3/static/libpq-pgpass.html

    #what about case 1 without quotes?

    #passwords assigned to variables whose names are nor similar to pwd
    #but the string seems a password
    regex_list = [pwd, pass_, urls]
    matches = regex_matcher(regex_list, s)
    has_password = len(matches) > 0
    matches = None if has_password is False else list(set(matches))
    return has_password, matches

#Checks if a string has ips
#Matching IPs with regex is a thing:
#http://stackoverflow.com/questions/10086572/ip-address-validation-in-python-using-regex
def ip_matcher(s):
    ips = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", s)
    #Remove obvious non-dangerous matches
    allowed_ips = ['127.0.0.1', '0.0.0.0']
    ips = [ip for ip in ips if ip not in allowed_ips]
    if len(ips):
        return True, ips
    else:
        return False, None

def create_domain_matcher(domain):
    '''Returns a function that serves as a matcher for a given domain'''
    def domain_matcher(s):
        regex = '\S+\.'+domain.replace('.', '\.')
        matches = re.findall(regex, s)
        if len(matches):
            return True, matches
        else:
            return False, None
    return domain_matcher


def regex_matcher(regex_list, s):
    '''Get a list of regex and return all matches'''
    #Find matches for each regex
    results_list = [regex.findall(s) for regex in regex_list]
    #Flatten list
    results_list = reduce(lambda x,y: x+y, results_list)
    #Return a set to remove duplicates?
    return results_list

#maybe also check aws related urls