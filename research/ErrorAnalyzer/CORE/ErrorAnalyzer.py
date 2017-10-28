from ErrorAnalyzer.MODELS.ASRError import ASRError
from ErrorAnalyzer.MODELS.Word import Word
from ErrorAnalyzer.UTILS import G, utils
import re
import difflib

def is_phone_neighbour(ref_word_form, hyp_word_form):
    ref_prcs = ref_word_form.pronunciations
    hyp_prcs = hyp_word_form.pronunciations
    max_score = 0
    for ref_prc in ref_prcs:
        for hyp_prc in hyp_prcs:
            score = difflib.SequenceMatcher(None, ref_prc.disc, hyp_prc.disc).ratio()
            if score > max_score:
                max_score = score

    return max_score >= 0.6

def get_root_word(structure):
    #structure looks like this: (((im)[A|.A],(mature)[A])[A],(ly)[B|A.])[B]
    patterns = re.findall('\([a-z]*\)', structure)
    root = '' #word with max length
    for pattern in patterns:
        word = pattern[1:-1]
        if len(word) > len(root):
            root = word
    return root

def is_equal(time_1, time_2):
    time_1 = [float(time_1[0]), float(time_1[1])]
    time_2 = [float(time_2[0]), float(time_2[1])]
    if abs(time_1[0] - time_2[0]) <= G.THRESHOLD:
        if abs(time_1[1] - time_2[1]) <= G.THRESHOLD:
            return True
    return False

def is_disjoint(time_1, time_2):
    time_1 = [float(time_1[0]), float(time_1[1])]
    time_2 = [float(time_2[0]), float(time_2[1])]
    if (((time_2[0] >= time_1[1]) or ((time_1[1] - time_2[0]) < G.THRESHOLD))
        or ((time_1[0] >= time_2[1]) or ((time_2[1] - time_1[0]) < G.THRESHOLD))):
        return True
    return False

def contains(time_1, time_2):
    time_1 = [float(time_1[0]), float(time_1[1])]
    time_2 = [float(time_2[0]), float(time_2[1])]
    if ((time_1[0] - time_2[0]) <= G.THRESHOLD) or (time_2[0] > time_1[0]):
        if ((time_2[1] - time_1[1]) <= G.THRESHOLD) or (time_1[1] > time_2[1]):
            return True
    return False

def postprocessing_one_to_one_errors(errors, celex):
    for error in errors:
        if error.get_error_type() == G.ERROR_CODE['ONE TO ONE']:
            ref_word = error.get_reference_word_list()[0].word
            hyp_word = error.get_hypothesis_word_list()[0].word
            ref_word_form = utils.get_word_form(celex, ref_word)[0]
            if len(ref_word_form.morphoLemma.strucLab) != 0:
                ref_structure = ref_word_form.morphoLemma.strucLab
                ref_root = get_root_word(ref_structure)
            else:
                ref_root = ref_word_form.morphoLemma.head

            hyp_word_form = utils.get_word_form(celex, hyp_word)[0]
            if len(hyp_word_form.morphoLemma.strucLab) != 0:
                hyp_structure = hyp_word_form.morphoLemma.strucLab
                hyp_root = get_root_word(hyp_structure)
            else:
                hyp_root = hyp_word_form.morphoLemma.head

            #print hyp_word_form, ref_word_form
            if ref_root == hyp_root:
                #check if inflection or derivational
                if hyp_word_form.isInflected() or ref_word_form.isInflected():
                    error.set_error_type(G.ERROR_CODE['INFLECTION'])
                else:
                    error.set_error_type(G.ERROR_CODE['DERIVATIONAL'])
            elif is_phone_neighbour(ref_word_form, hyp_word_form):
                error.set_error_type(G.ERROR_CODE['PHONE NEIGHBOUR'])
            else:
                error.set_error_type(G.ERROR_CODE['OTHERS'])

    return errors

def analyze(reference, hypothesis, celex):
    errors = [] #list of errors
    r_id, h_id = 0, 0
    buffer = None
    type = None
    while (True):
        if r_id < len(reference) and h_id < len(hypothesis):
            if reference[r_id].word == hypothesis[h_id].word:

                if buffer:
                    if len(buffer.get_hypothesis_word_list()) == 1 and len(
                            buffer.get_reference_word_list()) == 1:  # ONE TO ONE
                        buffer.set_error_type(G.ERROR_CODE['ONE TO ONE'])
                        errors.append(buffer)
                        h_id += 1
                        r_id += 1
                    else:
                        if type == G.ERROR_CODE['CHAIN']:
                            if len(buffer.get_hypothesis_word_list()) == 1:
                                type = G.ERROR_CODE['MANY TO ONE']
                            elif len(buffer.get_reference_word_list()) == 1:
                                type = G.ERROR_CODE['ONE TO MANY']
                        buffer.set_error_type(type)
                        errors.append(buffer)
                        buffer, type = None, None

                r_id += 1
                h_id += 1
                continue



        if r_id >= len(reference):
            if h_id >= len(hypothesis):
                if buffer:
                    buffer.set_error_type(type)
                    errors.append(buffer)
                break
            else:
                if buffer:
                    if len(buffer.get_hypothesis_word_list()) == 1 and len(
                            buffer.get_reference_word_list()) == 1:  # ONE TO ONE
                        buffer.set_error_type(G.ERROR_CODE['ONE TO ONE'])
                        errors.append(buffer)
                        h_id += 1
                        r_id += 1
                    else:
                        if type == G.ERROR_CODE['CHAIN']:
                            if len(buffer.get_hypothesis_word_list()) == 1:
                                type = G.ERROR_CODE['MANY TO ONE']
                            elif len(buffer.get_reference_word_list()) == 1:
                                type = G.ERROR_CODE['ONE TO MANY']
                        buffer.set_error_type(type)
                        errors.append(buffer)
                        h_id += 1
                        r_id += 1

                # all hyp_words are insertions
                for idx in range(h_id, len(hypothesis)):
                    new_error = ASRError(Word('', '', ''), hypothesis[idx], G.ERROR_CODE['INSERTION'])
                    errors.append(new_error)

                break
        else:
            if h_id >= len(hypothesis):

                if buffer:
                    if len(buffer.get_hypothesis_word_list()) == 1 and len(
                            buffer.get_reference_word_list()) == 1:  # ONE TO ONE
                        buffer.set_error_type(G.ERROR_CODE['ONE TO ONE'])
                        errors.append(buffer)
                        h_id += 1
                        r_id += 1
                    else:
                        if type == G.ERROR_CODE['CHAIN']:
                            if len(buffer.get_hypothesis_word_list()) == 1:
                                type = G.ERROR_CODE['MANY TO ONE']
                            elif len(buffer.get_reference_word_list()) == 1:
                                type = G.ERROR_CODE['ONE TO MANY']
                        buffer.set_error_type(type)
                        errors.append(buffer)
                        h_id += 1
                        r_id += 1

                for idx in range(r_id, len(reference)):
                    new_error = ASRError(reference[idx], Word('', '', ''), G.ERROR_CODE['DELETION'])
                    errors.append(new_error)

                break

        ref_word = reference[r_id]
        hyp_word = hypothesis[h_id]
        if is_equal(ref_word.get_time_interval(), hyp_word.get_time_interval()):
            if buffer:
                buffer.set_error_type(type)
                if type == G.ERROR_CODE['ONE TO MANY']:
                    prev_hyp_words = buffer.get_hypothesis_word_list()
                    prev_hyp_words.append(hyp_word)
                    buffer.set_hypothesis_words(prev_hyp_words)
                elif type == G.ERROR_CODE['MANY TO ONE']:
                    prev_ref_words = buffer.get_reference_word_list()
                    prev_ref_words.append(ref_word)
                    buffer.set_reference_words(prev_ref_words)
                elif type == G.ERROR_CODE['CHAIN']:
                    pass

                errors.append(buffer)
                buffer, type = None, None
                r_id += 1
                h_id += 1
                continue

            new_error = ASRError(ref_word, hyp_word, G.ERROR_CODE['ONE TO ONE'])
            errors.append(new_error)
            r_id += 1
            h_id += 1

        elif is_disjoint(ref_word.get_time_interval(), hyp_word.get_time_interval()):
            if buffer:
                if len(buffer.get_hypothesis_word_list()) == 1 and len(
                        buffer.get_reference_word_list()) == 1:  # ONE TO ONE
                    buffer.set_error_type(G.ERROR_CODE['ONE TO ONE'])
                    errors.append(buffer)
                    buffer, type = None, None
                else:
                    if type == G.ERROR_CODE['CHAIN']:
                        if len(buffer.get_hypothesis_word_list()) == 1:
                            type = G.ERROR_CODE['MANY TO ONE']
                        elif len(buffer.get_reference_word_list()) == 1:
                            type = G.ERROR_CODE['ONE TO MANY']
                    buffer.set_error_type(type)
                    errors.append(buffer)
                    buffer, type = None, None
            else:
                if float(ref_word.get_time_interval()[0]) > float(hyp_word.get_time_interval()[0]):
                    new_error = ASRError(ref_word, hyp_word, G.ERROR_CODE['INSERTION'])
                else:
                    new_error = ASRError(ref_word, hyp_word, G.ERROR_CODE['DELETION'])
                errors.append(new_error)

            if float(ref_word.get_time_interval()[0]) > float(hyp_word.get_time_interval()[0]):
                h_id += 1
            else:
                r_id += 1

        elif contains(ref_word.get_time_interval(), hyp_word.get_time_interval()):
            if not buffer:
                buffer = ASRError(ref_word, hyp_word, None)
                type = G.ERROR_CODE['ONE TO MANY']
            else:
                prev_hyp_words = buffer.get_hypothesis_word_list()
                prev_hyp_words.append(hyp_word)
                buffer.set_hypothesis_words(prev_hyp_words)
            if type != G.ERROR_CODE['CHAIN']:
                type = G.ERROR_CODE['ONE TO MANY']
            h_id += 1

        elif contains(hyp_word.get_time_interval(), ref_word.get_time_interval()):
            if not buffer:
                buffer = ASRError(ref_word, hyp_word, None)
                type = G.ERROR_CODE['MANY TO ONE']
            else:
                prev_ref_words = buffer.get_reference_word_list()
                prev_ref_words.append(ref_word)
                buffer.set_reference_words(prev_ref_words)
            if type != G.ERROR_CODE['CHAIN']:
                type = G.ERROR_CODE['MANY TO ONE']
            r_id += 1

        else:  # Overlap
            if not buffer:
                buffer = ASRError(ref_word, hyp_word, None)
            else:
                if float(ref_word.get_time_interval()[1]) > float(hyp_word.get_time_interval()[1]):
                    h_id += 1
                else:
                    r_id += 1
                prev_hyp_words = buffer.get_hypothesis_word_list()
                prev_hyp_words.append(hyp_word)
                buffer.set_hypothesis_words(prev_hyp_words)
                prev_ref_words = buffer.get_reference_word_list()
                prev_ref_words.append(ref_word)
                buffer.set_reference_words(prev_ref_words)

            type = G.ERROR_CODE['CHAIN']

    return postprocessing_one_to_one_errors(errors, celex)
