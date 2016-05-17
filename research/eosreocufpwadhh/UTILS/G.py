CELEX_PATH_LAB = '/Users/sxk5664/Documents/RIT/Research/Data/LDC-Data/CELEX2/celex2'
CELEX_PATH_LAP = '/Users/sushantkafle/Documents/Study/RIT/Research/Data/LDC-Data/celex2'
CELEX_PATH = CELEX_PATH_LAB

WORD_TYPE = {
    'FUNCTION' : 1,
    'CONTENT': 0
}

LIST_OF_FUNCTION_POS = ["MD", "CC", "DT", "IN", "PRP", "PRP$", "CD", "CC", "DT", "WDT", "UH", "MD", "PDT", "POS", "RP",
                        "TO", "EX", "FW", "SYM", "LS",
                        "WP", "WP$"]

ERROR_CODE = {
    'NO ERROR' : -1,
    'SUBSTITUTION' : 0,
    'ONE TO MANY': 1,
    'MANY TO ONE': 2,
    'ONE TO ONE' : -2,
    'INFLECTION' : 3,
    'DERIVATIONAL' : 4,
    'PHONE NEIGHBOUR' : 5,
    'OTHERS' : 6,
    'INSERTION' : 7,
    'DELETION' : 8,
    'CHAIN' : 9,
    'TBD' : 10,
}

THRESHOLD = 50

def factor_get_error_type(index):
    names = {
        0: 'NOERROR',
        1: 'ONETOMANY',
        2: 'MANYTOONE',
        3: 'INFLECTION',
        4: 'DERIVATIONAL',
        5: 'PHONENEIGHBOUR',
        6: 'OTHERS',
        7: 'INSERTION',
        8: 'DELETION',
        9: 'CHAIN',
        -1: 'TBD'
    }

    if type(index) is int:
        return names[index]
    else:
        return names[int(index)]



POS_TAGS = {
    "NN" : 1, #NOUN
    "NNS" : 1, #NOUN
    "NNP" : 1, #NOUN
    "NNPS" : 1, #NOUN

    "VB" : 2, #VERB
    "VBD" : 2, #VERB
    "VBG" : 2, #VERB
    "VBN" : 2, #VERB
    "VBP" : 2, #VERB
    "VBZ" : 2, #VERB

    "PRP" : 3, #PRONOUN
    "PRP$" : 3, #PRONOUN
    "WP": 3,  # PRONOUN
    "WP$": 3,  # PRONOUN

    "RB" : 4, #ADV
    "RBR" : 4, #ADV
    "RBS" : 4, #ADV
    "WRB" : 4, #ADV

    "JJ" : 5, #ADJ
    "JJR" : 5, #ADJ
    "JJS" : 5, #ADJ

    "IN" : 6, #PREP

    "CC" : 7, #CONJUNCTION

    "UH" : 8, #INTERJECTION

    "DT" : 9, #DET
    "WDT" : 9, #DET

    "CD" : 10, #NUM

    "MD" : 11, #MODAL (could, will)

    "PDT" : 11, #PREDETERMINER

    "POS" : 11, #POSSESIVE ENDING

    "RP" : 11, #PARTICLE

    "TO" : 11, #TO

    "EX" : 11, #EXISTENTIAL THERE

    "FW" : 11, #FOREIGN WORD

    "SYM" : 11, #SYM

    "LS" : 11, #LIST MARKER

    "TBD" : -1
}
