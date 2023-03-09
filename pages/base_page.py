class BasePage:
    def __init__(self, driver, url: str):
        self.driver = driver
        self.base_url = 'https://www.saucedemo.com/'
        self.url = url
        self.get()

    def get(self):
        full_url = self.base_url + self.url
        if self.url not in self.driver.current_url:
            self.driver.get(full_url)

    def get_url(self):
        return self.driver.current_url
