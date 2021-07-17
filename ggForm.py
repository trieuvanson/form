# Add thư viện
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import random
import os
# # Tắt thông báo từ chrome
# # chrome_options = webdriver.ChromeOptions()
# # prefs = {"profile.default_content_setting_values.notifications": 2}
# # chrome_options.add_experimental_option("prefs", prefs)
# # driver = webdriver.Chrome(chrome_options = chrome_options)
# driver = webdriver.Chrome('D:\Python\chromedriver.exe')
# # Phóng to màn hình
# driver.maximize_window()
# # Vào facebook
# driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeCi1sYlnmjsgpeQde88mr-d_yXmgKh7BhJGQnRAPmH7U-C_g/viewform")

# # Trang 1

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
driver.find_elements_by_xpath("//div[@class = 'appsMaterialWizToggleRadiogroupOffRadio exportOuterCircle']")[0].click();
button1 = driver.find_element_by_xpath("//div[@class = 'appsMaterialWizButtonPaperbuttonFocusOverlay exportOverlay']");
driver.execute_script("arguments[0].click();", button1);
#  Trang 2

radios = driver.find_elements_by_xpath("//div[@class = 'appsMaterialWizToggleRadiogroupOffRadio exportOuterCircle']");
length = [random.randint(1, 2),random.randint(3, 7),random.randint(8, 12),random.randint(13, 16),random.randint(17, 20)];
for j in range(len(length)):
        print(length[j])
        radios[length[j]-1].click();


checkboxs = driver.find_elements_by_xpath("//div[@class = 'quantumWizTogglePapercheckboxInnerBox exportInnerBox']");

for i in range(len(checkboxs)):
    checkboxs[i].click();
button = driver.find_elements_by_xpath("//div[@class = 'appsMaterialWizButtonPaperbuttonFocusOverlay exportOverlay']");
driver.execute_script("arguments[0].click();", button[1]);
#  Trang 3
length = [random.randint(4, 5),random.randint(9, 10),random.randint(14, 15),random.randint(19, 20),random.randint(24, 25)];
radios = driver.find_elements_by_xpath("//div[@class = 'appsMaterialWizToggleRadiogroupOffRadio exportOuterCircle']");
for j in range(len(length)):
        radios[length[j]-1].click();
button = driver.find_elements_by_xpath("//div[@class = 'appsMaterialWizButtonPaperbuttonFocusOverlay exportOverlay']");
driver.execute_script("arguments[0].click();", button[4]);
# Trang 4
radios = driver.find_elements_by_xpath("//div[@class = 'appsMaterialWizToggleRadiogroupOffRadio exportOuterCircle']");
# length = [5,10,15,19,25,29,35,40,45,49];
length = [random.randint(4, 5),random.randint(9, 10),random.randint(14, 15),random.randint(19, 20),random.randint(24, 25),
random.randint(29, 30),random.randint(34, 35),random.randint(39, 40),random.randint(44, 45),random.randint(49, 50)];
for j in range(len(length)):
        radios[length[j]-1].click();
button = driver.find_elements_by_xpath("//span[@class = 'appsMaterialWizButtonPaperbuttonContent exportButtonContent']");
driver.execute_script("arguments[0].click();", button[1]);
# Trang 5
radios = driver.find_elements_by_xpath("//div[@class = 'appsMaterialWizToggleRadiogroupOffRadio exportOuterCircle']");
# length= [5,10,15,20,25];
length = [random.randint(4, 5),random.randint(9, 10),random.randint(14, 15),random.randint(19, 20),random.randint(24, 25)];
for j in range(len(length)):
        radios[length[j]-1].click();
button = driver.find_elements_by_xpath("//span[@class = 'appsMaterialWizButtonPaperbuttonContent exportButtonContent']");
driver.execute_script("arguments[0].click();", button[1]);

button= driver.find_elements_by_xpath("//span[@class = 'appsMaterialWizButtonPaperbuttonContent exportButtonContent']");
driver.execute_script("arguments[0].click();", button[1]);

driver.quit()