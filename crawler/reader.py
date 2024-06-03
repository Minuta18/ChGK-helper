from pywebcopy import save_webpage
from os import startfile, getcwd, chdir
from json import dump
import validators


print("Текущая деректория:", getcwd())


def getsite(siteurl):
    chdir("crawler")
    startfile("filemaker.py")
    print("\033[1m\033[31m{}\033[0m".format(
        'ВНИМАНИЕ! Для корректной работы необходимо соединение с интернетом.'))
    if (siteurl[:len('https://db.chgk.info/tour/')] != 'https://db.chgk.info/tour/'):
        print("\033[1m\033[31m{}\033[0m".format(
            'ОШИБКА! Введённая ссылка указывает на неправильный сайт!'))
        raise ValueError
    save_webpage(
        url=siteurl,
        project_folder='/богдан/програмирование/Python/КРОК 2024/' +
        'ChGK-helper/crawler/tempfiles',
        project_name='site',
        bypass_robots=True,
        debug=True,
        open_in_browser=True,
        delay=None,
        threaded=False,
    )
    return siteurl[len('https://db.chgk.info/tour/'):]


def getrawquestions(tourname):
    # kostyl_dlya_VScode = 'програмирование/Python/считывание базы данных/'  # это костыль
    path = 'tempfiles/site/db.chgk.info/tour/' + tourname + '.html'
    site = ''
    with open(path, 'r') as s:
        site = s.read()
    #
    site = site.replace("<div class='collapsible collapsed'>", '')
    site = site.replace(
        '<div class="collapse-processed"><a href="#">...</a></div>', '')
    #
    rawquestions = []
    while (site.find('<div class="question"') != -1):
        site = site[site.find('<div class="question"'):]
        site = site[:site.find("</div>")] + site[site.find("</div>")+6:]
        raw_question = site[:site.find('</div>')]
        rawquestions.append(raw_question)
    #
    return rawquestions


def finish(questions):
    with open("result.json", 'w') as res:
        res.dump(questions)
    startfile("filecleaner.py")


# getsite(input('Введите адрес страницы с вопросами (с сайта https://db.chgk.info): '))
finish(getrawquestions(getsite(
    input('Введите адрес страницы с вопросами (с сайта https://db.chgk.info): '))))
# getrawquestions('quizbr3_u')
