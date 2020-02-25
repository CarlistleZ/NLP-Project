import numpy as np
from keras import Input
from keras.layers import Embedding, LSTM, Dropout, TimeDistributed, Dense


def init_mat(file):
    di = {0: '', 1: 'oov'}
    f = open(file, "r")
    res = []
    sentence = []
    for line in f:
        if line != '\t\n':
            word = line.split('\t')[0]
            sentence.append(word)
            if word not in di.values():
                di[len(di)] = word
        else:
            while len(sentence) != 86:
                sentence.append('')
            res.append(sentence)
            sentence = []
    res = np.asmatrix(res)
    # res = np.expand_dims(res, axis=2)  # Embedding will produce the 3rd dim
    return res, di


def launch_clf(input_matrix, input_dict):
    max_seq_size = 86
    nbexamples = 4978
    X = input_matrix
    nb_labels = 5000

    entree = Input(shape=(max_seq_size,), dtype='int32')
    emb = Embedding(len(input_dict), 100)(entree)
    config = emb.get_config()   # raise an exception here
    bi = LSTM(config.hidden, return_sequences=True)(emb)
    # bi = Bidirectional(LSTM(config.hidden, return_sequences=True))(emb)
    drop = Dropout(0.5)(bi)
    out = TimeDistributed(Dense(units=nb_labels, activation='softmax'))(drop)
    # Y=(nbexamples∗MAX_SEQ_SIZE∗1)

    return out


def print_mat(m):
    print('shape: ', m.shape)
    for x in range(m.shape[0]):
        s = ''
        for y in range(m.shape[1]):
            s += '\'' + m[x, y] + '\','
        print(s)


if __name__ == '__main__':
    my_mat, my_dict = init_mat('./../atis.train')
    print(my_dict)
    # print_mat(my_mat)
    # result = launch_clf(my_mat, my_dict)
    # print(result)
