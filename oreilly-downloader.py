from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep 
from PIL import Image
import io
from io import StringIO
import os
import sys
print(' ============================================================= C y B e R ============================================================= ')
usr = input('Enter email: ')  
pwd = input('Enter pass: ')
night_mode = "YES"#input('Night-Mode (YES/NO): ')
# ------------------------------------------------------------------------------------------------------------------------------------------ #

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')

driver = webdriver.Chrome(executable_path=os.getcwd()+'\\chromedriver', chrome_options=chrome_options)
driver.get('https://www.oreilly.com/member/') 
sleep(3)
print ("[*] Connecting to oreilly [1/3] !")
try:
    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[1]/input').send_keys(usr)
    sleep(1)
    print ("[*] Connecting to oreilly [2/3] !")
    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[2]/input').send_keys(pwd)
    sleep(1)
    print ("[*] Connecting to oreilly [3/3] !")
    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[4]').click()
    print ("[*] Connected to oreilly !")
except Exception:
    print("\n Trying find by ID ...")
try:
    driver.find_element_by_id('email').send_keys(usr)
    sleep(1)
    print ("[*] Connecting to oreilly [2/3] !")
    driver.find_element_by_id('pass').send_keys(pwd)
    sleep(1)
    print ("[*] Connecting to oreilly [3/3] !")
    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[4]').click()
    print ("[*] Connected to oreilly !")
except Exception:
    print("\n Trying find by XPATH ...")
try:
    driver.find_element_by_xpath('//*[@placeholder="Email Address or Username"]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[1]/input').send_keys(usr)
    sleep(1)
    print ("[*] Connecting to oreilly [2/3] !")
    driver.find_element_by_id('pass').send_keys(pwd)
    sleep(1)
    print ("[*] Connecting to oreilly [3/3] !")
    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/form/div[4]').click()
    print ("[*] Connected to oreilly !")
except Exception:
    pass
# ----------------------------------------------------------------- FASE 2 ----------------------------------------------------------------- #
counter = 0
books = ["CWNA Certified Wireless Network Administrator Study Guide, 5th Edition"] # INTRODUCE LOS LIBROS QUE QUIERES DESCARGAR EN ESTA LISTA


def imprimir(name_book, trys_counter):
    if os.path.isdir(str(name_book)) == False:
	    os.mkdir(str(os.getcwd()+'\\'+str(name_book)))
    
    print(" 1/4 [Finding] {}".format(name_book))
    sleep(10)
    try:
        actions = ActionChains(driver)
        actions.move_to_element_with_offset(driver.find_element_by_tag_name('body'), 0,0)
        actions.move_by_offset(200+(10*trys_counter), 500).click().perform()
        sleep(5)
        driver.find_element_by_xpath('//*[@placeholder="Find a Solution..."]').send_keys(name_book)
        print(" 2/4 [Search] {}".format(name_book))
        sleep(1)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[2]/div[1]/form/div[3]/button').click()
        sleep(3)
        print(" 3/4 [Founded] {}".format(name_book))
        driver.find_element_by_xpath('//*[@id="main"]/div/div/article[2]/div/div[2]/h4/a').click()
        sleep(8)
        print(" 4/4 [Opening Book] {}".format(name_book))
        driver.find_element_by_xpath('//*[@id="container"]/article/section/div[1]/div[3]/span').click()
    except Exception as err:
        print(err)
        return "bad";
    sleep(3)
    print(' ==================================================== DOWNLOADING ==================================================== ')
    try:
        if night_mode == "YES":
            driver.find_element_by_id('font-controls').click()
            sleep(2)
            driver.find_element_by_id('night-mode').click()
            sleep(1)
            driver.find_element_by_id('font-controls').click()
    except:
        print('[CAUTION] night-mode disabled for this book.')

    i = 1
    while True:
        sleep(3)
        try:
            try:
                driver.find_element_by_xpath('//*[@id="container"]/div[2]/section/div[2]/a').click()
            except:
                print('Error on click or program finished')
                ask = "Y" #input('Print end page? (Y/N): ')
                if ask == 'Y':
                    print("[PRINTING] page_{}".format(i))
                    original_size = driver.get_window_size()
                    required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
                    required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
                    driver.set_window_size(required_width, required_height)
                    driver.find_element_by_tag_name('body').screenshot(str(os.getcwd())+'\\'+str(name_book)+'\\'+"page_{}.png".format(i))
                    driver.set_window_size(original_size['width'], original_size['height'])
                    break

            print("[PRINTING] page_{}".format(i))
            original_size = driver.get_window_size()
            required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
            required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
            driver.set_window_size(required_width, required_height)
            driver.find_element_by_tag_name('body').screenshot(str(os.getcwd())+'\\'+str(name_book)+'\\'+"page_{}.png".format(i))
            driver.set_window_size(original_size['width'], original_size['height'])
            
            i+=1
        except:
            print('Error on: page_{} [retrying...]'.format(i))
trys_counter = 0
while counter < len(books):
    driver.get('https://learning.oreilly.com/home/') 
    sleep(1)
    flag = imprimir(books[counter],trys_counter)
    if flag == "bad":
        trys_counter +=1
        print("nothing")
    else:
        counter += 1
    if trys_counter == 10:
        counter += 1
        trys_counter = 0

driver.close()
