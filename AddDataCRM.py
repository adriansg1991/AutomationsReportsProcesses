# Corus
import csv
import time
from selenium import webdriver

# read CSV
with open ('corus_test.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        web = webdriver.Chrome(r'C:\chromedriver_win32\chromedriver.exe')
        web.get('https://www.coruslink.com/mylab/clinics/7355/edit#contact')
        time.sleep(1)

        #Identificación
        email_ident = 'adrian.sanchez@xxxxxx.com'
        email = web.find_element_by_xpath('//*[@id="user_email"]')
        email.send_keys(email_ident)
        password_ident= 'XXXXXXX'
        password = web.find_element_by_xpath('//*[@id="user_password"]')
        password.send_keys(password_ident)
        Submit_ident = web.find_element_by_xpath('//*[@id="new_user"]/div[4]/input')
        Submit_ident.click()
        time.sleep(1)
        
        # Pestaña: Contact data
        click_contact_data = web.find_element_by_xpath('/html/body/div/main/div[2]/div[2]/div[2]/div/form/ul/li[2]/a')
        click_contact_data.click()

        
        
        Mobile = web.find_element_by_xpath('//*[@id="clinic_mobile_phone"]') # añadir xpath de supercliente
        Mobile.send_keys(line[0])
        Submit = web.find_element_by_xpath('//*[@id="edit_clinic_7355"]/div[2]/input')
        Submit.click()
        web.close()