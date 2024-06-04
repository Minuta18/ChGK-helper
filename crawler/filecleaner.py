from os import chdir, replace
from shutil import rmtree
chdir("crawler")
replace("tempfiles/result/result.json", "result.json")
rmtree("tempfiles")
# remove("tempfiles")
