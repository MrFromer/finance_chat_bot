# def get_data(url):
#     headers = {
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
#     }

#     req = requests.get(url, headers)

#     # with open('projects.html', 'w') as file:
#     #     file.write(req.content)
        

#     soup = BeautifulSoup(req.content, 'lxml')
#     print(soup)
# get_data('https://www.fxclub.org/economcalendar')





#22.04.24
# #валютная пара
# try:
#     currency = soup.find('div', class_='item-wrapper').find('div', class_='impact').find("span").text
# except NameError:
#     print('Name Error')

# #время валютки
# try:
#     time_c = soup.find('div', class_='economcalendar-column').find('div', class_='item-wrapper').find('div', class_='economcalendar-row row--time-country').find('div',class_='time').text.strip()
# except Exception:
#     print('Error')

# items_str = str(items)
# if items_str.find("name importance--medium") != -1:
#     print(f'Влияние на валютную пару {currency} среднее, новость вышла в {time_c}')
# elif items_str.find("name importance--high") != -1:
#     print(f'Влияние на валютную пару {currency} высокое, новость вышла в {time_c}')