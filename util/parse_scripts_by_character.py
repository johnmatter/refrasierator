#!/usr/local/bin/python3
from preprocess import get_character_lines

import re

transcriptsDir = "transcripts/raw/"
parsedDir = "transcripts/parsed_by_character/"

seasons = range(1,12)
episodes = range(1,25)

characters = ["Frasier", "Niles", "Martin", "Daphne", "Roz", "Bulldog"]

for c in characters:
    print("Parsing " + c)
    filename = parsedDir + c + ".txt"
    f = open(filename, "w")

    charRegex=r'\W*' + c +':\W*'
    for s in seasons:
        print(".",end="")
        for e in episodes:
            episode = "s%02de%02d.txt" % (s,e)
            script = transcriptsDir + episode
            lines = get_character_lines(c,script)
            for l in lines:
                # Remove e.g. "  Niles: " from beginning of line
                line = re.sub(charRegex, '', l)
                if line=="":
                    continue
                if line[-1] != '\n':
                    line += ('\n')
                f.write(line)
    f.close()
    print()
