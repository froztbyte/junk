#!/usr/bin/python
"""
facebook contact export clobber script

this is hellabad. it assumes names and email addresses are present, nothing
more than that. then it clobbers things.

code by froztbyte, MIT License 2012
"""
import argparse
from os import getcwd

# because fuck manual arg parsing forever
parser = argparse.ArgumentParser(
    description="pop out a nicer format for fb export data")
parser.add_argument('--input', help='input file', type=None, required=False)
parser.add_argument('--output', help='output file', type=None, required=False)

args = parser.parse_args()

# loads appropriate var paths, assumes files in cwd by default
if args.input is None:
    INPUT = getcwd() + '/fb.txt'
else:
    INPUT = args.input
if args.input is None:
    OUTPUT = getcwd() + '/output.txt'
else:
    OUTPUT = args.output

#read the file, drop it in a list
initList = open(INPUT, 'r')


def stripsearch(input):
    """ utility function time! """
    temp = input.strip()
    if temp != '':
        return temp

#the real work
#we make the assumption that we're keeping list order all the way through
strippedBlanks = filter(stripsearch, initList)
for idx, item in enumerate(strippedBlanks):
    strippedBlanks[idx] = item.strip()

# yes, that just happened.
# this code is on github, after all.

names = {}
for item in strippedBlanks:
    if '@' not in item:
        name = item
        names[name] = []
    else:
        names[name].append(item)

csvLines = []
for name, addresses in names.iteritems():
    for address in addresses:
        linestruct = "%(name)s,%(address)s" % {
            'name': name,
            'address': address}
        csvLines.append(linestruct + '\n')

outfile = open(OUTPUT, 'w')
outfile.writelines(csvLines)
outfile.close()
