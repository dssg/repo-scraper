from setuptools import setup

setup(
      name='repo-scraper',
      version='0.1',
      description='Safety evaluation for repositories',
      url='http://github.com/edublancas',
      author='Eduardo Blancas Reyes',
      author_email='edu.blancas@gmail.com',
      license='MIT',
      packages=['repo_scraper'],
      scripts=['bin/scrap-folder'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False
      )