#!/usr/local/bin/python3
from classes.character import Character
import random

characternames = ["Frasier", "Niles", "Roz"]
lines = 10

characters = []
for c in characternames:
    characters.append(Character(c,"transcripts/parsed_by_character/"+c+".txt",1))

prevC = c = 0 
prevLine = line = None

for i in range(0,lines):
    # Choose a new respondent
    while c == prevC: 
        c = random.randint(0,len(characternames)-1)

    # Generate line
    while line==None:
        # First sentence
        if prevLine==None:
            line = characters[c].say()
        # Else, potentially say something new
        elif random.random() < 0.3:
            line = characters[c].say()
        # Else, respond to the previous line
        else:
            line = characters[c].respond(prevLine)

    # Print line
    lineFormat = "%8s: %s" % (characters[c].Name(), line)
    print(lineFormat)

    # Keep track of who spoke last
    prevC = c
    prevLine = line
    line = None
