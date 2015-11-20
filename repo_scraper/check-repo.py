from repo_scraper.GitChecker import GitChecker 

gc = GitChecker().file_traverser()

for result in gc:
    if result.result_type:
        print result