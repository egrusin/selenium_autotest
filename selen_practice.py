import os
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_num_from_alert(browser):
    alert = browser.switch_to.alert
    text_alert = alert.text
    value = text_alert[(text_alert.index(': ')) + 2:]
    time.sleep(2)
    alert.accept()
    return value


def func(x):
    return math.log((abs(12 * math.sin(x))), math.e)


url1 = 'https://suninjuly.github.io/math.html'
url2 = 'http://suninjuly.github.io/get_attribute.html'
url3 = 'http://suninjuly.github.io/selects1.html'
url4 = 'http://suninjuly.github.io/execute_script.html'
url5 = 'http://suninjuly.github.io/file_input.html'
url6 = 'http://suninjuly.github.io/alert_accept.html'
url7 = 'http://suninjuly.github.io/redirect_accept.html'
url8 = 'http://suninjuly.github.io/explicit_wait2.html'


def s1(url):
    with webdriver.Chrome() as browser:
        browser.get(url=url)
        x = int(browser.find_element(By.ID, 'input_value').text)
        ans = func(x)

        browser.find_element(By.ID, 'robotCheckbox').click()
        browser.find_element(By.ID, 'robotsRule').click()
        browser.find_element(By.ID, 'answer').send_keys(ans)
        browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()
        time.sleep(2)

        answer_value = get_num_from_alert(browser)
        print(answer_value)


def s2(url):
    with webdriver.Chrome() as browser:
        browser.get(url=url)
        x = int(browser.find_element(By.ID, 'treasure').get_attribute('valuex'))
        ans = func(x)

        browser.find_element(By.ID, 'robotCheckbox').click()
        browser.find_element(By.ID, 'robotsRule').click()
        browser.find_element(By.ID, 'answer').send_keys(ans)
        browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()
        time.sleep(2)

        answer_value = get_num_from_alert(browser)
        print(answer_value)


def s3(url):
    with webdriver.Chrome() as browser:
        browser.get(url=url)
        x1 = int(browser.find_element(By.ID, 'num1').text)
        x2 = int(browser.find_element(By.ID, 'num2').text)
        ans = str(x1 + x2)

        browser.find_element(By.TAG_NAME, "select").click()
        for i in browser.find_elements(By.TAG_NAME, 'option')[1:]:
            if i.text == ans:
                i.click()

        browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()
        time.sleep(2)

        answer_value = get_num_from_alert(browser)
        print(answer_value)


def scroll_and_click(button, browser):
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


def s4(url):
    with webdriver.Chrome() as browser:
        browser.get(url=url)
        x = int(browser.find_element(By.ID, 'input_value').text)
        ans = func(x)

        browser.find_element(By.ID, 'answer').send_keys(ans)
        scroll_and_click(browser.find_element(By.ID, 'robotCheckbox'), browser)
        scroll_and_click(browser.find_element(By.ID, 'robotsRule'), browser)

        scroll_and_click(browser.find_element(By.CLASS_NAME, 'btn.btn-primary'), browser)
        time.sleep(2)

        answer_value = get_num_from_alert(browser)
        print(answer_value)


def send_file(element):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'files/file.txt')
    element.send_keys(file_path)


def s5(url):
    with webdriver.Chrome() as browser:
        browser.get(url=url)
        form = {0: 'Ivan', 1: 'Ivanov', 2: 'ivanov_ivan@mail.ru'}

        fields = browser.find_elements(By.CLASS_NAME, 'form-control')
        for ans, field in enumerate(fields):
            field.send_keys(form[ans])

        there_file = browser.find_element(By.ID, 'file')
        send_file(there_file)

        browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
        time.sleep(5)

        answer_value = get_num_from_alert(browser)
        print(answer_value)


def s6(url):
    with webdriver.Chrome() as browser:
        browser.get(url=url)
        browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

        alert = browser.switch_to.alert
        alert.accept()

        x = int(browser.find_element(By.ID, 'input_value').text)
        ans = func(x)
        browser.find_element(By.ID, 'answer').send_keys(ans)
        browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

        answer_value = get_num_from_alert(browser)
        print(answer_value)


def s7(url):
    with webdriver.Chrome() as browser:
        browser.get(url=url)
        browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)

        x = int(browser.find_element(By.ID, 'input_value').text)
        ans = func(x)
        browser.find_element(By.ID, 'answer').send_keys(ans)
        browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

        answer_value = get_num_from_alert(browser)
        print(answer_value)


def s8(url):
    with webdriver.Chrome() as browser:
        browser.get(url=url)
        while True:
            value = browser.find_element(By.ID, 'price')
            if value.text and int(value.text.strip('$')) == 100:
                browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
                break
            else:
                time.sleep(0.5)

        button = browser.find_element(By.ID, 'input_value')

        x = int(button.text)
        ans = func(x)
        browser.find_element(By.ID, 'answer').send_keys(ans)
        browser.find_element(By.ID, 'solve').click()
        time.sleep(3)

        answer_value = get_num_from_alert(browser)
        print(answer_value)




s8(url8)

