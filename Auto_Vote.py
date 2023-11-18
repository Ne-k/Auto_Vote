import multiprocessing
import random
import time
import requests
import json
import re
import html
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def vote():
    user_agents = [
        'Mozilla_foo_bar_Chrome',
        'Mozilla_foo_bar_Firefox',
        'Mozilla_foo_bar_Safari',
        'Mozilla_foo_bar_Edge',
        'Mozilla_foo_bar_Opera'
    ]

    while True:
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(options=chrome_options)

        driver.get("https://campustech.org/tech-the-halls?entry_id=d8a1c99d-3da3-4858-a75f-76bcfc547708")

        vote_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "vote_me"))
        )

        print("Pressed vote button")

        vote_button.click()

        s = requests.Session()

        agent = random.choice(user_agents)
        response = s.get(f'http://api.guerrillamail.com/ajax.php?f=get_email_address&ip=127.0.0.1&agent={agent}')
        data = json.loads(response.text)
        email = data['email_addr']

        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "verification_email"))
        )
        email_input.send_keys(email)
        print("Entered in email " + email)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "cta_submit"))
        )
        submit_button.click()
        print("Email submit button pressed")

        while True:
            response = s.get(f'http://api.guerrillamail.com/ajax.php?f=check_email&seq=1&email={email}&agent={agent}')
            data = json.loads(response.text)
            if 'list' in data:
                emails = data['list']
                for email in emails:
                    if email['mail_from'] == 'messages-noreply-bounce@campustech.org':

                        response = s.get(
                            f'http://api.guerrillamail.com/ajax.php?f=fetch_email&email_id={email["mail_id"]}&email={email}&agent={agent}')
                        data = json.loads(response.text)

                        decoded_mail_body = html.unescape(data['mail_body'])
                        soup = BeautifulSoup(decoded_mail_body, 'html.parser')
                        mail_body = soup.get_text()

                        if mail_body:

                            match = re.search(r'\b\d{6}\b', mail_body)
                            if match:
                                code = match.group(0)

                                code_input = WebDriverWait(driver, 10).until(
                                    EC.presence_of_element_located((By.ID, "verification_code"))
                                )
                                code_input.send_keys(code)
                                print("Entered in verification code " + code)

                                complete_button = WebDriverWait(driver, 10).until(
                                    EC.element_to_be_clickable((By.ID, "cta_complete"))
                                )
                                complete_button.click()

                                print("Vote Successful!")

                                time.sleep(5)

                                driver.quit()

                                exit()

            time.sleep(10)


if __name__ == "__main__":
    processes = []
    for _ in range(100):  # number of instances
        time.sleep(5)
        p = multiprocessing.Process(target=vote)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

