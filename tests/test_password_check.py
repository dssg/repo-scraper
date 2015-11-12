from unittest import TestCase
from repo_scraper import checker


#Missing tests:
#more than one password in a strig
#correctly idenitfy multiple passwords in one string

class TestPasswordCheck(TestCase):
    def test_detects_easy_password(self):
        str_to_check = 'password="123456"'
        has_password, matches = checker.has_password(str_to_check)
        #self.assertTrue(has_password)
        #self.assertEqual(len(matches), 1)
        self.assertEqual(matches, [str_to_check])

    def test_detects_easy_password_single_quotes(self):
        has_password, matches = checker.has_password('password=\'123456\'')
        self.assertTrue(has_password)

    def test_detects_easy_password_spaces(self):
        has_password, matches = checker.has_password('password =   "123456"')
        self.assertTrue(has_password)

    def test_detects_easy_password_linebreaks(self):
        has_password, matches = checker.has_password('\npassword ="123456"')
        self.assertTrue(has_password)

    def test_detects_easy_password_in_R(self):
        has_password, matches = checker.has_password('\npassword<-   "123456"')
        self.assertTrue(has_password)

    def test_detects_pwd(self):
        has_password, matches = checker.has_password('pwd="123456"')
        self.assertTrue(has_password)

    def test_detects_password_with_prefix(self):
        has_password, matches = checker.has_password('POSTGRES_PASSWORD=\'iYiLKi7879\'')
        self.assertTrue(has_password)

    def test_detects_password_with_suffix(self):
        has_password, matches = checker.has_password('PASSWORD_MYSQL=\'iYiLKi7879\'')
        self.assertTrue(has_password)

    def test_ignores_password_from_another_variable(self):
        has_password, matches = checker.has_password('password=variable')
        self.assertFalse(has_password)

    def test_ignores_pwd_from_another_variable(self):
        has_password, matches = checker.has_password('pwd=variable')
        self.assertFalse(has_password)

    def test_ignores_password_from_another_variable_with_blanks(self):
        has_password, matches = checker.has_password('\npwd    =variable')
        self.assertFalse(has_password)