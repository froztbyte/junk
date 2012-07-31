#!/usr/bin/python
import argparse
from os import getcwd

""" because fuck manual arg parsing forever """
parser = argparse.ArgumentParser(description="pop out a nicer format for fb export data")
parser.add_argument('--input', help='input file', type=None, required=False)
parser.add_argument('--output', help='output file', type=None, required=False)

args = parser.parse_args()

""" loads appropriate var paths, assumes files in cwd by default """
if args.input is not None:
    INPUT = args.input
else:
    INPUT = getcwd() + '/fb.txt'
if args.input is not None:
    OUTPUT = args.output
else:
    OUTPUT = getcwd() + '/output.txt'

""" read the file, drop it in a list """
initList = open(INPUT, 'r').readlines()


def stripsearch(input):
    """ utility function time! """
    temp = input.strip()
    if temp != '':
        return temp

""" the real work """
""" we make the assumption that we're keeping list order all the way through """
strippedBlanks = filter(stripsearch, initList)
for idx, item in enumerate(strippedBlanks):
    strippedBlanks[idx] = item.strip()

names = {}
for idx, item in enumerate(strippedBlanks):
    if '@' not in item:
        name = item
        names[name] = []
    else:
        names[name].append(item)

csvLines = []
for item in names:
    for address in names[item]:
        linestruct = "%(name)s,%(surname)s,%(address)s" % {
            'name': item.split(' ')[0],
            'surname': item.split(' ', 1)[1],
            'address': address}
        csvLines.append(linestruct + '\n')

outfile = open(OUTPUT, 'w')
outfile.writelines(csvLines)
outfile.close()
