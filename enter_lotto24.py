# Enter Lotto Numebrs on lotto24.de
from selenium import webdriver
import time
import sqlite3

NUMBER_TICKETS = 4

lotto_rows = 8 * NUMBER_TICKETS

conn = sqlite3.connect('lottoX.db')
c = conn.cursor()

list_of_lotto = c.execute(f'''  
    SELECT num_1, num_2, num_3, num_4, num_5,euro_1,euro_2, count(*) as hit  
    FROM lotto 
    GROUP BY num_1, num_2, num_3, num_4, num_5
    ORDER BY hit DESC
    LIMIT {lotto_rows};
''').fetchall()


def get_new_list(list_of_lotto):
    new_list = []
    for tup in list_of_lotto:
        new_list.append(list(tup[:-1]))
    return new_list

lotto_to_list = get_new_list(list_of_lotto)

options = webdriver.ChromeOptions()
driver = webdriver.Chrome('/Volumes/REDTEAM/lottokingkarl/chromedriver') 
driver.get('https://www.lotto24.de/webshop/profile/login.htm')

time.sleep(5)
username = driver.find_element_by_css_selector("#consoleLoginNickname")
password = driver.find_element_by_css_selector("#consoleLoginPassword")

username.send_keys("<YOUR-EMAIL>")
password.send_keys("<YOUR-PASSWORD>")

time.sleep(1)
driver.find_element_by_css_selector("#btLogin1").click()
time.sleep(5)
driver.find_element_by_css_selector("#consent_prompt_submit").click()

for num in range(0,NUMBER_TICKETS):
    time.sleep(2)
    driver.get("https://www.lotto24.de/webshop/product/eurojackpot")
    time.sleep(3)

    lotto_listen = lotto_to_list[:8]
    counter = 0
    for lotto_list in lotto_listen:

        driver.find_element_by_css_selector(f"#field{counter+1} > div.numberBlock").click()
        for lotto_num in lotto_list[:5]:
            driver.find_element_by_css_selector(f"#contentArea > div > div > div.productHTML.ejp.contentbox.ng-app\\:ejpTicketApp.ng-scope.ticketLoadComplete > span > div > div > div.selectedFieldBlock > div.selectedField > div:nth-child(1) > div:nth-child({lotto_num+1})").click()
        for euro_num in lotto_list[-2:]:
            driver.find_element_by_css_selector(f"#contentArea > div > div > div.productHTML.ejp.contentbox.ng-app\\:ejpTicketApp.ng-scope.ticketLoadComplete > span > div > div > div.selectedFieldBlock > div.selectedField > div:nth-child({euro_num+2})").click()

        print(f"Getippte Lottozahlen: {lotto_list[:5]} - Eurozahlen: {lotto_list[-2:]}")
        print("-----------------------------------------------------------------------")
        # Feld abgeben
        time.sleep(1)
        driver.find_element_by_css_selector("#contentArea > div > div > div.productHTML.ejp.contentbox.ng-app\:ejpTicketApp.ng-scope.ticketLoadComplete > span > div > div > div.fieldOptions > a.confirm.middle.further--arrow").click()
        counter += 1
            
    del lotto_to_list[:8]

    # schein abgeben 
    time.sleep(2)
    driver.find_element_by_css_selector("#productSubmit").click()
time.sleep(3)
