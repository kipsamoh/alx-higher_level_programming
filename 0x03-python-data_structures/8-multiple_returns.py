#!/usr/bin/python3
def multiple_returns(sentence):
    length_sent = len(sentence)

    if (length_sent == 0):
        new_tuple = (length_sent, None)
    else:
        new_tuple = (length_sent, sentence[0])

    return (new_tuple)
