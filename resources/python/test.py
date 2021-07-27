import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def DataMolding(URL):
    
    res = requests.get(URL)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    info_list = []
    datum_list = []
    datum = {}
    
    


    basic_info = soup.find('div', attrs={'class': 'g-container info basic'})
    basic_culms = basic_info.find_all('tr')

    basic_sales = soup.find('div', attrs={'class': 'g-container info sales'})
    sales_culms = basic_sales.find_all('tr')

    info_list.append(basic_culms)
    info_list.append(sales_culms)



    for culms in info_list:
        for culm in culms:
            data = culm.text.split(" ", 1)
            data[1] = data[1].replace('\n', ' ')
            data[1] = data[1].replace('\r', ' ')
            data[1] = data[1].replace('/', ' ')
            data[1] = " ".join(data[1].split())
            datum[data[0]] = data[1]
        datum_list.append(datum)
        datum = {}


    return datum_list

def CampsiteSearch(campsiteWord):
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options = options)

    url = 'https://www.nap-camp.com/'
    browser.get(url)
    sleep(2)

    elem_search = browser.find_element_by_class_name('suggest-form')
    sleep(1)
    elem_search.send_keys(campsiteWord)
    sleep(1)
    elem_search_btn = browser.find_element_by_class_name('basic-button')
    elem_search_btn.click()
    sleep(1)
    
    
    elem_target_atag = browser.find_element_by_css_selector(".campsite-item")
    sleep(1)
    URL =elem_target_atag.get_attribute("href")
    sleep(1)
    
    print(URL)

    browser.quit()

    result = DataMolding(URL)
    
        
    return result


CampsiteSearch("ふもとっぱら")