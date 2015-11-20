from repo_scraper.GitChecker import GitChecker 

gc = GitChecker(["py", "ipynb", "json", "sql", "sh", "txt", "r", "md", "log"]).file_traverser()

for result in gc:
    if result.result_type=='ALERT':
        print result