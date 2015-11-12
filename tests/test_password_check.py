from unittest import TestCase
from repo_scraper import checker


#Missing tests:
#more than one password in a strig
#a password spanned across multiple lines

class HardcodedPasswordString(TestCase):
    def test_detects_easy_password(self):
        str_to_check = 'password="123456"'
        has_password, matches = checker.has_password(str_to_check)
        self.assertTrue(has_password)
        self.assertEqual(matches, [str_to_check])

    def test_detects_easy_password_single_quotes(self):
        str_to_check = 'password=\'123456\''
        has_password, matches = checker.has_password(str_to_check)
        self.assertTrue(has_password)
        self.assertEqual(matches, [str_to_check])

    def test_detects_easy_password_spaces(self):
        str_to_check = 'password =   "123456"'
        has_password, matches = checker.has_password(str_to_check)
        self.assertTrue(has_password)
        self.assertEqual(matches, [str_to_check])

    def test_detects_easy_password_linebreaks(self):
        has_password, matches = checker.has_password('password ="123456"\n')
        self.assertTrue(has_password)
        self.assertEqual(matches, ['password ="123456"'])

    def test_detects_easy_password_in_R(self):
        str_to_check = 'password<-   "123456"'
        has_password, matches = checker.has_password(str_to_check)
        self.assertTrue(has_password)
        self.assertEqual(matches, [str_to_check])

    def test_detects_pwd(self):
        str_to_check = 'pwd="123456"'
        has_password, matches = checker.has_password(str_to_check)
        self.assertTrue(has_password)
        self.assertEqual(matches, [str_to_check])

    def test_detects_password_with_prefix(self):
        str_to_check = 'POSTGRES_PASSWORD=\'iYiLKi7879\''
        has_password, matches = checker.has_password(str_to_check)
        self.assertTrue(has_password)
        self.assertEqual(matches, [str_to_check])

    def test_detects_password_with_suffix(self):
        str_to_check = 'PASSWORD_MYSQL=\'iYiLKi7879\''
        has_password, matches = checker.has_password(str_to_check)
        self.assertTrue(has_password)
        self.assertEqual(matches, [str_to_check])

    def test_ignores_password_from_another_variable(self):
        str_to_check = 'password=variable'
        has_password, matches = checker.has_password(str_to_check)
        self.assertFalse(has_password)
        self.assertEqual(matches, None)

    def test_ignores_pwd_from_another_variable(self):
        str_to_check = 'pwd=variable'
        has_password, matches = checker.has_password(str_to_check)
        self.assertFalse(has_password)
        self.assertEqual(matches, None)

    def test_ignores_password_from_another_variable_with_blanks(self):
        has_password, matches = checker.has_password('pwd    =variable\n')
        self.assertFalse(has_password)
        self.assertEqual(matches, None)

class HardcodedSQLAlchemyEngines(TestCase):
    def test_detects_sqlalchemy_engine(self):
        str_to_check = 'db-schema://user:strong-pwd@localhost:5432/mydb'
        has_password, matches = checker.has_password(str_to_check)
        self.assertTrue(has_password)
        self.assertEqual(matches, [str_to_check])