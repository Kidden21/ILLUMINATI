import os
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

'''
value = 149 = B14BatuKurau
value = 150 = BaganDatuk
value = 151 = BukitLarut
value = 152 = BukitMerah
value = 153 = ChangkatJong
value = 154 = Emp.Cenderoh
value = 693 = FeldaIjok
value = 155 = GuaTempurung
value = 156 = JambatanIskandar
value = 157 = KampongLalang
value = 158 = KampungGajah
value = 159 = KampungLintang
value = 692 = KelianGunungIjok
value = 700 = KgPantaiBesar
value = 160 = KgSahom
value = 694 = KgSempeneh
value = 699 = KgSgKuning
value = 690 = KgSgRambutan
value = 161 = KualaKenderong
value = 162 = KualaPari
value = 695 = LadangSeldings
value = 691 = LojiAirSgBayor
value = 163 = Parit
value = 673 = PasangApi_BaganDatok
value = 165 = PondokTanjong
value = 166 = PulauPangkor
value = 696 = RumahJPSAlorPongsu
value = 167 = Samagagah
value = 168 = Selama
value = 698 = SgArakgBatu20
value = 701 = SgKurauPondokTanjung
value = 697 = SgSelamaGuaPetai
value = 169 = SungaiBil
value = 170 = SungaiSlim
value = 171 = TanjungRambutan
value = 172 = TanjungTualang
value = 173 = TasikBanding
value = 174 = TelukSena
value = 175 = UluIjok
value = 176 = UluSlim
'''

chrome_driver_path = "/Users/Kidden/Downloads/Automation/chromedriver"
os.environ["webdriver.chrome.driver"] = chrome_driver_path
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://infobanjir2.water.gov.my/login.cfm")

search_field_username = driver.find_element_by_name("name")
search_field_username.send_keys("Kidden21")

search_field_pass = driver.find_element_by_name("pass")
search_field_pass.send_keys("Kidden21881")

driver.find_element_by_name("hantar").click()

driver.get("http://infobanjir2.water.gov.my/db/data_query.cfm?state=PRK")

#'149', '150', '151', '152', '153', '154', '693', '155', '156', '157',
#'158', '159', '692', '700', '160', '694', '699', '690', '161', '162',
#'695', '691', '163', '673', '165', '166', '696', '167', '168', '698',
#'701', '697', '175', '176'
#'169', '171'，'174'，
location = ['174']

#day = ['1', '8', '15', '22', '28']
#month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#year = ['2016 ', '2017 ', '2018 ']

for location_item in location:
    driver.find_element_by_xpath("//option[@value='"+location_item+"']").click()
    for year_item in year:
        driver.find_element_by_xpath("//select[@name='startyear']/option[text()='"+year_item+"']").click()
        #driver.find_element_by_xpath("//select[@name='startyear']/option[text()='2012 ']").click()
        for month_item in month:
            driver.find_element_by_xpath("//select[@name='startmonth']/option[text()='"+month_item+"']").click()
            #driver.find_element_by_xpath("//select[@name='startmonth']/option[text()='November']").click()
            for day_item in day:
                driver.find_element_by_xpath("//select[@name='startday']/option[text()='"+day_item+"']").click()
                #driver.find_element_by_xpath("//select[@name='startday']/option[text()='22']").click()
                
                driver.find_element_by_xpath("//input[@value='Search']").click()
                
                excel_button = driver.find_element_by_tag_name("area")
                
                try:
                    excel_button.click()
                except WebDriverException:
                    pass
                driver.find_element_by_xpath("//strong[text()=':Return to Previous Page']").click()               








