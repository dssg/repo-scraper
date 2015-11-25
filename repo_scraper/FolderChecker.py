#Creates a FileChecker instance for each file inside a directory
#(and subdirectories) and applies matchers
from repo_scraper import filesystem as fs
from repo_scraper.FileChecker import FileChecker

class FolderChecker:
    def __init__(self, folder_path, allowed_extensions, ignore_git_folder=True, ignore_path=None):
        #List all files in directory, apply ignore file if necessary
        self.filenames = fs.list_files_in(folder_path, ignore_git_folder=ignore_git_folder, ignore_file=ignore_path)
        self.allowed_extensions = allowed_extensions
    def file_traverser(self):
        for filename in self.filenames:
            yield FileChecker(filename, allowed_extensions=self.allowed_extensions).check()