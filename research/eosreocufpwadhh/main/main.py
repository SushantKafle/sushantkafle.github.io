from CORE import ErrorAnalyzer
from MODELS.Sentence import Sentence
from CELEX2 import pyCelex
from UTILS import G

celex = pyCelex.buildWordFormDict(G.CELEX_PATH, False)

reference = Sentence('../data/SA1.WRD', 'ldc-wrd')
hypothesis = Sentence('../data/SA1.xml', 'umarker')

errors = ErrorAnalyzer.analyze(reference, hypothesis, celex)

for error in errors:
    print error



