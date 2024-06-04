from pywebcopy import save_webpage
import validators
from os import startfile, getcwd, chdir

chdir("crawler")
siteurl = ''
with open('tempfiles/link.txt', 'r') as l:
    siteurl = l.read()

print("\033[1m\033[31m{}\033[0m".format(
    'ВНИМАНИЕ! Для корректной работы необходимо соединение с интернетом.'))

if (siteurl[:len('https://db.chgk.info/tour/')] != 'https://db.chgk.info/tour/'):
    print("\033[1m\033[31m{}\033[0m".format(
        'ОШИБКА! Введённая ссылка указывает на неправильный сайт!'))
    raise ValueError

save_webpage(
    url=siteurl,
    project_folder='/богдан/програмирование/Python/' + 'ChGK-helper/crawler/tempfiles',
    # "/богдан/програмирование/Python/" is a local path of my pc. In the final version it'll be deleted or changed to local path of server
    project_name='site',
    bypass_robots=True,
    debug=True,
    open_in_browser=True,
    delay=None,
    threaded=False,
)
