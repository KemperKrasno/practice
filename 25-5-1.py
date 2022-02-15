import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('F:/cromedriver/chromedriver.exe')
   pytest.driver.implicitly_wait(10)
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends1.herokuapp.com/login')

   yield

   pytest.driver.quit()


def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('putinov@list.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('55555')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
   images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
   descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0

def test_my_pets_all():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('putinov@list.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('55555')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
   pytest.driver.find_element_by_css_selector('button.navbar-toggler').click()
   pytest.driver.find_element_by_link_text('Мои питомцы').click()
   statistic = pytest.driver.find_element_by_css_selector('html > body > div > div > div')
   names = pytest.driver.find_elements_by_css_selector('div#all_my_pets > table > tbody > tr')
   parts = statistic.text.split()
   count = int(parts[2])
   assert count == len(names)

def test_my_pets_half_photo():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('putinov@list.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('55555')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
   pytest.driver.find_element_by_css_selector('button.navbar-toggler').click()
   pytest.driver.find_element_by_link_text('Мои питомцы').click()
   statistic = pytest.driver.find_element_by_css_selector('html > body > div > div > div')
   images = pytest.driver.find_elements_by_css_selector('div#all_my_pets > table > tbody > tr > th > img')
   parts = statistic.text.split()
   count = int(parts[2])
   img_counter=0
   for i in range(len(images)):
      if images[i].get_attribute('src') != '':
         img_counter += 1
   assert img_counter >= count/2

def test_my_pets_all_data():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('putinov@list.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('55555')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
   pytest.driver.find_element_by_css_selector('button.navbar-toggler').click()
   pytest.driver.find_element_by_link_text('Мои питомцы').click()
   types = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody[1]/tr[1]/td[2]')))
   ages = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody[1]/tr[1]/td[3]')))
   names = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table[1]/tbody[1]/tr[1]/td[1]'))
   )
   for i in range(len(names)):
      assert names[i].text != ''
      assert types[i].text != ''
      assert ages[i].text != ''

def test_my_pets_different_names():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('putinov@list.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('55555')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
   pytest.driver.find_element_by_css_selector('button.navbar-toggler').click()
   pytest.driver.find_element_by_link_text('Мои питомцы').click()
   names = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table[1]/tbody[1]/tr[1]/td[1]')
   names_mass = list(names)
   for i in range(len(names)):
      dable_name = 0
      for j in range(len(names_mass)):
         if names[i] == names_mass[j]:
            dable_name += 1
            assert dable_name != 1

def test_my_pets_no_duplicates():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('putinov@list.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('55555')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
   pytest.driver.find_element_by_css_selector('button.navbar-toggler').click()
   pytest.driver.find_element_by_link_text('Мои питомцы').click()
   names = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table[1]/tbody[1]/tr[1]/td[1]')
   types = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table[1]/tbody[1]/tr[1]/td[2]')
   ages = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table[1]/tbody[1]/tr[1]/td[3]')
   pets[0] = names[0] + types[0] + ages[0]
   for i in range(len(names)):
      pets[i] = names[i] + types[i] + ages[i]
   pets_mass = list(pets)
   for i in range(len(pets)):
      duplicate = 0
      for j in range(len(pets_mass)):
         if pets[i].text == pets_mass[j].text:
            duplicate += 1
            assert duplicate != 1

