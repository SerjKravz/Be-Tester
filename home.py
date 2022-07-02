# 1. Откройте http://practice.automationtesting.in/
# 2. Проскролльте страницу вниз на 600 пикселей
# 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
# 4. Нажмите на вкладку "REVIEWS"
# 5. Поставьте 5 звёзд
# 6. Заполните поле "Review" сообщением: "Nice book!"
# 7. Заполните поле "Name"
# 8. Заполните "Email"
# 9. Нажмите на кнопку "SUBMIT"

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

driver.execute_script("window.scrollBy(0,600);") #скролим на 600 пикселей вниз
selenium_ruby = driver.find_element(By.CSS_SELECTOR, ".post-160 h3") #ищем книгу
selenium_ruby.click()
reviews_btn = driver.find_element(By.CSS_SELECTOR, ".reviews_tab a") #открываем вкладку ревью
reviews_btn.click()
star5 = driver.find_element(By.CSS_SELECTOR, ".star-5") #выставляем 5 звёзд
star5.click()
comment_text = driver.find_element(By.ID, "comment") #ищем поле комментариев и оставляем свой
comment_text.send_keys("Nice book!")
name_pl = driver.find_element(By.ID, "author") #оставляем своё имя
name_pl.send_keys("SerjK")
email_pl = driver.find_element(By.ID, "email") #оставляем свою почту
email_pl.send_keys("klgd@klgd.klgd")
submit_btn = driver.find_element(By.NAME, "submit") #сохраняем
submit_btn.click()

driver.quit()