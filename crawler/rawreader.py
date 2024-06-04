from os import chdir
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
ps = bs.BeautifulSoup(site, 'html.parser')  # parsed site
rawquestions = [str(i) for i in ps.select("div.question")]
#
rawres = open("tempfiles/result/raw_result.json", 'bw')
rawres.write('#elementend#'.join(rawquestions).encode())
rawres.close()
