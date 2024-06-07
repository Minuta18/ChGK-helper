from filemaker import make_tempfiles
from filecleaner import clean_tempfiles
from rawfile_editor import seprawquestions
from rawreader import getrawquestions
from sitegetter import get_site
from shutil import rmtree
from os import chdir, getcwd
#
print(getcwd())
chdir("crawler")
make_tempfiles()
with open('tempfiles/link.txt', 'w') as link_file:
    link = input(
        'Введите адрес страницы с вопросами (с сайта https://db.chgk.info): ')
    link_file.write(link)
get_site()
getrawquestions()
seprawquestions()
clean_tempfiles()

rmtree("__pycache__")
