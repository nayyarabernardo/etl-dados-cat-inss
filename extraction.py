import os
import time
import requests
import logging
from pathlib import Path
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class CATDownloader:
    def __init__(self):
        self.base_url = "https://dados.gov.br/dados/conjuntos-dados/comunicacoes-de-acidente-de-trabalho-cat-plano-de-dados-abertos-jun-2023-a-jun-2025"
        self.download_dir = Path("data/cat_downloads")
        self.processed_dir = Path("data/processed")
        self.log_file = Path("logs/cat_downloader.log")
        self.driver_timeout = 30
        self.max_retries = 3
        self.current_year = datetime.now().year
        self.setup_directories()
        self.setup_logging()
        self.driver = self.setup_webdriver()

    def setup_directories(self):
        self.download_dir.mkdir(parents=True, exist_ok=True)
        self.processed_dir.mkdir(parents=True, exist_ok=True)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def setup_webdriver(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        
        prefs = {
            "download.default_directory": str(self.download_dir.absolute()),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        options.add_experimental_option("prefs", prefs)
        
        service = Service()
        return webdriver.Chrome(service=service, options=options)

    def wait_for_element(self, locator, timeout=None):
        timeout = timeout or self.driver_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def extract_file_info(self, filename):
        try:
            parts = filename.split('-')
            month = parts[-2].strip().lower()
            year = int(parts[-1].strip().split('.')[0])
            return month, year
        except (IndexError, ValueError):
            self.logger.warning(f"Failed to parse month/year from filename: {filename}")
            return None, None

    def is_current_month_file(self, filename):
        month, year = self.extract_file_info(filename)
        if not month or not year:
            return False
            
        current_month = datetime.now().strftime("%B").lower()
        return (month == current_month and year == self.current_year)

    def get_latest_files(self):
        try:
            self.driver.get(self.base_url)
            self.wait_for_element((By.XPATH, "//button[contains(., 'Acessar recursos')]")).click()
            
            links = self.driver.find_elements(By.XPATH, "//a[contains(translate(@href, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '.zip')]")
            return {link.get_attribute('href'): link.get_attribute('text').strip() for link in links}
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Error finding download links: {str(e)}")
            return {}

    def download_file(self, url, filename):
        local_path = self.download_dir / filename
        
        for attempt in range(self.max_retries):
            try:
                with requests.get(url, stream=True, timeout=60) as response:
                    response.raise_for_status()
                    with open(local_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
                return True
            except requests.exceptions.RequestException as e:
                self.logger.warning(f"Attempt {attempt + 1} failed for {filename}: {str(e)}")
                if attempt < self.max_retries - 1:
                    time.sleep(5)
        
        return False

    def process_new_files(self):
        downloaded_files = {}
        file_urls = self.get_latest_files()
        
        for url, filename in file_urls.items():
            if not self.is_current_month_file(filename):
                continue
                
            if (self.download_dir / filename).exists():
                self.logger.info(f"File already exists: {filename}")
                downloaded_files[filename] = url
                continue
                
            if self.download_file(url, filename):
                downloaded_files[filename] = url
                self.logger.info(f"Successfully downloaded: {filename}")
            else:
                self.logger.error(f"Failed to download: {filename}")
        
        return downloaded_files

    def run(self):
        try:
            self.logger.info("Starting CAT files download process")
            downloaded_files = self.process_new_files()
            
            if not downloaded_files:
                self.logger.info("No new files to download")
                return False
            
            self.logger.info(f"Downloaded {len(downloaded_files)} new files")
            return True
            
        except Exception as e:
            self.logger.error(f"Unexpected error: {str(e)}", exc_info=True)
            return False
        finally:
            self.driver.quit()
            self.logger.info("Process completed")

if __name__ == "__main__":
    downloader = CATDownloader()
    success = downloader.run()
    exit(0 if success else 1)