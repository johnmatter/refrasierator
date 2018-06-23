import markovify
from random import choice
from nltk.corpus import stopwords

class Character(object):
    def __init__(self, name, corpus, verbosity):
        self.name = name
        self.verbosity = verbosity # not used yet

        # Define Markov brain
        self.corpus = corpus # location of text corpus
        with open(corpus) as f:
            text = f.read()
        self.brain = markovify.Text(text, state_size=3)

        # Words that are blocked from respond()
        self.blockwords = set(stopwords.words('english')) 

    def say(self):
        return self.brain.make_sentence(max_overlap_ratio=0.5, max_overlap_total=10)

    def respond(self, line):
        line = line.lower()
        tokens = line.split()

        # Remove stop words (a, an, the, etc)
        cleanTokens = []
        for t in tokens:
            if t not in self.blockwords:
                cleanTokens.append(t)

        # Choose a seed from the remaining words
        seed = choice(cleanTokens).title()
        return self.brain.make_sentence_with_start(seed, strict=False, tries=50, max_overlap_ratio=0.5, max_overlap_total=10)

    def Name(self):
        return self.name
