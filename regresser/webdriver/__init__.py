import os

from selenium import webdriver


class Driver:

    def __init__(self, url, version='baseline', driver='firefox', timeout=10, background=True, width=None, height=None):

        self.width = width
        self.height = height
        self.version = version
        self.url = url

        if driver == 'chrome':
            from selenium.webdriver.chrome.options import Options
            options = Options()
            if background:
                options.add_argument("--headless")
            self.driver = webdriver.Chrome(options=options)
        else:
            from selenium.webdriver.firefox.options import Options
            options = Options()
            if background:
                options.add_argument("--headless")
            self.driver = webdriver.Firefox(options=options)

        self.driver.set_page_load_timeout(timeout)

        self.run_version()

    def screenshot_dir(self):
        if not os.path.exists(f'./screenshots/{self.version}'):
            os.makedirs(f'./screenshots/{self.version}')

    def run_version(self):
        self.screenshot_dir()
        self.driver.get(self.url)
        self.driver.fullscreen_window()
        if self.width is None:
            self.width = self.driver.execute_script(
                "return Math.max( document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth )")
        if self.height is None:
            self.height = self.driver.execute_script(
                "return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight )")
        # self.driver.close()
        self.driver.set_window_size(self.width, self.height)
        self.driver.get(self.url)
        self.take_screenshot()
        self.driver.quit()

    def take_screenshot(self):
        self.driver.save_screenshot(f'./screenshots/{self.version}/screenshot.png')
