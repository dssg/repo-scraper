from itertools import chain
from repo_scraper import git
from repo_scraper.DiffChecker import DiffChecker
from repo_scraper.FolderChecker import FolderChecker
import subprocess

class GitChecker:
    def __init__(self, allowed_extensions):
        self.allowed_extensions = allowed_extensions
    def file_traverser(self):
        #Checkout master
        print 'git checkout master'
        p = subprocess.Popen(['git', 'checkout', 'master'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p.communicate()

        #Get all commits in chronological order
        commits = git.list_commits()
        #Generate commit pairs (each commit with the previous one)
        commit_pairs = zip(commits[:-1], commits[1:])

        #Go to the first commit
        print 'git checkout %s (first commit in master)' % commits[0]
        p = subprocess.Popen(['git', 'checkout', commits[0]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p.communicate()

        #Get generator to check the first commit
        fc = FolderChecker('.')
        folder_file_traverser = fc.file_traverser()

        #Define a second generator that will traverse the repository
        def repo_generator():
            for pair in commit_pairs:
                #print 'getting diff for %s %s' % pair
                files_diff = git.diff_for_commit_to_commit(*pair)
                for f in files_diff:
                    #print 'gichecker: %s' % f['filename']+' in '+pair[1]
                   yield DiffChecker(pair, f['filename'], f['content'], f['error'], self.allowed_extensions).check()

        repo_file_traverser = repo_generator()

        #Join both generators and return
        return chain(folder_file_traverser, repo_file_traverser)
        
        #Checkout master
        #print 'git checkout master'
        #p = subprocess.Popen(['git', 'checkout', 'master'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #p.communicate()