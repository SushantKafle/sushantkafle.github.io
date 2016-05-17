from Word import Word
from nltk import word_tokenize
import string

class Sentence:
    def __init__(self, path, source = 'text'):
        self.words = []
        if source == 'umarker': #xml from uncertaintymaker code
            import untangle
            template = untangle.parse(path)
            for word in template.transcription.words:
                if not word.word.cdata in ["[sil]", "[NOISE]", "[SPEECH]"]:
                    self.words.append(Word(word.word.cdata, word.timeStart.cdata, word.timeEnd.cdata))

        elif source == 'ldc-wrd':
            wrd_file = open(path, 'r')
            for line in wrd_file:
                elements = line.split(' ')
                word = elements[2].rstrip()
                time_from = self.convert_time(elements[0], from_time='ldc', to_time='ms')
                time_to = self.convert_time(elements[1], from_time='ldc', to_time='ms')
                self.words.append(Word(word, time_from, time_to))
            wrd_file.close()
        elif source == 'text':
            path = path.encode('ascii', 'ignore')
            for word in word_tokenize(path):
                if not word in ['"', "'", ".", "!", '``', '`', "''", '""']:
                    self.words.append(Word(word, '', ''))


    def __str__(self):
        str_sentence = "( Sentence: "
        for word in self.words:
            str_sentence += word.word + " (" + str(word.POS) + ") "
        return str_sentence + " )"

    def __len__(self):
        return len(self.words)

    def __getitem__(self, item):
        return self.words[item]

    def convert_time(self, time, from_time, to_time):
        time = int(time)
        if from_time == 'ldc' and to_time == 'ms':
            time = time/16.
        else:
            print 'Format not supported!'
        return str(time)



