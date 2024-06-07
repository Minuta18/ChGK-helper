from os import chdir, mkdir


def make_tempfiles():
    mkdir("tempfiles")
    chdir("tempfiles")
    mkdir("result")
    chdir("result")
    open('raw_result.txt', 'w').close()
    open('result.json', 'w').close()
    chdir('..')
    open('link.txt', 'w').close()
    chdir('..')
