from unittest import TestCase
from repo_scraper import checker

#what if it's not quoted? what if is spanned across more than one line
#is this reasonable to test? p=some-password

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

    def test_detects_multiple_passwords(self):
        str_to_check = 'PASSWORD_MYSQL=\'iYiLKi7879\'  \n  \n  password ="123456"\n var=5'
        has_password, matches = checker.has_password(str_to_check)
        self.assertTrue(has_password)
        self.assertEqual(matches, ['PASSWORD_MYSQL=\'iYiLKi7879\'', 'password ="123456"'])

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

class HardcodedURLs(TestCase):
    def test_detects_sqlalchemy_engine(self):
        str_to_check = 'db-schema://user:strong-pwd@localhost:5432/mydb'
        has_password, matches = checker.has_password(str_to_check)
        self.assertTrue(has_password)
        self.assertEqual(matches, [str_to_check])

    def test_detects_sqlalchemy_engine_different_settings(self):
        str_to_check = 'another-schema://user2:1234@localhost:0000/awesome-db'
        has_password, matches = checker.has_password(str_to_check)
        self.assertTrue(has_password)
        self.assertEqual(matches, [str_to_check])

    def test_detects_sqlalchemy_quoted(self):
        str_to_check = '\'db-schema://user:strong-pwd@localhost:5432/mydb\''
        has_password, matches = checker.has_password(str_to_check)
        self.assertTrue(has_password)
        self.assertEqual(matches, [str_to_check])

    def test_detects_sqlalchemy_double_quoted(self):
        str_to_check = '"db-schema://user:strong-pwd@localhost:5432/mydb"'
        has_password, matches = checker.has_password(str_to_check)
        self.assertTrue(has_password)
        self.assertEqual(matches, [str_to_check])

class HardcodedPasswordsInJSON(TestCase):
    def test_detects_hardcoded_value_json(self):
        str_to_check = '''{
                            "password":"super-secret-password"     \n\n\t
                        }'''
        has_password, matches = checker.has_password(str_to_check)
        self.assertTrue(has_password)
        self.assertEqual(matches, ['"password":"super-secret-password"'])

    def test_detects_hardcoded_value_json_single_quotes(self):
        str_to_check = '''{
                            \'password\': \'super-secret-password\'     \n\n\t
                        }'''
        has_password, matches = checker.has_password(str_to_check)
        self.assertTrue(has_password)
        self.assertEqual(matches, ['\'password\': \'super-secret-password\''])

    def test_detects_hardcoded_value_json_multiple_keys(self):
        str_to_check = '''{
                            "pass": "dont-hack-me-please",
                            "key": "1234"
                        }'''
        has_password, matches = checker.has_password(str_to_check)
        self.assertTrue(has_password)
        self.assertEqual(matches, ['"pass": "dont-hack-me-please"'])

    def test_detects_hardcoded_value_json_multiple_passwords(self):
        str_to_check = '''{
                            "pass": "dont-hack-me-please",
                            "key": "1234",
                            \'pwd\'  :    \'qwerty\',
                        }'''
        has_password, matches = checker.has_password(str_to_check)
        self.assertTrue(has_password)
        self.assertEqual(matches, ['"pass": "dont-hack-me-please"', '\'pwd\'  :    \'qwerty\''])

    def test_detects_hardcoded_value_json_blanks(self):
        str_to_check = '''{
                            "   pass"  :    "dont-hack-me-please"     \n\n\t
                        }'''
        has_password, matches = checker.has_password(str_to_check)
        #self.assertTrue(has_password)
        #self.assertEqual(matches, ['"   pass"  :    "dont-hack-me-please"'])
    def test_ignores_json_without_passwords(self):
        str_to_check = '''{
                            "some_key": "this is not a password",
                            "another_key": 100-12301-123,
                        }'''
        has_password, matches = checker.has_password(str_to_check)
        self.assertFalse(has_password)
        self.assertEqual(matches, None)
    def test_detects_url_in_json_file(self):
        str_to_check = '''{
                            "engine": "db-schema://user:strong-pwd@localhost:5432/mydb",
                            "key": "1234",
                        }'''
        has_password, matches = checker.has_password(str_to_check)
        self.assertTrue(has_password)
        self.assertEqual(matches, ['"db-schema://user:strong-pwd@localhost:5432/mydb"'])

class HardcodedPasswordsInYAML(TestCase):
    def test_detects_hardcoded_value_json(self):
        str_to_check = '''
                            database: 
                              drivername: "dbdriver"
                              host:       "dbhost"
                              port:       "port"
                              username:   "username"
                              password:   "password"
                              database:   "database"
                        '''
        has_password, matches = checker.has_password(str_to_check)
        self.assertTrue(has_password)
        self.assertEqual(matches, ['password:   "password"'])

class HardcodedPasswordsInCSV(TestCase):
    def test_detects_hardcoded_value_csv(self):
        #str_to_check = '''password, qwerty'''
        #has_password, matches = checker.has_password(str_to_check)
        #self.assertTrue(has_password)
        #self.assertEqual(matches, ['password, qwerty'])
        pass

class HardcodedPasswordsInGenericPlainText(TestCase):
    pass