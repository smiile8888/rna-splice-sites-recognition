import numpy as np


def calculate_mutation_score(ref_seq_score, alt_seq_score):
    """
    To calculate mutation score between reference sequence and alternative sequence
    :param ref_seq_score:
    :param alt_seq_score:
    :return:
    """
    return np.log10(ref_seq_score/alt_seq_score)