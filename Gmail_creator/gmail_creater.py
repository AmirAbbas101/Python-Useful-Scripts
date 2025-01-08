import csv
import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from nameList import names

# Initialize the web driver
driver = webdriver.Firefox()
URL = "https://accounts.google.com/lifecycle/steps/signup/name?ddm=1&dsh=S-1324855153:1733545004495008&flowEntry=SignUp&flowName=GlifWebSignIn&ifkv=AX3vH39E0iYVTmn-NoMNM_C35EPrno8LWsRx2Qhr0HApkVLZ-Zc_Vql8ouaSQOiXzEmthrpOPAV5&TL=AKOx4s0jsDUVAuK39xdq8YC-XQcoZlfluUpxnOeIWSNZTDXrx5ot43MUREg8n3lm&continue=https://accounts.google.com/ManageAccount?nc%3D1"
driver.get(URL)


class GmailAccountCreator:
    def __init__(self):
        self.timeout = 20
        self.firstName = "David"
        self.lastName = "Jones"
        self.userName = "david.jones3452"
        self.userPassword = "3452david@jones"
        self.birthDate = "09/05/2003"

    def generateUniqueUsername(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        randomSuffix = random.randint(10000, 99999)
        self.userName = f"{self.firstName}.{self.lastName}{randomSuffix}"

    def clickNextButton(self):
        nextButton = driver.find_element(By.CSS_SELECTOR, '[type="button"]')
        driver.execute_script("arguments[0].scrollIntoView();", nextButton)
        nextButton.click()

    def fillNameFields(self):
        sleep(5)
        firstNameInput = driver.find_element(By.NAME, "firstName")
        lastNameInput = driver.find_element(By.NAME, "lastName")
        firstNameInput.clear()
        firstNameInput.send_keys(self.firstName)
        lastNameInput.clear()
        lastNameInput.send_keys(self.lastName)
        self.clickNextButton()

    def fillDateOfBirth(self, month="September", day=5, year=2001, gender="Male"):
        sleep(5)
        try:
            birthMonthSelector = Select(
                WebDriverWait(driver, self.timeout).until(
                    EC.element_to_be_clickable((By.ID, "month"))
                )
            )
            birthDayInput = driver.find_element(By.NAME, "day")
            birthYearInput = driver.find_element(By.NAME, "year")
            genderSelector = Select(
                WebDriverWait(driver, self.timeout).until(
                    EC.element_to_be_clickable((By.ID, "gender"))
                )
            )
            birthMonthSelector.select_by_visible_text(month)
            genderSelector.select_by_visible_text(gender)
            birthDayInput.clear()
            birthYearInput.clear()
            birthDayInput.send_keys(day)
            birthYearInput.send_keys(year)
            self.birthDate = f"{month} {day}, {year}"
            self.clickNextButton()
        except Exception as e:
            print(f"Error filling date of birth: {e}")

    def fillUsernameField(self):
        sleep(5)
        usernameInput = WebDriverWait(driver, self.timeout).until(
            EC.element_to_be_clickable((By.NAME, "Username"))
        )
        usernameInput.clear()
        usernameInput.send_keys(self.userName)
        nextButton = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        driver.execute_script("arguments[0].scrollIntoView();", nextButton)
        nextButton.click()

    def fillPasswordFields(self):
        sleep(5)
        self.userPassword = self.userName.replace(".", "@")[-1::-1]
        print(f"Generated Password: {self.userPassword}")
        passwordInput = WebDriverWait(driver, self.timeout).until(
            EC.element_to_be_clickable((By.NAME, "Passwd"))
        )
        confirmPasswordInput = WebDriverWait(driver, self.timeout).until(
            EC.element_to_be_clickable((By.NAME, "PasswdAgain"))
        )
        passwordInput.clear()
        confirmPasswordInput.clear()
        passwordInput.send_keys(self.userPassword)
        confirmPasswordInput.send_keys(self.userPassword)
        self.clickNextButton()

    def saveDataToCsv(self):
        data = [
            self.firstName,
            self.lastName,
            self.birthDate,
            self.userName,
            f"{self.userName}@gmail.com",
            self.userPassword,
        ]
        csvFileName = "UserData.csv"
        with open(csvFileName, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if file.tell() == 0:  # Write headers only if the file is empty
                writer.writerow(
                    [
                        "FirstName",
                        "LastName",
                        "DateOfBirth",
                        "Username",
                        "Email",
                        "Password",
                    ]
                )
            writer.writerow(data)
            print("User data successfully appended to the CSV file.")


def processUserData(userDetails):
    accountCreator = GmailAccountCreator()
    accountCreator.generateUniqueUsername(
        userDetails["firstName"], userDetails["lastName"]
    )
    accountCreator.clickNextButton()
    accountCreator.fillNameFields()
    accountCreator.fillDateOfBirth()
    accountCreator.fillUsernameField()
    accountCreator.fillPasswordFields()
    accountCreator.saveDataToCsv()


if __name__ == "__main__":
    for user in names:
        processUserData(user)
