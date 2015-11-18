import subprocess
import re
from repo_scraper.matchers import password_matcher

def list_commits():
    p = subprocess.Popen(['git', 'log', '--pretty=format:%H'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out.replace('"', '').split('\n')

#use diff instead of show
def diff_for_commit(commit_hash):
    p = subprocess.Popen(['git', 'diff', commit_hash],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    out, err = p.communicate()
    #For some reason, this commands is returning with ""\n at the
    #beginning of the file
    return out.replace('""\n', '')

#http://stackoverflow.com/questions/2529441/how-to-read-the-output-from-git-diff
def parse_commit_diff(diff):
    files = diff.split('diff --git ')[1:]
    files = [parse_file_diff(f) for f in files]
    return files

def parse_file_diff(diff):
    lines = diff.split('\n')
    filename = lines[0]
    content = filter(lambda x: x.startswith('+'), lines[1:])
    content = reduce(lambda x,y:x+'\n'+y, content) if len(content) else ''
    return {'filename': filename, 'content': content}

for commit in commits[:10]:
    files = parse_commit_diff(diff_for_commit(commit))
    for f in files:
        has_password, matches = password_matcher(f['content'])
        if has_password:
            print 'Commit %s \nHas passwords in file %s, \nmatches: %s' % (commit, f['filename'], matches)
    print '-----------------------'