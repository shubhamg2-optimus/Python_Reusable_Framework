import os
from selenium import webdriver

def get_imei():
    # get the path of ChromeDriverServer
    dir = os.path.dirname(__file__)
    chrome_driver_path = dir + "/chromedriver"

    # create a new Chrome session
    driver = webdriver.Chrome(chrome_driver_path)
    driver.implicitly_wait(30)
    driver.maximize_window()

    # navigate to the application home page
    driver.get("https://www.getnewidentity.com/imei-generator.php")

    # get the generate button
    imei_gen_button = driver.find_element_by_class_name("col-md-4")
    imei_gen_button.click()

    imei = driver.find_element_by_id("imei_num")
    print imei.text

    imei_text = imei.text




    # close the browser window
    driver.quit()

    return imei_text