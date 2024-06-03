from os import startfile, getcwd, chdir
from json import dump
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


with open("result.json", 'w') as res:
    res.dump(rawquestions)
startfile("filecleaner.py")
