"""
pyCelex.py: a python interface to CELEX2.
=========================================

- Author: Max
- Updated by: Sushant Kafle

Usage example
-------------

Assume you have CELEX2 installed at `/path/to/CELEX2`. This should be top directory
from the CELEX2 disc containing the `README`, and subdirectories `awk`, `c`,
`dutch`, `english`, `german`, etc.

    >>> import pyCelex
    >>> celex = pyCelex.buildWordFormDict('/path/to/CELEX2')
    >>> celex['run']
    [WordForm('run', 75882, 39588, 987, 'S', '@'),
     WordForm('run', 75883, 39589, 626, 'i', '@'),
     WordForm('run', 113816, 39589, 626, 'e1S', '@'),
     WordForm('run', 130829, 39589, 626, 'e2S', '@'),
     WordForm('run', 147739, 39589, 626, 'eP', '@'),
     WordForm('run', 158066, 39589, 626, 'pa', 'IRR')]
    >>> celex['run'][0].cob # corpus freq of first wordform
    987
    >>> dir(celex['run'][0]) # lots of other wordform properties
        ...
    >>> dir(celex['run'][0].lemma) # lemma properties
        ...

END MODULE DOC
"""
import os, csv, sys

#notInCelex = 'notInCelex.csv'
#notInCelex = '/home/morgan/bigbro/measurements/notInCelex.csv'

class Pronunciation(object):
    def __init__(self, status, disc, cv, celex):
        self.status = status
        self.disc = disc
        self.cv = cv
        self.celex = celex

    def __repr__(self):
        if self.status == 'P':
            statStr = 'Primary'
        elif self.status == 'S':
            statStr = 'Secondary'
        else:
            raise ValueError('Bad status value %r' % self.status)

        return "%s pronunciation: %s / %s / %s" % (statStr, self.disc,
                self.cv, self.celex)

    def segments(self):
        """
        Returns a list of the segments in this pronunciation, in the DISC
        transcription, which has a one-to-one correspondence between phones
        and characters. Stress and syllable boundary markers are excluded.
        """
        nonSegs = ('-', "'", '"')
        return [seg for seg in self.disc if seg not in nonSegs]

    def syllables(self):
        """
        Returns a list of the syllables in this pronunciation, each syllable
        being a string of characters in DISC transcription. Stress markers
        ("'", '"') are included.
        """
        return self.disc.split('-')
    

class WordForm(object):
    def __init__(self, orthography, wordFormID, syntaxLemma, morphoLemma, cob, flectType, transInfl):
        self.orthography = orthography
        self.wordFormID = wordFormID
        self.syntaxLemma = syntaxLemma
        self.morphoLemma = morphoLemma
        self.cob = cob
        self.pronunciations = []
        self.flectType = flectType
        self.transInfl = transInfl

        # break flectType up into individual features (cf. type2fea.awk on the
        # CELEX2 disc)
        self.sing   = 'S' in self.flectType
        self.plu    = 'P' in self.flectType
        self.pos    = 'b' in self.flectType
        self.comp   = 'c' in self.flectType
        self.sup    = 's' in self.flectType
        self.inf    = 'i' in self.flectType
        self.part   = 'p' in self.flectType
        self.pres   = 'e' in self.flectType
        self.past   = 'a' in self.flectType
        self.sin1   = '1' in self.flectType
        self.sin2   = '2' in self.flectType
        self.sin3   = '3' in self.flectType
        self.rare   = 'r' in self.flectType


    def addPronunciation(self, status, disc, cv, celex):
        self.pronunciations.append(Pronunciation(status, disc, cv, celex))

    def __str__(self):
        return "%s (wf #%d, lemma #%d)" % (self.orthography, self.wordFormID,
                self.syntaxLemma.idNum)

    def __repr__(self):
                
        return 'WordForm(%r, %d, %d, %d, %r, %r)' % (self.orthography,
                self.wordFormID, self.syntaxLemma.idNum,
                self.cob, self.flectType, self.transInfl)


    def averageNumSegments(self):
        return sum([len(p.segments()) for p in self.pronunciations]) / \
               float(len(self.pronunciations))

    def isInflected(self):
        return self.transInfl != '@'
        
    def averageNumSyllables(self):
        return sum([len(p.syllables()) for p in self.pronunciations]) / \
               float(len(self.pronunciations))

    def maxNumSegments(self):
        return max([len(p.segments()) for p in self.pronunciations])

    def maxNumSyllables(self):
        return max([len(p.syllables()) for p in self.pronunciations])

    def minNumSegments(self):
        return min([len(p.segments()) for p in self.pronunciations])

    def minNumSyllables(self):
        return min([len(p.syllables()) for p in self.pronunciations])

def buildWordFormDict(celexPath, log=False):
    if log:
        print ("Building English wordform dictionary from", os.sep.join([celexPath,
                    'english']))
        print ("Reading lemmas...")

    syntax_lemmas = loadSyntaxLemmas(celexPath)

    if log:
        print ("(%d lemmas)" % len(syntax_lemmas))
        print ("Reading syntax lemma...")

    morpho_lemmas = loadMorphoLemmas(celexPath)

    if log:
        print ("(%d lemmas)" % len(morpho_lemmas))
        print ("Reading morphology...")

    emw = loadEMW(celexPath)

    if log:
        print ("(%d wordforms)" % len(emw))
        print ("Reading phonology...")

    f = open(os.sep.join([celexPath, 'english', 'epw', 'epw.cd']), 'r')
    r = csv.reader(f, delimiter='\\', quoting=csv.QUOTE_NONE)

    d = {} # orthograph -> [WordForm instances]

    fileName=f.name

    lineno = 1
    try:
        for row in r:
            lineno += 1
            id, ortho, cob, lemmaID, pronCnt = row[:5]
            id = int(id)
            cob = int(cob)
            lemmaID = int(lemmaID)

            if ortho not in d:
                d[ortho] = []
                # in case we have a proper noun:
                if ortho != ortho.lower() and ortho.lower() not in d:
                    d[ortho.lower()] = []

            syntax_lemma = syntax_lemmas[lemmaID-1]
            morpho_lemma = morpho_lemmas[lemmaID-1]
            flectType, transInfl = emw[id]
            wf = WordForm(ortho, id, syntax_lemma, morpho_lemma, cob, flectType, transInfl)

            i = 5
            while i < len(row):
                status = row[i]
                disc = row[i+1]
                cv = row[i+2]
                celex = row[i+3]
                wf.addPronunciation(status, disc, cv, celex)
                i += 4

            d[ortho].append(wf)
            if ortho != ortho.lower():
                d[ortho.lower()].append(wf)
                            
    except (csv.Error, e):
        print ('CSV error in %s at line %d' % (fileName,lineno))
        raise e

    if log:
        print ("(%d orthographies)" % len(d))
    return d

def boolYN(s):
    if s == "Y":
        return True
    elif s == "N":
        return False
    else: 
        raise ValueError("String must be 'Y' or 'N'. Got %r." % s)

# Lemma class numbers
LEMMA_CLASS_NOUN            = 1
LEMMA_CLASS_ADJECTIVE       = 2
LEMMA_CLASS_NUMERAL         = 3
LEMMA_CLASS_VERB            = 4
LEMMA_CLASS_ARTICLE         = 5
LEMMA_CLASS_PRONOUN         = 6
LEMMA_CLASS_ADVERB          = 7
LEMMA_CLASS_PREPOSITION     = 8
LEMMA_CLASS_CONJUNCTION     = 9
LEMMA_CLASS_INTERJECTION    = 10
LEMMA_CLASS_SGCONTRACTION   = 11
LEMMA_CLASS_CXCONTRACTION   = 12

class SyntaxLemma(object):
    fieldNames = [
        "idNum", "head", "cob", "classNum", "c_N", "unc_N", "sing_N", "plu_N",
        "grC_N", "grUnc_N", "attr_N", "postPos_N", "voc_N", "proper_N", "exp_N",
        "trans_V", "transComp_V", "intrans_V", "ditrans_V", "link_V", "phr_V",
        "prep_V", "phrPrep_V", "exp_V", "ord_A", "attr_A", "pred_A",
        "postPos_A", "exp_A", "ord_ADV", "pred_ADV", "postPos_ADV", "comb_ADV",
        "exp_ADV", "card_NUM", "ord_NUM", "exp_NUM", "pers_PRON", "dem_PRON",
        "poss_PRON", "refl_PRON", "wh_PRON", "det_PRON", "pron_PRON",
        "exp_PRON", "cor_C", "sub_C",
    ]

    fieldTypes = {
        "idNum": int,
        "cob": int,
        "head": str,
        "classNum": int,
    }

    def __init__(self, row):
        for fieldNum, fieldValue in enumerate(row):
            fieldName = self.fieldNames[fieldNum]
            if fieldName in self.fieldTypes:
                fieldValue = self.fieldTypes[fieldName](fieldValue)
            else:
                fieldValue = boolYN(fieldValue)

            setattr(self, fieldName, fieldValue)

    def __getitem__(self, key):
        return getattr(self, key)

    def __repr__(self):
        return 'Lemma(%d, %r, %d, %d, ...)' % (self.idNum, self.head, self.cob,
                self.classNum)


class MorphoLemma(object):
    fieldNames = [
        "idNum", "head", "cob", "moprhStatus", "lang", "morphCnt",
        "nvaffComp", "der", "comp", "derComp", "deff", "imm", "immSubCat",
        "immSA", "immAllo", "immSubst", "immOpac", "transDer", "immInfix",
        "immRevers", "flatSA", "strucLab", "strucAllo", "strucSubst", "strucOpac",
    ]

    fieldTypes = {
        "idNum": int,
        "cob": int,
        "morphCnt": int
    }

    def __init__(self, row):
        for fieldNum, fieldValue in enumerate(row):
            if fieldNum > 24:
                break
            fieldName = self.fieldNames[fieldNum]
            if fieldName in self.fieldTypes:
                fieldValue = self.fieldTypes[fieldName](fieldValue)
            else:
                fieldValue = str(fieldValue)

            setattr(self, fieldName, fieldValue)

    def __getitem__(self, key):
        return getattr(self, key)

    def __repr__(self):
        return 'MorphoLemma(%d, %r, %d, %r ...)' % (self.idNum, self.head, self.cob, self.deff)

def loadSyntaxLemmas(celexPath):
    f = open(os.sep.join([celexPath, 'english', 'esl', 'esl.cd']), 'r')
    r = csv.reader(f, delimiter='\\', quoting=csv.QUOTE_NONE)

    fileName=f.name
    lemmas = []

    lineno = 1
    try:
        for row in r:
            lineno += 1
            lemmas.append(SyntaxLemma(row))

    except (csv.Error, e):
        print ('CSV error in %s at line %d' % (fileName,lineno))
        raise e

    return lemmas

def loadMorphoLemmas(celexPath):
    f = open(os.sep.join([celexPath, 'english', 'eml', 'eml.cd']), 'r')
    r = csv.reader(f, delimiter='\\', quoting=csv.QUOTE_NONE)

    fileName=f.name
    lemmas = []

    lineno = 1
    try:
        for row in r:
            lineno += 1
            lemmas.append(MorphoLemma(row))

    except (csv.Error, e):
        print ('CSV error in %s at line %d' % (fileName,lineno))
        raise e

    return lemmas

def loadEMW(celexPath):
    f = open(os.sep.join([celexPath, 'english', 'emw', 'emw.cd']), 'r')
    r = csv.reader(f, delimiter='\\', quoting=csv.QUOTE_NONE)

    fileName=f.name
    emw = {}

    lineno = 1
    try:
        for row in r:
            lineno += 1
            id, orhto, cob, idLemma, flectType, transInfl = row
            emw[int(id)] = (flectType, transInfl)

    except (csv.Error, e):
        print ('CSV error in %s at line %d' % (fileName,lineno))
        raise e

    return emw

