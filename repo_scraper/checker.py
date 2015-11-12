import re


#This file contains code that checks a file for
#potential problems:
#passwords, ips, data files (check file size?)

#File checker, receives a path to a file
#opens it (if it's a text file) applies relevant rules


#Checks if a string has passwords

# p = re.compile('password="mypass"')
# p.findall('password="mypass"')

def has_password(s):
    #Case 1: hardcoded passwords assigned to variables
    #match variable names such as password, PASSWORD, pwd, pass,
    #SOMETHING_PASSWORD assigned to strings (match = and <-)
    pwd = re.compile('(p|P)\S*(w|W)\S*(d|D)\s*(=|<-)\s*(\'|\").*(\'|\")') #Matches p_w_d='something' and similar
    pass_ = re.compile('(pass|PASS)\S*\s*(=|<-)\s*(\'|\").*(\'|\")') #Matches pass='something' and similar

    #Case 2: SQLAlchemy engines

    #Case 3: Passwords in bash files (bash, psql, etc)

    #Case 4: Passwords stores in json, csv files

    #Case 5: Pgpass

    #passwords assigned to variables whose names are nor similar to pwd
    #but the string seems a password
    regex_list = [pwd, pass_]
    matches = regex_matcher(regex_list, s)
    has_password = len(matches) > 0
    matches = None if has_password is False else matches
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
