#Constants in git.py (used in git diff commands)
#Maximum number of lines when doing git diff hash_a hash_b
#that won't trigger a BIG_FILE result, note that this constant
#includes all lines in the git diff output (additions, deletions)
MAX_DIFF_LINES = 10000
#Max number of characters in ADDITIONS that won't trigger a BIG_FILE result,
#note that in this case, only new lines are taken into account
MAX_DIFF_ADDITIONS_CHARACTERS = 1048576