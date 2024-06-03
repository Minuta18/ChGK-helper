from os import chdir, mkdir
chdir("crawler")
mkdir("tempfiles")
chdir("tempfiles")
mkdir("result")
chdir("result")
open('raw_result.json', 'w').close()
chdir('..')
open('link.txt', 'w').close()
