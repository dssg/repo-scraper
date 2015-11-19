import subprocess

def list_commits():
    '''Returns a list with all commit hashes'''
    p = subprocess.Popen(['git', 'log', '--pretty=format:%H'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out.replace('"', '').split('\n')


def diff_for_commit_to_commit(commit1_hash, commit2_hash):
    '''Retrieves diff for a specific commit and parses it
       to get file name and additions'''
    #Pass the -M flag to detect modified files and avoid redundancy
    p = subprocess.Popen(['git', 'diff', '-M', commit1_hash, commit2_hash],
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
    #File line is the first line here, with the following format:
    #a/file.txt b/file2.txt where file and file2 are different
    #only if the file was renamed, in which case the current name is file2
    filename = lines[0].split(' ')[1].split('/')[1]
    content = filter(lambda x: x.startswith('+'), lines[1:])
    content = reduce(lambda x,y:x+'\n'+y, content) if len(content) else ''
    return {'filename': filename, 'content': content}