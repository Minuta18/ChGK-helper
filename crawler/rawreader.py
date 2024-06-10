import bs4 as bs  # beautiful soup 4


def getrawquestions():
    tourname = ''
    with open('tempfiles/link.txt', 'r') as lnk_file:
        lnk = lnk_file.read()
        tourname = lnk[len('https://db.chgk.info/tour/'):]
    path = 'tempfiles/site/db.chgk.info/tour/' + tourname + '.html'
    site = ''
    with open(path, 'r') as s:
        site = s.read()
    #
    ps = bs.BeautifulSoup(site, 'html.parser')  # parsed site
    rawquestions = [str(i) for i in ps.select("div.question")]
    #
    with open("tempfiles/result/raw_result.txt", 'bw') as rawres:
        rawres.write('#elementend#'.join(rawquestions).encode())