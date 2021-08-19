from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class AppleMusicDriver():
    """The Apple Music driver class"""
    def __init__(self):
        self.setup_chrome()
    
    def setup_chrome(self, window_visible = True, no_load_conditions = False):
        """
        Sets up Chrome and its webdriver to be used by Selenium.
        """
        print("Setting up Chrome...")
        chrome_options = Options()
        if not window_visible:
            chrome_options.add_argument("--headless") # this allows not seeing the browser window
        caps = DesiredCapabilities().CHROME
        if no_load_conditions:
            caps["pageLoadStrategy"] = "none" # Does not wait for full page load
        else:
            caps["pageLoadStrategy"] = "normal" #  Waits for full page load
        chrome_options.add_argument("--window-size=%s" % '960,1080')
        self.driver = webdriver.Chrome(options = chrome_options, desired_capabilities = caps)

    def connect(self):
        """Open the website"""
        print("Opening the website...")
        self.driver.get('https://music.apple.com/login')
        self.sign_in()

    def sign_in(self):
        self.apple_id = input("Sign in with your Apple ID: ")
        apple_id_input = wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@can-field='accountName']")))
        #apple_id_input = self.driver.find_element_by_id("account_name_text_field")
        apple_id_input.send_keys(self.apple_id)

def main():
    apple_music_driver = AppleMusicDriver()
    apple_music_driver.connect()
    while True:
        pass

if __name__ == '__main__':
    main()
