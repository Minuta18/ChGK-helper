from json import dump
from os import startfile, getcwd, chdir
import soupsieve as bs  # beautiful soup 4
chdir("crawler")

# kostyl_dlya_VScode = 'програмирование/Python/считывание базы данных/'  # это костыль
tourname = 'dsgsdg'
with open('tempfiles/link.txt', 'r') as l:
    l2 = l.read()
    tourname = l2[len('https://db.chgk.info/tour/'):]
path = 'tempfiles/site/db.chgk.info/tour/' + tourname + '.html'
site = ''
with open(path, 'r') as s:
    site = s.read()
#
rawquestions = []
#


with open("result.json", 'w') as res:
    res.dump(rawquestions)
startfile("filecleaner.py")
