from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
import shutil
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from first_batch import links as fb_links
from second_batch import links as sb_links

url = "http://teitok.clul.ul.pt/cople2/"

downloadPathRoot = r"/home/joao/Desktop/KUL/MThesis/COPLE"
options = Options()
options.add_argument("--headless")
options.add_experimental_option("prefs", {
  "download.default_directory": downloadPathRoot,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True
})
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)


for link in fb_links + sb_links:
    driver.get(url + link)
    folder = "ortho"
    try:
        newFilename = driver.find_element(by=By.XPATH, value="//div[@id='ja-content']//h1").text
        proficiency = driver.find_element(by=By.XPATH, value="//tr//th[text()='Proficiency']/../td").text
        newFilename += '-' + proficiency
    except:
        print(f"No proficiency: {link}")
        file1 = open("errors.txt", "a")
        file1.write(f"No proficiency: {link}\n")
        file1.close()
        continue

    try:
        Wait(driver, 10).until(EC.element_to_be_clickable((By.ID, "but-nform"))).click()
    except:
        try:
            Wait(driver, 5).until(EC.element_to_be_clickable((By.ID, "but-fform"))).click()
            folder = "teacher"
        except:
            try:
                Wait(driver, 5).until(EC.element_to_be_clickable((By.ID, "but-form"))).click()
                folder = "student"
            except:
                try:
                    Wait(driver, 5).until(EC.element_to_be_clickable((By.ID, "but-pform"))).click()
                    folder = "transcription"
                except:
                    print(f"No format button: {link}")
                    file1 = open("errors.txt", "a")
                    file1.write(f"No format button: {link}\n")
                    file1.close()
                    continue
    
    Wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Download text']"))).click()
    time.sleep(1)

    downloadPath = downloadPathRoot + "/" + folder
    filename = max([downloadPathRoot + "/" + f for f in os.listdir(downloadPathRoot)],key=os.path.getctime)
    shutil.move(filename, os.path.join(downloadPath, newFilename))
    print(f"Downloaded to {folder}: {newFilename}")



# index.php?action=files&folder=xmlfiles/RECAP_1/English
# index.php?action=files&folder=xmlfiles/RECAP_1/French
# index.php?action=files&folder=xmlfiles/RECAP_1/Italian
# index.php?action=files&folder=xmlfiles/RECAP_1/Japanese
# index.php?action=files&folder=xmlfiles/RECAP_1/Polish
# index.php?action=files&folder=xmlfiles/RECAP_1/Russian
# index.php?action=files&folder=xmlfiles/RECAP_1/Spanish
# index.php?action=files&folder=xmlfiles/RECAP_2/Chinese