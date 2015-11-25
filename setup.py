from setuptools import setup

setup(
      name='repo-scraper',
      version='0.1',
      description='Search for potential passwords/data leaks in a folder or git repo',
      url='https://github.com/dssg/repo-scraper',
      author='Eduardo Blancas Reyes',
      author_email='edu.blancas@gmail.com',
      license='MIT',
      packages=['repo_scraper'],
      scripts=['bin/check-dir', 'bin/check-repo'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False
      )