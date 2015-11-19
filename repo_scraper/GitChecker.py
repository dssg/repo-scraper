from repo_scraper import git
from repo_scraper.matchers import password_matcher
import subprocess

#Checkout master
subprocess.call(['git', 'checkout', 'master'])

#Get all commits, reverse the list to get them in chronological order
commits = git.list_commits()[::-1]

#Go to the first commit
subprocess.call(['git', 'checkout', commits[0]])

#Run folder checker on first commit

#Checkout master
subprocess.call(['git', 'checkout', 'master'])

#Generate commit pairs (each commit with the previous one)
commit_pairs = zip(commits[:-1], commits[1:])

#Then checkings on each consecutive pair of commits, to account for addictions
#only
for pair in commit_pairs:
    print 'Checking commit %s with %s' % pair
    files = git.diff_for_commit_to_commit(*pair)
    for f in files:
        has_password, matches = password_matcher(f['content'])
        #print 'content is: %s' % f['content']
        if has_password:
            print 'Passwords in file %s, \nmatches: %s\n\n' % (f['filename'], matches)
    print '-----------------------'

