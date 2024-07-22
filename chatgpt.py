from g4f.client import Client
import sys
sys.path.append('E://Studying_project/')
from Parser_news.news_parser_1 import currency
currency_list = str(currency())
flag = True
news = str('Дай оценку следующей новости и напиши сильно или нет повлияет эта новость на курс валюты EUR/USD: ' + currency_list + ' ответь на русском ' + ' ответ должен состоять из одного слова ')
while (flag):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": news}],

    )
    if (response.choices[0].message.content == '当前地区当日额度已消耗完, 请尝试更换网络环境'):
        flag = True
    else:
        flag = False
result_gpt = response.choices[0].message.content
