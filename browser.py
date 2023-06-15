# Selenium Normal
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.service import Service
from selenium import webdriver
# Selenium - Chromedriver indetectável
import undetected_chromedriver as uc
# Classe de configurações
from settings import Settings


# - Selenuim normal
# Configurar para abrir em um perfil
configs = Settings()
options = configs.download()
# options = configs.no_extensions()
# options = configs.extensions()
# options = configs.detection()
# options = configs.maximize()
# options = configs.profile()
# options = configs.hidden()
# options = configs.pdfs()
# options = configs.humanize_navigation()

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    chrome_options=options
)

# configs.block_urls(driver)

# - Selenium - Chromedriver indetectável
options = uc.Chrome_options()
# ...
driver = uc.Chrome(
    options=options
)