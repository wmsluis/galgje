#!/usr/bin/python3

import galgje
import re
import os
import argparse

parser = argparse.ArgumentParser(description="Start Galgje")
parser.add_argument("-p", "--pogingen",
        type = int,
        default = 5,
        help = "Maximaal aantal pogingen")

args = parser.parse_args()

dn = os.path.dirname(os.path.realpath(__file__))
fn = os.path.join(dn, 'woorden.txt' )

with open(fn, mode='r', encoding='utf8') as f:
    tekst = f.read()

woordenlijst = re.findall('\\b[a-zA-Z]+\\b', tekst)

spel = galgje.Galgje(woordenlijst)
spel.speel(args.pogingen)

 
