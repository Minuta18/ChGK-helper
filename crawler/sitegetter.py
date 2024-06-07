from pywebcopy import save_webpage
from re import match


def get_site():
    siteurl = ''
    with open('tempfiles/link.txt', 'r') as linkfile:
        siteurl = linkfile.read()

    print("\033[1m\033[31m{}\033[0m".format(
        'ВНИМАНИЕ! Для корректной работы необходимо соединение с интернетом.'))

    if (match('https://db\.chgk\.info/tour/', siteurl) is None):
        print("\033[1m\033[31m{}\033[0m".format(
            'ОШИБКА! Введённая ссылка указывает на неправильный сайт!'))
        raise ValueError

    save_webpage(
        url=siteurl,
        project_folder='/богдан/програмирование/Python/' +
        'ChGK-helper/crawler/tempfiles',
        # "/богдан/програмирование/Python/" is a local path of my pc.
        # In the final version it'll be deleted
        # or changed to local path of the server
        project_name='site',
        bypass_robots=True,
        debug=True,
        open_in_browser=True,
        delay=None,
        threaded=False,
    )
