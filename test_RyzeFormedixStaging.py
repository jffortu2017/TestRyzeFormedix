from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.ID, "btnSubmit").click()

class NavigatingPages:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = webdriver.ActionChains(self.driver)

    def navigate_to_pages(self):
        #Navigate to Repository > Studies
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[contains(@class,'has-sub-menu')])[1]")))
        self.actions.move_to_element(self.driver.find_element(By.XPATH, "(//div[contains(@class,'has-sub-menu')])[1]")).perform()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//p[contains(text(),'Browse, update and transition studies through thei')])[1]")))
        self.driver.find_element(By.XPATH, "(//p[contains(text(),'Browse, update and transition studies through thei')])[1]").click()

        #Enter Tech Study View
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[@id='fdxMdbContainerListItem0MenuToggle'])[1]")))
        self.driver.find_element(By.XPATH, "(//span[@id='fdxMdbContainerListItem0MenuToggle'])[1]").click()
        self.driver.find_element(By.XPATH, "(//li[@id='fdxMdbContainerListItem0View'])[1]").click()

        #Enter Data Acquisition View
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//li[@id='ViewAssetGroupdataAcquisition'])[1]")))
        self.driver.find_element(By.XPATH, "(//li[@id='ViewAssetGroupdataAcquisition'])[1]").click()

        #Select View Forms
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='fdx-mdb-asset-type-list-item-details'])[4]")))
        self.driver.find_element(By.XPATH, "(//div[@class='fdx-mdb-asset-type-list-item-details'])[4]").click()

class UserActions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = webdriver.ActionChains(self.driver)

    def navigate_medical_history_form(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[contains(@class,'assetBrowseListItem')])[3]")))
        self.driver.find_element(By.XPATH, "(//div[contains(@class,'assetBrowseListItem')])[3]").click()

    def edit_description(self, input_description, input_locale):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//button[@id='switchEditMode'])[1]")))
        self.driver.find_element(By.XPATH, "(//button[@id='switchEditMode'])[1]").click()
        self.driver.find_element(By.XPATH, "(//button[@id='editPropsAddEntrydescription'])[1]").click()
        self.driver.find_element(By.XPATH, "(//textarea[@id='assetLocaleEditTextTextareadescription'])[1]").send_keys(input_description)
        self.driver.find_element(By.XPATH, "(//input[@id='localeInputdescription'])[1]").send_keys(input_locale)
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, "(//span[@id='errorListErrors'])[1]")))
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Update'])[1]").click()

    def verify_description_changes(self):
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, "(//div[@id='asset-reordering-disabled'])[1]")))
        self.driver.find_element(By.XPATH, "(//button[@id='switchEditMode'])[1]").click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@id='descriptionTitle'])[1]")))
        property_description = self.driver.find_element(By.XPATH, "(//div[@class='locale'])[1]")
        main_form_description = self.driver.find_element(By.XPATH, "(//span[@id='formDescription'])[1]")

        #Verifying if Property Panel Matches the Main Form Description
        try:
            assert main_form_description.text in property_description.text
            print("Change successful!")
        except AssertionError:
            print("Saved input is different from the Main Form!")

    def logout(self):
        self.actions.move_to_element(self.driver.find_element(By.XPATH, "(//div[contains(@class,'has-sub-menu')])[3]")).perform()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//p[normalize-space()='Sign out of ryze'])[1]")))
        self.driver.find_element(By.XPATH, "(//p[normalize-space()='Sign out of ryze'])[1]").click()

class UserActionsFramework:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=webdriver.chrome.service.Service(driver_path))
        self.login_page = LoginPage(self.driver)
        self.navigate_page = NavigatingPages(self.driver)
        self.form_page = UserActions(self.driver)

    def login(self, username, password):
        self.driver.get("https://ryze-staging.formedix.com/sign-in")
        self.login_page.login(username, password)

    def edit_medical_history_description(self, description, locale):
        self.navigate_page.navigate_to_pages()
        self.form_page.navigate_medical_history_form()
        self.form_page.edit_description(description, locale)
        self.form_page.verify_description_changes()

    def logout(self):
        self.form_page.logout()

    def close(self):
        self.driver.quit()

#User Action Flow
if __name__ == "__main__":
    framework = UserActionsFramework("C:\OneDrive\Documents\ChromeDriver 114.0.5735.90\chromedriver.exe")
    framework.login("testteamtechtest", "Ryz3T3st!x")
    framework.edit_medical_history_description("test_description", "us")
    framework.logout()
    framework.close()