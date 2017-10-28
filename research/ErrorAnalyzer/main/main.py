from ErrorAnalyzer.CORE import ErrorAnalyzer
from ErrorAnalyzer.MODELS.Sentence import Sentence
from ErrorAnalyzer.CELEX2 import pyCelex
from ErrorAnalyzer.UTILS import G

celex = pyCelex.buildWordFormDict(G.CELEX_PATH, False)

reference = Sentence('../data/SA1.WRD', 'ldc-wrd')
hypothesis = Sentence('../data/SA1.xml', 'umarker')

errors = ErrorAnalyzer.analyze(reference, hypothesis, celex)

for error in errors:
    print (error)



