import subprocess
import re
from repo_scraper.matchers import password_matcher

def list_commits():
    '''Returns a list with all commit hashes'''
    p = subprocess.Popen(['git', 'log', '--pretty=format:%H'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out.replace('"', '').split('\n')


def diff_for_commit(commit_hash):
    '''Retrieves diff for a specific commit and parses it
       to get file name and additions'''
    p = subprocess.Popen(['git', 'diff', commit_hash],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    out, err = p.communicate()
    #For some reason, this commands is returning with ""\n at the
    #beginning of the file
    diff = out.replace('""\n', '')
    return parse_diff(diff)

def parse_diff(diff):
    '''Parse a diff output'''
    files = diff.split('diff --git ')[1:]
    files = [parse_file_diff(f) for f in files]
    return files

#http://stackoverflow.com/questions/2529441/how-to-read-the-output-from-git-diff
def parse_file_diff(diff):
    '''Parse a diff oputput'''
    lines = diff.split('\n')
    filename = lines[0]
    content = filter(lambda x: x.startswith('+'), lines[1:])
    content = reduce(lambda x,y:x+'\n'+y, content) if len(content) else ''
    return {'filename': filename, 'content': content}

commits = list_commits()
for commit in commits[8:10]:
    print 'Checking commit %s' % commit
    files = diff_for_commit(commit)
    for f in files:
        has_password, matches = password_matcher(f['content'])
        if has_password:
            print 'Passwords in file %s, \nmatches: %s\n\n' % (f['filename'], matches)
    print '-----------------------'