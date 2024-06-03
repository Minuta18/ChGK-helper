from os import chdir, startfile
chdir("crawler")

startfile('filemaker.py')
with open('tempfiles/link.txt', 'w') as l:
    link = input(
        'Введите адрес страницы с вопросами (с сайта https://db.chgk.info): ')
    l.write(link)

startfile('sitegetter.py')
startfile('rawreader.py')
