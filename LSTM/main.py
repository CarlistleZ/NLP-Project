import numpy as np
from keras import Input, Model
from keras.layers import Embedding, LSTM, Dropout, TimeDistributed, Dense


def init_mat(file):
    di = {'': 0, 'oov': 1}
    f = open(file, "r")
    res = []
    sentence = []
    for line in f:
        if line != '\t\n':
            word = line.split('\t')[0]
            if word not in di:
                di[word] = len(di)
            sentence.append(di[word])
        else:
            while len(sentence) != 86:
                sentence.append(0)
            res.append(sentence)
            sentence = []

    mat_tags = []
    line_tags = []
    dict_tags = {}
    f = open(file, "r")
    for line in f:
        if line != '\t\n':
            tag = line.split('\t')[1]
            if tag not in dict_tags:
                dict_tags[tag] = len(dict_tags)
            line_tags.append(dict_tags[tag])
        else:
            while len(line_tags) != 86:
                line_tags.append(0)
            mat_tags.append(line_tags)
            line_tags = []

    res = np.asmatrix(res)
    mat_tags = np.asmatrix(mat_tags)
    mat_tags = np.expand_dims(mat_tags, axis=2)  # Embedding will produce the 3rd dim
    return res, mat_tags, di, dict_tags


def launch_clf(input_matrix, tag_matrix):
    max_seq_size = 86
    nb_labels = 5000

    entree = Input(shape=(max_seq_size,), dtype='int32')
    emb = Embedding(len(tag_matrix), 100)(entree)
    bi = LSTM(100, return_sequences=True)(emb)
    # bi = Bidirectional(LSTM(config.hidden, return_sequences=True))(emb)
    drop = Dropout(0.5)(bi)
    out = TimeDistributed(Dense(units=nb_labels, activation='softmax'))(drop)

    model = Model(inputs=entree, outputs=out)
    model.compile(loss="sparse_categorical_crossentropy", optimizer="adam")
    # or use loss sparse_categorical_crossentropy
    model.fit(input_matrix, tag_matrix, batch_size=64, epochs=5)
    res = model.predict(input_matrix).argmax(-1)
    return res


def print_mat(m):
    print('shape: ', m.shape)
    for x in range(m.shape[0]):
        s = ''
        for y in range(m.shape[1]):
            s += '\'' + m[x, y] + '\','
        print(s)


if __name__ == '__main__':
    my_mat, tags_mat, my_dict, tags_dict = init_mat('./../atis.train')
    # print(my_dict)
    # print_mat(my_mat)
    result = launch_clf(my_mat, tags_mat)
    print_mat(result)
