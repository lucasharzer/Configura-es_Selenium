from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv, find_dotenv
import os


class Settings:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.userdata = os.getenv("USERDATA")
        self.profile = os.getenv("PROFILE")
        self.pathfiles = os.getenv("PATHFILES")
        self.crxfiles = os.getenv("CRXFILE")
        self.useragent = os.getenv("USERAGENT")
        self.url = os.getenv("URL")

        self.options = Options()
    
    def hidden(self):
        self.options.add_argument("--headless")
        # ou em casos de recursos avançados do Chrome
        # self.options.add_argument("--headless=new")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        # ou 
        # self.options.headless = True
        return self.options
    
    def humanize_navigation(self):
        # Comando JavaScript: navigator.userAgent
        self.options.add_argument(f"user-agent={self.useragent}")
        self.options.add_argument("--disable-notifications")
        return self.options
    
    def profile(self):
        self.options.add_argument(f"--user-data-dir={self.userdata}")
        self.options.add_argument(f"--profile-directory={self.profile}")
        return self.options

    def download(self):
        self.options.add_experimental_option("prefs", {
            "download.default_directory": self.pathfiles,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        return self.options
    
    def pdfs(self):
        self.options.add_experimental_option("prefs", {
            "download.default_directory": self.pathfiles,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True
        })
        return self.options
    
    def detection(self):
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        return self.options
    
    def extensions(self):
        self.options.add_extension(self.crxfiles)
    
    def no_extensions(self):
        self.options.add_argument("--disable-extensions")
        return self.options
    
    def maximize(self):
        self.options.add_argument("--start-maximized")
        self.options.add_experimental_option()
        return self.options

    def block_urls(self, driver):
        driver.execute_cdp_cmd("Network.setBlockedURLs", {"urls": [self.url]})
        driver.execute_cdp_cmd("Network.enable", {})
