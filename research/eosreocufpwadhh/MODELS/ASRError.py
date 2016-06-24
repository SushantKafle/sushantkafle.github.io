class ASRError:
    def __init__(self, reference, hypothesis, type):
        self.error_type = type
        self.reference = reference
        self.hypothesis = hypothesis

    def unique(self, test):
        buff = []
        for t in test:
            if t not in buff:
                buff.append(t)
        return buff

    def get_reference_word_list(self):
        if type(self.reference) is list:
            return self.unique(self.reference)
        else:
            return [self.reference]

    def set_reference_words(self, ref_list):
        self.reference = ref_list

    def get_hypothesis_word_list(self):
        if type(self.hypothesis) is list:
            return self.unique(self.hypothesis)
        else:
            return [self.hypothesis]

    def set_hypothesis_words(self, hyp_list):
        self.hypothesis = hyp_list

    def get_error_type(self):
        return self.error_type

    def set_error_type(self, type):
        self.error_type = type


    def __str__(self):
        from UTILS import G
        ref_str = "Reference: "
        hyp_str = "Hypothesis: "
        for reference in self.get_reference_word_list():
            ref_str += str(reference) + " "
        for hypothesis in self.get_hypothesis_word_list():
            hyp_str += str(hypothesis) + " "

        return ref_str + " " + hyp_str + "Error Type: " + G.factor_get_error_type(self.error_type)