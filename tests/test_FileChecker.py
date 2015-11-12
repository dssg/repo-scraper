from unittest import TestCase
from repo_scraper.FileChecker import FileChecker
import os

module_path = os.path.dirname(os.path.abspath(__file__))
dummy_repo_path = os.path.join(module_path, '..', 'dummy-repo')

class TestFileChecker(TestCase):
    def test_json_file_with_password(self):
        pass
    def test_plain_text_file_with_password(self):
        pass
    def test_python_file_with_password(self):
        path = os.path.join(dummy_repo_path, 'python_file_with_password.py')
        result, matches = FileChecker(path).check()
        self.assertTrue(result)
    def test_hidden_file_with_password(self):
        pass