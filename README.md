#repo_scraper

Check your projects for possible data/password leaks.

##How does it work

##Installation

```bash
    pip install git+git://github.com/dssg/repo-scraper.git
```

##Dependencies

* glob2
* python-magic
* nose (for running tests)

##Usage

```bash
    cd path/to/your/projects
    scrap-folder
```

See help for more options available:

```bash
    scrap-folder --help
```

###Using a IGNORE file

Just as with git, you can specify a file to make the program ignore some files/folders. This is specially useful when you have folder with many log files that you are sure do not have sensitive data.

Adding a IGNORE file will make execution faster, since many regular expressions are matched against all files that have certain characteristics.

##What's done

##What's missing