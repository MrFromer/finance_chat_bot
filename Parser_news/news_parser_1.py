from bs4 import BeautifulSoup as BS
from selenium import webdriver
import time


url = "https://www.fxclub.org/economcalendar#/"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)
html = driver.page_source
soup = BS(html, "html.parser")

#удаляем уже прошедшие новости 
def delete_div(code,tag,arg):
    for div in code.find_all(tag, arg): 
        div.decompose()

delete_div(soup, "div", {'class':'economcalendar-column obsolete'})


#все блоки валютных пар
try:
    items = soup.find_all('div', class_='economcalendar-column')
except Exception:
    print('Error')
#print(items)

#print(soup.find('div', class_='layout__region layout__region--first'))

def currency():
    itog = []
    #последние 4
    items_c = items[0:4]

    print('Количество валютных пар в новостях: ', len(items_c))
    for item in items_c:
        #print(items_c.index(f'{item}'))
        #валютная пара
        try:
            currency_news = item.find('div', class_='economcalendar-row row-numbers').find('div', class_='impact').find('span').text
        except NameError:
            print('Name Error')

        if currency_news == '–':
            itog.append('Нет влияния на валютную пару')
        else:
            #время валютной пары
            time_c = item.find('div',class_='time').text.strip()

            if item.find("name importance--medium") != -1:
                #сама новость
                try:
                    text_news = item.find('div', class_='name importance--medium').text.strip()
                except Exception:
                    print('Error')
                itog.append(f'Влияние на валютную пару {currency_news} среднее, новость вышла в {time_c} \nНовость: {text_news}')
            elif item.find("name importance--high") != -1:
                try:
                    text_news = item.find('div', class_='name importance--high').text.strip()
                except Exception:
                    print('Error')
                itog.append(f'Влияние на валютную пару {currency_news} высокое, новость вышла в {time_c} \nНовость: {text_news}')

    itog.append('Нет новостей по этой валютной паре')
    return itog

#currency()