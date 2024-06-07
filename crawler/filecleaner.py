from os import replace
from shutil import rmtree


def clean_tempfiles():
    replace("tempfiles/result/result.json", "result.json")
    rmtree("tempfiles")
