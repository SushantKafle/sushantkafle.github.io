from UTILS import G

class Word:
    def __init__(self, word, time_start, time_end):
        self.word = word
        self.time_start = time_start
        self.time_end = time_end
        self.POS = G.POS_TAGS["TBD"]

    def get_word(self):
        return self.word

    def get_time_interval(self):
        return [self.time_start, self.time_end]

    def set_POS(self, tag):
        self.POS = tag


    def __str__(self):
        if self.POS != G.POS_TAGS["TBD"]:
            return "( WORD: " + self.time_start + " " + self.word + " ( " + str(self.POS) + " ) " + self.time_end + " )"
        return "( WORD: " + self.time_start + " " + self.word + " " + self.time_end + " )"

    def __len__(self):
        return len(self.word)