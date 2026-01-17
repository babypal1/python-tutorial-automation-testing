import time
from re import search
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()  # Auto matches your Chrome version
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.ID,"checkBoxOption1").click()
# driver.find_element(By.ID,"checkBoxOption2").click()
# driver.find_element(By.NAME,"checkBoxOption1").click()
# driver.find_element(By.CLASS_NAME,"radioButton").click()
# driver.find_element(By.CLASS_NAME,"radioButton").click()
# driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"InterviewQues/ResumeAssistance/Material").click()
# driver.find_element(By.XPATH,"//input[@id='name']").send_keys('baby')
# sleep(2)
# driver.find_element(By.XPATH,"//input[@id='name']").clear()
# driver.find_element(By.XPATH,"//input[@id='name']").send_keys('pal')
# driver.find_element(By.XPATH,"//input[@id = 'alertbtn']").click()
# sleep(2)
# alert_example = driver.find_element(By.XPATH,"//legend[text()='Switch Tab Example']")
# alert_example_text = alert_example.text
#
# print(alert_example_text)
driver.get("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
driver.maximize_window()
# search_box = driver.find_element(By.XPATH,"//input[@class='Pke_EE']")
# search_box.send_keys("one plus")
# search_box.send_keys
# dropdown_options = driver.find_elements(
#     "xpath",
#     "(//form[contains(@class,'header-form-search')]//a)")
# time.sleep(2)
# for index,option in enumerate(dropdown_options):
#     print(f"link present in {index+1} option:{option.get_attribute('href')}")
#     print(f"present in {index+1} option : {option.text}")
#     if "one plus" in option.text:
#         option.click()
#         break
#     else:
#         print('one plus not found')
email_field = driver.find_element(By.XPATH, "//input[@type='email']")
email_field.send_keys("babypal0601@gmail.com")
print("email_field")
time.sleep(1)
Next_button = driver.find_elements(By.XPATH,"//span[text()= 'Next']")
Next_button[0].click()




# driver.find_elements(By.XPATH,"(//div)//span[@class = 'T-Jo J-J5-Ji T-Jo-auq T-Jo-Jp']")
# print("**************")



