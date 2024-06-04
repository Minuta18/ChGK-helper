from json import dump
from os import startfile, getcwd, chdir
import bs4 as bs  # beautiful soup 4
chdir("crawler")

tourname = ''
with open('tempfiles/link.txt', 'r') as l:
    l2 = l.read()
    tourname = l2[len('https://db.chgk.info/tour/'):]
path = 'tempfiles/site/db.chgk.info/tour/' + tourname + '.html'
site = ''
with open(path, 'r') as s:
    site = s.read()
#
rawquestions = bs.BeautifulSoup(site, 'html.parser').select("div.question")
#
with open("raw_result.json", 'w') as rawres:
    dump(rawres, rawquestions)
