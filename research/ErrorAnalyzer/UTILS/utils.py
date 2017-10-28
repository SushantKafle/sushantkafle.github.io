from ErrorAnalyzer.CELEX2.pyCelex import WordForm, Pronunciation, MorphoLemma, SyntaxLemma

def get_word_form(celex, key):
    try:
        return celex[key]
    except KeyError:
        m_lemma = MorphoLemma([
            -1, key, -1, "moprhStatus", "lang", -1,
            "nvaffComp", "der", "comp", "derComp", "deff", "imm", "immSubCat",
            "immSA", "immAllo", "immSubst", "immOpac", "transDer", "immInfix",
            "immRevers", "flatSA", "", "strucAllo", "strucSubst", "strucOpac",
        ])

        s_lemma = SyntaxLemma([
            -1, key, -1, -1, "N", "N", "N", "N",
            "N", "N", "N", "N", "N", "N", "N",
            "N", "N", "N", "N", "N", "N",
            "N", "N", "N", "N", "N", "N",
            "N", "N", "N", "N", "N", "N",
            "N", "N", "N", "N", "N", "N",
            "N", "N", "N", "N", "N",
            "N", "N", "N",
        ])

        pronunciation = ''
        for a in key:
            pronunciation += a + '-'
        pronunciation = pronunciation[:-1]
        word_form = WordForm(None, None, s_lemma, m_lemma, None, '', '@')
        word_form.addPronunciation('P', pronunciation, '', '')

        return [word_form]
