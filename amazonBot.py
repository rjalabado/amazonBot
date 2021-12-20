import time
from selenium import webdriver

browser = webdriver.Chrome('/chromedriver.exe')

#strix 3080
browser.get("https://www.amazon.com/gp/product/B08HH5WF97/ref=ox_sc_saved_title_1?smid=ATVPDKIKX0DER&psc=1")


loop = True
submitLoop = True

email = "exampleEmail@example.com"
password = "ExamplePassword"

while loop:
        try:

            browser.find_element_by_id("buy-now-button").click()
            browser.find_element_by_id("ap_email").send_keys(email)
            browser.find_element_by_id("continue").click()
            browser.find_element_by_id("ap_password").send_keys(password)
            browser.find_element_by_id("signInSubmit").click()
            
            while submitLoop:
                try:
                    browser.find_element_by_id("submitOrderButtonId").click()
                    submitLoop = False
                except:
                    time.sleep(.25)
                    print("attempting submission")


            print("Order placed")

            loop = False
            
        except:
            time.sleep(1)
            browser.refresh()
