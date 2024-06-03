from os import chdir, startfile
chdir("crawler")

startfile('filemaker.py')
with open('tempfiles/link.txt', 'w') as l:
    l = input(
        'Введите адрес страницы с вопросами (с сайта https://db.chgk.info): ')

startfile('sitegetter.py')
