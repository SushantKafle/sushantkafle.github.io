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