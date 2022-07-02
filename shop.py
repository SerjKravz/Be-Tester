# # 1. Откройте http://practice.automationtesting.in/
# # 2. Залогиньтесь
# # 3. Нажмите на вкладку "Shop"
# # 4. Откройте книгу "HTML 5 Forms"
# # 5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in/")
#
# my_account = driver.find_element(By.LINK_TEXT, "My Account")
# my_account.click()
# login = driver.find_element(By.ID, "username")
# login.send_keys("phil5909@ya.ru")
# log_password = driver.find_element(By.ID, "password")
# log_password.send_keys("Polspols8963")
# login_btn = driver.find_element(By.NAME, "login")
# login_btn.click()
#
# shop = driver.find_element(By.LINK_TEXT, "Shop")
# shop.click()
# book = driver.find_element(By.CSS_SELECTOR, ".products.masonry-done li:nth-child(3) img")
# book.click()
# title = driver.find_element(By.CSS_SELECTOR, ".summary h1")
# title_text = title.text
# if title_text == "HTML5 Forms":
#     print("заголовок книги называется: HTML5 Forms")
# else:
#     print("заголовок книги имеет другое название")
# #второй способ
# # assert "HTML5 Forms" in title_text
# driver.quit()


################### задание 2
# 1. Откройте http://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Откройте категорию "HTML"
# 5. Добавьте тест, что отображается три товара
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in/")
#
# my_account = driver.find_element(By.LINK_TEXT, "My Account")
# my_account.click()
# login = driver.find_element(By.ID, "username")
# login.send_keys("phil5909@ya.ru")
# log_password = driver.find_element(By.ID, "password")
# log_password.send_keys("Polspols8963")
# login_btn = driver.find_element(By.NAME, "login")
# login_btn.click()
#
# shop = driver.find_element(By.LINK_TEXT, "Shop")
# shop.click()
# product_html = driver.find_element(By.CSS_SELECTOR, ".product-categories li:nth-child(2) a")
# product_html.click()
# books_count = driver.find_elements(By.CSS_SELECTOR, ".products li")
# if len(books_count) == 3:
#     print("отображается три товара")
# else:
#     print("отображается не три товара")
# driver.quit()


#################################задание 3
# 1. Откройте http://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# • Используйте проверку по value
# 5. Отсортируйте товары по цене от большей к меньшей
# • в селекторах используйте класс Select
# 6. Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
# 7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
# • Используйте проверку по value
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in/")
#
# my_account = driver.find_element(By.LINK_TEXT, "My Account")
# my_account.click()
# login = driver.find_element(By.ID, "username")
# login.send_keys("phil5909@ya.ru")
# log_password = driver.find_element(By.ID, "password")
# log_password.send_keys("Polspols8963")
# login_btn = driver.find_element(By.NAME, "login")
# login_btn.click()
# shop = driver.find_element(By.LINK_TEXT, "Shop")
# shop.click()
#
# sort_selector = driver.find_element(By.CSS_SELECTOR, "select.orderby")
# sort_default = sort_selector.get_attribute("value")
# assert "menu_order" in sort_default
#
# select = Select(sort_selector)
# select.select_by_index(5)
#
# sort_selector = driver.find_element(By.CSS_SELECTOR, "select.orderby")
# new_select = sort_selector.get_attribute("value")
# assert "price-desc" in new_select
#
# driver.quit()
#################################### задание 4
# 1. Откройте http://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Откройте книгу "Android Quick Start Guide"
# 5. Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
# 6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
# 7. Добавьте явное ожидание и нажмите на обложку книги
#  • Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
# 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 5)
# driver.get("http://practice.automationtesting.in/")
#
# my_account = driver.find_element(By.LINK_TEXT, "My Account")
# my_account.click()
# login = driver.find_element(By.ID, "username")
# login.send_keys("phil5909@ya.ru")
# log_password = driver.find_element(By.ID, "password")
# log_password.send_keys("Polspols8963")
# login_btn = driver.find_element(By.NAME, "login")
# login_btn.click()
# shop = driver.find_element(By.LINK_TEXT, "Shop")
# shop.click()
# book = driver.find_element(By.CSS_SELECTOR, ".post-169 h3")
# book.click()
#
# old_price = driver.find_element(By.CSS_SELECTOR, ".price del>span")
# old_price_text = old_price.text
# new_price = driver.find_element(By.CSS_SELECTOR, ".price ins>span")
# new_price_text = new_price.text
# assert "₹600.00" in old_price_text
# assert "₹450.00" in new_price_text
#
# img = driver.find_element(By.CSS_SELECTOR, ".images img")
# img.click()
# img_open = wait.until(
#     EC.visibility_of_element_located((By.ID, "fullResImage"))
# )
# close_img = wait.until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close"))
# )
# close_img.click()
# driver.quit()
########################## задание 5
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# 2. Нажмите на вкладку "Shop"
# 3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
# 4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
# • Используйте для проверки assert
# 5. Перейдите в корзину
# 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
# 7. Используя явное ожидание, проверьте что в Total отобразилась стоимость
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 5)
# driver.get("http://practice.automationtesting.in/")
# shop = driver.find_element(By.LINK_TEXT, "Shop")
# shop.click()
# book_to_cart = driver.find_element(By.CSS_SELECTOR, ".post-182 a:nth-child(2)")
# book_to_cart.click()
#
# time.sleep(2)
# count_item = driver.find_element(By.CLASS_NAME, "cartcontents")
# cart_item = count_item.text
# total_price = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-contents span:nth-child(3)")
# cart_price = total_price.text
#
# assert "1 Item" in cart_item
# assert "₹180.00" in cart_price
#
# to_cart = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-contents")
# to_cart.click()
# subtorbal_price = wait.until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount.amount"), cart_price)
# )
# total = wait.until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total"), "₹189.00")
# )
# driver.quit()
# ######################################### задание 6
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# 2. Нажмите на вкладку "Shop"
# 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# •Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# •После добавления 1-й книги добавьте sleep
# 4. Перейдите в корзину
# 5. Удалите первую книгу
# •Перед удалением добавьте sleep
# 6. Нажмите на Undo (отмена удаления)
# 7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# • Предварительно очистите поле с помощью локатор_поля.clear()
# 8. Нажмите на кнопку "UPDATE BASKET"
# 9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
# 10. Нажмите на кнопку "APPLY COUPON"
# • Перед нажатимем добавьте sleep
# 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in/")
# shop = driver.find_element(By.LINK_TEXT, "Shop")
# shop.click()
#
# driver.execute_script("window.scrollBy(0, 300);")
# book_to_cart1 = driver.find_element(By.CSS_SELECTOR, ".post-182 a:nth-child(2)")
# book_to_cart1.click()
# time.sleep(2)
# book_to_cart2 = driver.find_element(By.CSS_SELECTOR, ".post-180 a:nth-child(2)")
# book_to_cart2.click()
# to_cart = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-contents")
# to_cart.click()
# del_book = driver.find_element(By.CSS_SELECTOR, "tbody>tr.cart_item:nth-child(1) td.product-remove a")
# time.sleep(2)
# del_book.click()
# undo = driver.find_element(By.LINK_TEXT, "Undo?")
# undo.click()
# quantity_book = driver.find_element(By.CSS_SELECTOR, "tbody>tr.cart_item:nth-child(1) .quantity input")
# quantity_book.clear()
# quantity_book_value = quantity_book.get_attribute("value")
# quantity_book.send_keys(3)
#
# update_besket = driver.find_element(By.NAME, "update_cart")
# update_besket.click()
# quantity_book_value_new = quantity_book.get_attribute("value")
# assert "3" in quantity_book_value_new
# time.sleep(2)
# apply_coupon = driver.find_element(By.CSS_SELECTOR, ".coupon input:nth-child(3)")
# apply_coupon.click()
# coupon_error = driver.find_element(By.CSS_SELECTOR, ".woocommerce-error li")
# coupon_error_text = coupon_error.text
# assert "Please enter a coupon code." in coupon_error_text
#
# driver.quit()
##################################Задание 7
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# 2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
# 3. Добавьте в корзину книгу "HTML5 WebApp Development"
# 4. Перейдите в корзину
# 5. Нажмите "PROCEED TO CHECKOUT"
# • Перед нажатием, добавьте явное ожидание
# 6. Заполните все обязательные поля
# • Перед заполнением first name, добавьте явное ожидание
# • Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
# • Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
# 7. Выберите способ оплаты "Check Payments"
# • Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
# 8. Нажмите PLACE ORDER
# 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
# 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
wait = WebDriverWait(driver, 5)
shop = driver.find_element(By.LINK_TEXT, "Shop")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")

book = driver.find_element(By.CSS_SELECTOR, ".post-182 a:nth-child(2)")
book.click()
time.sleep(1)
to_cart = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-contents")
to_cart.click()
produceed_to_check = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout a"))
)
produceed_to_check.click()
first_n = wait.until(
    EC.element_to_be_clickable((By.ID, "billing_first_name"))
)
first_n.send_keys("Serj")
last_n = driver.find_element(By.ID, "billing_last_name")
last_n.send_keys("Kravz")
email_field = driver.find_element(By.ID, "billing_email")
email_field.send_keys("5615ttt@ggg.com")
phone_field = driver.find_element(By.ID, "billing_phone")
phone_field.send_keys("+74952250055")
select_on = driver.find_element(By.CSS_SELECTOR, ".select2-chosen")
select_on.click()
select_input = driver.find_element(By.CSS_SELECTOR, ".select2-search input")
select_input.send_keys("Uganda")
select_choice = driver.find_element(By.CSS_SELECTOR, ".select2-result-label")
select_choice.click()
adress = driver.find_element(By.NAME, "billing_address_1")
adress.send_keys("Ugandino")
city = driver.find_element(By.NAME, "billing_city")
city.send_keys("Town")
state = driver.find_element(By.NAME, "billing_state")
state.send_keys("Uga")
post_code = driver.find_element(By.NAME, "billing_postcode")
post_code.send_keys("257007")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
payment_method = driver.find_element(By.ID, "payment_method_cheque")
payment_method.click()
place_order = driver.find_element(By.ID, "place_order")
place_order.click()
thank = wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"),
                                     "Thank you. Your order has been received."))
payment_type = wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot tr:nth-child(3) td"), "Check Payments")
)
driver.quit()