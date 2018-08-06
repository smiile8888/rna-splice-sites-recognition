import csv


def get_sequences(file_name, class_label):
    """
    To get sequences from file and put class label each sequence
    :param file_name:
    :param class_label:
    :return:
    """
    with open(file_name) as data:
        data = data.readlines()
        sequences = [[data[i].replace('\n', ''), class_label] for i in range(len(data)) if i%2 == 1]
    return sequences


def write_preprocess_data(file_name, data):
    """
    To write all sequences with their classes to file
    :param file_name:
    :param data:
    :return:
    """
    with open(file_name, 'w', newline='\n') as preprocessFile:
        writer = csv.writer(preprocessFile, delimiter=',')
        writer.writerow(['Seq', 'Class'])
        for line in data:
            writer.writerow(line)


def transform_seq_to_Vmatrix(sequence):
    """
    To transform a sequence to binary matrix of Xx4
    :param sequence:
    :return:
    """
    m = []
    for x in sequence:
        if x == 'A':
            m.append([1, 0, 0, 0])
        if x == 'C':
            m.append([0, 1, 0, 0])
        if x == 'T':
            m.append([0, 0, 1, 0])
        if x == 'G':
            m.append([0, 0, 0, 1])
    return m


def transform_seq_to_Hmatrix(sequence):
    """
    To transform a sequence to binary matrix of 4xX
    :param sequence:
    :return:
    """
    m = []
    a = [1 if x == 'A' else 0 for x in sequence]
    c = [1 if x == 'C' else 0 for x in sequence]
    g = [1 if x == 'G' else 0 for x in sequence]
    t = [1 if x == 'T' else 0 for x in sequence]
    m.append(a)
    m.append(c)
    m.append(g)
    m.append(t)
    return m

