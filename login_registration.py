# 1. Откройте http://practice.automationtesting.in/
# 2. Нажмите на вкладку "My Account Menu"
# 3. В разделе "Register", введите email для регистрации
# 4. В разделе "Register", введите пароль для регистрации
# 5. Нажмите на кнопку "Register"

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in/")
#
# my_account = driver.find_element(By.LINK_TEXT, "My Account")
# my_account.click()
# # Логин
# reg_email = driver.find_element(By.NAME, "email")
# reg_email.send_keys("phil5909@ya.ru")
# reg_password = driver.find_element(By.ID, "reg_password")
# reg_password.send_keys("Polspols8963")
# reg_btn = driver.find_element(By.NAME, "register")
# reg_btn.click()
#
# driver.quit()
################################# Задание 2
# 1. Откройте http://practice.automationtesting.in/
# 2. Нажмите на вкладку "My Account Menu"
# 3. В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
# 4. В разделе "Login", введите пароль для логина # данные можно взять из предыдущего теста
# 5. Нажмите на кнопку "Login"
# 6. Добавьте проверку, что на странице есть элемент "Logout"

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
#Авторизация
my_account = driver.find_element(By.LINK_TEXT, "My Account")
my_account.click()
login = driver.find_element(By.ID, "username")
login.send_keys("phil5909@ya.ru")
log_password = driver.find_element(By.ID, "password")
log_password.send_keys("Polspols8963")
login_btn = driver.find_element(By.NAME, "login")
login_btn.click()

#проверка наличия элемента Logout
logout = driver.find_elements(By.LINK_TEXT, "Logout")
if bool(logout) is True:
    print("элемент Logout есть на странице")
else:
    print("элемент Logout отсутствует на странице")
#второй способ
# logout = driver.find_element(By.LINK_TEXT, "Logout")
# logout_text = logout.text
# assert "Logout" in logout_text
driver.quit()