import subprocess
import re
from repo_scraper.matchers import password_matcher

commits = list_commits()

for commit in commits[:10]:
    diff = diff_for_commit(commit)
    print password_matcher(diff)
    print '-----------------------'

def list_commits():
    p = subprocess.Popen(['git', 'log', '--pretty=format:"%H'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out.replace('"', '').split('\n')

def diff_for_commit(commit_hash):
    p = subprocess.Popen(['git', 'show', commit_hash],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out