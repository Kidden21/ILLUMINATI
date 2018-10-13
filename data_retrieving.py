import os
import selenium
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import datetime
import calendar


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

def retry_login():
    i = True
    while i:
        try:
            current_url = driver.current_url
            if current_url == "http://infobanjir2.water.gov.my/login.cfm":
                insert_info()
                sign_in()
                driver.get("http://infobanjir2.water.gov.my/db/data_query.cfm?state=PRK")
            else:
                i = False
        except selenium.common.exceptions.UnexpectedAlertPresentException:
            alert = driver.switch_to.alert
            alert.accept()

def insert_info():
    search_field_username = driver.find_element_by_name("name")
    search_field_username.send_keys("Kidden21")

    search_field_pass = driver.find_element_by_name("pass")
    search_field_pass.send_keys("Kidden21894")

def sign_in():
    driver.find_element_by_name("hantar").click()

def get_year():
    item = []
    current_date = datetime.datetime.now()
    current_date = str(current_date)
    year = str(current_date[:4])
    year = str(year) + " "
    item.append(year)
    return item

def get_month():
    item = []
    current_date = datetime.datetime.now()
    current_date = str(current_date)
    month = str(current_date[5:7])
    month = calendar.month_name[int(month)]
    item.append(month)
    return item

def get_day():
    item = []
    current_date = datetime.datetime.now()
    current_date = str(current_date)
    day = str(current_date[8:10])
    item.append(day)
    return item

def menu():
    print("1. Yes")
    print("2. No")
    

while True:
    try:
        menu()
        answer = int(input("You want to start download? If yes, please enter 1. "))
        if answer == 1:
            chrome_driver_path = "/Users/Kidden/Desktop/ILLUMINATI/chromedriver"
            os.environ["webdriver.chrome.driver"] = chrome_driver_path
            driver = webdriver.Chrome(chrome_driver_path)
            driver.implicitly_wait(30)
            driver.maximize_window()
            driver.get("http://infobanjir2.water.gov.my/login.cfm")

            retry_login()
            ##location = ['149', '150', '151', '152', '153', '155', '156', '157', '158', '159', '699']
            location = ['149']

            item_year = get_year()
            item_month = get_month()
            item_day = get_day()

            for location_item in location:
                driver.find_element_by_xpath("//option[@value='"+location_item+"']").click()
                for value_year in item_year:
                    driver.find_element_by_xpath("//select[@name='startyear']/option[text()='"+value_year+"']").click()
                    for value_month in item_month:
                        driver.find_element_by_xpath("//select[@name='startmonth']/option[text()='"+value_month+"']").click()
                        for value_day in item_day:
                            driver.find_element_by_xpath("//select[@name='startday']/option[text()='"+value_day+"']").click()
                            
                            driver.find_element_by_xpath("//input[@value='Search']").click()
                            
                            excel_button = driver.find_element_by_tag_name("area")
                            
                            try:
                                excel_button.click()
                            except WebDriverException:
                                pass
                            driver.find_element_by_xpath("//strong[text()=':Return to Previous Page']").click()
        elif answer == 2:
            break
        else:
            print("Please enter a valid command.")
    except SyntaxError, NameError:
        print("Please enter a valid command.")







