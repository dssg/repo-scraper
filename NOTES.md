#Notes

##Git and standard error

Git (even in version 2.6.0) does not get along with the [standard error](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=447395) and sends any kind of unpredictable output to it. Since `check-repo` executes git commands (via `subprocess`), it needs to handle git errors. Since just checking stdrr is not enough, a naive helper function checks for the keyword 'fatal' in the standard error to raise an Exception.

Right now, it works. Since the most common error is to run git commands on a directory that does not have a git repository and hopefully will catch some other 'fatal' errors.

##On checking git history

As it is mentioned on the [README](/README.md) file, checking only at the differences between commits is faster than checking out each commit. To check such differences, the library relies on `git diff`, which introduces a couple limitations and design caveats, such limitations are explained below.

##`git diff` and extensions

##`git diff` and file size


##`git diff`  and binary files

By default, `git diff` does not show changes in binary files. That make things easier since we do not need to check if the file we are dealing with is binary before applying the regular expressions. However, what git interprets as a binary file depends on your configuration. That being said, `check-repo` will not look at binary files and will only print a warning.