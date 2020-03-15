from regresser import webdriver, analyzer

if __name__ == '__main__':
    webdriver.Driver(url='https://www.nytimes.com/', background=True, timeout=60)
    webdriver.Driver(url='https://www.nytimes.com/', version='stg', background=False, timeout=60)
    analyzer.Compare(version='stg')
