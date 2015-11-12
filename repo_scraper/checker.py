import re

#This file contains code that checks a file for
#potential problems:
#passwords, ips, data files (check file size?)

def has_password(s):
    #Case 1: hardcoded passwords assigned to variables (python, r, etc) 
    #or values (json, csv, etc)
    #match variable names such as password, PASSWORD, pwd, pass,
    #SOMETHING_PASSWORD assigned to strings (match = and <-)

    #Matches p_w_d='something' and similar
    pwd = re.compile('''(\S*(?:\'|\")*(?:p|P)\S*(?:w|W)\S*(?:d|D)(?:\'|\")*\s*(?:=|<-|:)\s*(?:\'|\").*(?:\'|\"))''')
    #Matches pass='something' and similar
    pass_ = re.compile('(\S*(?:\'|\")*(?:pass|PASS)\S*(?:\'|\")*\s*(?:=|<-|:)\s*(?:\'|\").*(?:\'|\"))')

    #Case 2: URLS (e.g. SQLAlchemy engines)
    #http://docs.sqlalchemy.org/en/rel_1_0/core/engines.html
    #Note that validating URls is really hard...
    #http://stackoverflow.com/questions/827557/how-do-you-validate-a-url-with-a-regular-expression-in-python
    urls = re.compile('(?:\'|\")*[a-zA-Z0-9-_]+://[a-zA-Z0-9-_]+:[a-zA-Z0-9-_]+@[a-zA-Z0-9-_]+:[a-zA-Z0-9-_]+/[a-zA-Z0-9-_]+(?:\'|\")*')

    #Case 3: Passwords in bash files (bash, psql, etc) bash parameters

    #Case 5: Pgpass

    #what about case 1 without quotes?

    #passwords assigned to variables whose names are nor similar to pwd
    #but the string seems a password
    regex_list = [pwd, pass_, urls]
    matches = regex_matcher(regex_list, s)
    has_password = len(matches) > 0
    matches = None if has_password is False else list(set(matches))
    return has_password, matches


#Checks if a string has ips
# p = re.compile('(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])')
# p = re.compile('\d+')
# p.findall('this does not have ips')
# p.findall('Oh, look! an IP 192.168.1.22')
def has_ip(str):
    return False, None


def regex_matcher(regex_list, s):
    '''Get a list of regex and return all matches'''
    #Find matches for each regex
    results_list = [regex.findall(s) for regex in regex_list]
    #Flatten list
    results_list = reduce(lambda x,y: x+y, results_list)
    #Return a set to remove duplicates?
    return results_list
