#repo_scraper

Check your projects for possible password (or other sensitive data) leaks.

The library exposes two commands:
* `check-folder` - Performs checks on a folder and subdirectories
* `check-repo` - Performs a check in a git repository

Both scripts work almost the same from the user point of view, enter `check-folder --help` or `check-repo --help` for more details.

##Example

Check your dummy-project:
```bash
check-folder dummy-project
```

Output:
```bash
Checking folder dummy-project...

dummy-project/python_file_with_password.py
ALERT - MATCH ["password = 'qwerty'"]

dummy-project/dangerous_file.json
ALERT - MATCH ['"password": "super-secret-password"']
```

##How does it work?

Briefly speaking, `check-folder` lists all files below a folder and applies regular expressions to look for passwords/IPs. Given that a blind search would never end (for example, if the repo constans a 50MB csv file), some filters are applied before the regular expressions are matched:

* File size. 
* Extension.
* Base64.

`check-repo` works in a slightly different way, one obvious way to check git history is to checkout each commit and apply `check-folder`. That approach would be really slow since the script would be checking the same files many times. Instead, `check-repo` checks out the first commit, runs `check-folder` there and then, moves up one commit at a time and uses `git diff` to get only the difference between each consecutive pair of commits.

As in `check-folder`, the script applies some filters before applying regular expressions, to prevent getting stuck on big files:

* Number of lines.
* Number of characters.
* Extension.
* Base64.

The project has some limitations see [NOTES](NOTES.md) file for information regarding the design of the project and how that limits what the library is able to detect.

##Installation

```bash
    pip install git+git://github.com/dssg/repo-scraper.git -r requirements.txt
```

##Dependencies

* glob2
* nose (optional, for running tests)

##Tested with
* Python 2.7.10
* Git 2.6.0

##Usage

```bash
    cd path/to/your/project
    check-folder
```

See help for more options available:

```bash
    check-folder --help
```

###Using a IGNORE file with check-folder

Just as with git, you can specify a file to make the program ignore some files/folders. This is specially useful when you have folder with many log files that you are sure do not have sensitive data. The library assumes one glob rule per line.

Adding a IGNORE file will make execution faster, since many regular expressions are matched against all files that have certain characteristics.

**Important**: Even though the format is very similar, you cannot use the same rules as in your [.gitignore](https://git-scm.com/docs/gitignore) file. For more details, see [this](https://en.wikipedia.org/wiki/Glob_(programming)).

##What's done

* Passwords (using regex). See [`test_password_check.py`](tests/test_password_check.py)

##What's missing

* IPs
* URLs
* Check other branches apart from master

#TODO
* Come up with a cool name
