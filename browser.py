from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.service import Service
from selenium import webdriver

from settings import Settings


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

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    chrome_options=options
)

# configs.block_urls(driver)