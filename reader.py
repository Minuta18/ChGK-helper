from pywebcopy import save_webpage
import validators


def getsite():
    print("\033[1m\033[31m{}\033[0m".format(
        'ВНИМАНИЕ! Для корректной работы необходимо соединение с интернетом.'))
    siteurl = input(
        'Введите адрес страницы с вопросами (с сайта https://db.chgk.info): ')
    if (siteurl[:len('https://db.chgk.info/tour/')] != 'https://db.chgk.info/tour/'):
        print("\033[1m\033[31m{}\033[0m".format(
            'ОШИБКА! Введённая ссылка указывает на неправильный сайт!'))
        return -1
    save_webpage(
        url=siteurl,
        project_folder='/богдан/програмирование/Python/считывание базы данных/tempfiles',
        project_name='site',
        bypass_robots=True,
        debug=True,
        open_in_browser=True,
        delay=None,
        threaded=False,
    )
    return siteurl[len('https://db.chgk.info/tour/'):]


def getquestions(tourname):
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
    while (site.find('<div class="question"') != -1)
    site = site[site.find('<div class="question"'):]
    site = site[:site.find("</div>")] + site[te.find("</div>")+6:]
    raw_question = site[:site.find('</div>')]


# getquestions(getsite())
getquestions('quizbr3_u')
