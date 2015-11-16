import subprocess
import re
from repo_scraper.matchers import password_matcher

def list_commits():
    p = subprocess.Popen(['git', 'log', '--pretty=format:%H'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out.replace('"', '').split('\n')

def diff_for_commit(commit_hash):
    p = subprocess.Popen(['git', 'show', '--pretty=format:""', commit_hash],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out

def parse_diff(diff):
    split_by_file = diff.split('diff --git ')
    #Filter empty lines
    #Get filename
    #Get file extension
    return split_by_file

commits = list_commits()
diff = diff_for_commit(commits[0])
parse_diff(diff)

for commit in commits[:10]:
    #Get diff for a given commit
    diff = diff_for_commit(commit)
    #Parse diff content
    #Get file extension
    #Decide what to to based on the file
    
    print len(diff)
    #print password_matcher(diff)
    print '-----------------------'