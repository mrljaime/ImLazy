# --*-- encoding: utf-8 --*--

import argparse 

parser = argparse.ArgumentParser(description="Allow read user input")
parser.add_argument("-d", dest="directory", required=True)

args = parser.parse_args()
