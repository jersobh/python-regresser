# Regresser - Visual Regression Library

## What is it?
A visual regression tool for comparing web apps and websites to visually find differences between versions.

## Usage:

### Webdriver
First we need to create a baseline, your main version. Any other version will be compared to this one.

```
webdriver.Driver(url='https://www.nytimes.com/', timeout=500) 
```

Now we're able to create another version. Eg.:

```python
from regresser import webdriver

webdriver.Driver(url='https://www.nytimes.com/', background=True, timeout=60)
webdriver.Driver(url='https://www.nytimes.com/', version='stg', background=False, timeout=60)```
```

Options:

```
version='staging' #version name 
driver='firefox' #defaults to firefox. Use 'chrome' to enable chromedriver
timeout=10 #timeout loading a page
background=True or False #Loads the website in background (headless)
width=None #force a width, otherwise will be automatic.
height=None #force a height, otherwise will be automatic.
```

### Analyzer
```python
from regresser import analyzer

analyzer.Compare(version='stg')
```


### Results
There are currently two outputs: alpha_diff.png and highlights.png. 
The alpha_diff will hide everything except differences, and highlights will show differences in red color after comparing
versions.