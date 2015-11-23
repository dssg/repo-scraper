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

The project has some limitations see [NOTES]('NOTES.md') file for information regarding the design of the project and how that limits what the library is able to detect..

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

Just as with git, you can specify a file to make the program ignore some files/folders. This is specially useful when you have folder with many log files that you are sure do not have sensitive data.

Adding a IGNORE file will make execution faster, since many regular expressions are matched against all files that have certain characteristics.

##What's done

* Passwords (using regex). See [`test_password_check.py`](tests/test_password_check.py)

##What's missing

* IPs
* URLs
* Check other branches apart from master

#TODO
* Come up with a cool name
