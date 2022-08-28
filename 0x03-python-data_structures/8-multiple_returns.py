#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    if str_len != 0:
        str_fir_char = sentence[0]
    else:
        str_fir_char = None
    sentence_tuple = (str_len, str_fir_char)
    return sentence_tuple
