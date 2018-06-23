#!/usr/local/bin/python3
import re

def get_character_lines(character, script):
    characterRegex = r'^\W*'+character+':.*$'

    with open(script) as f:
        text = f.readlines()

    # Strip newlines and trailing whitespace
    text = [re.sub(r'\ *\n*$', '', line) for line in text]

    thisCharacterLines = []
    prevLineContinues = False

    # Loop over lines and find character's.
    # If it starts with e.g. "   Niles: " it's the beginning of a line.
    # Note that a \n doesn't mean the end of a line of dialogue! Some
    # dialogue continues on the next line (much like this comment!)
    for i in range(len(text)-1):
        line = ' ' + text[i]
        nextline = ' ' + text[i+1]

        # Continuing a line--------------------------------------------
        if prevLineContinues==True:
            # Is this line blank or a new character? Then we're done.
            if (line==' ' or bool(re.match(r'^\W*\w+:.*$',line))):
                prevLineContinues = False
                continue
            # Is next line is blank or a new character? Then we're done after this one.
            elif (nextline==' ' or bool(re.match(r'^\W*\w+:.*$',nextline))):
                thisCharacterLines[-1] += line
                prevLineContinues = False
                continue
            # Otherwise it's *probably* continued dialogue. 
            else:
                thisCharacterLines[-1] += line
                prevLineContinues = True
                continue

        # Starting a new line--------------------------------------------
        # If line matches this character
        if bool(re.match(characterRegex,line)):
            thisCharacterLines.append(line)
            prevLineContinues = True

                  
    # Remove excess spaces
    thisCharacterLines = [re.sub(r'\ +',' ',line) for line in thisCharacterLines]
    thisCharacterLines = [line.lstrip(' ') for line in thisCharacterLines]

    # Remove stage directions
    thisCharacterLines = [re.sub(r'\[[^\]]*\]','',line) for line in thisCharacterLines]

    return thisCharacterLines

