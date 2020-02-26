import numpy as np
from keras import Input, Model
from keras.engine.saving import load_model
from keras.layers import Embedding, LSTM, Dropout, TimeDistributed, Dense
from sklearn.model_selection import train_test_split


# import tensorflow as tf
# configT = tf.ConfigProto()
# configT.gpu_options.allow_growth = True
# session = tf.Session()


def init_mat(file):
    # Generate word matrix
    dict_words = {'': 0, 'oov': 1}
    mat_words = []
    sentence = []
    f = open(file, "r")
    for line in f:
        if line != '\t\n':
            word = line.split('\t')[0]
            if word not in dict_words:
                dict_words[word] = len(dict_words)
            sentence.append(dict_words[word])
        else:
            while len(sentence) != 86:
                sentence.append(0)
            mat_words.append(sentence)
            sentence = []

    # Generate tag matrix
    mat_tags = []
    line_tags = []
    dict_tags = {}
    f = open(file, "r")
    for line in f:
        if line != '\t\n':
            tag = line.split('\t')[1].rstrip()
            if tag not in dict_tags:
                dict_tags[tag] = len(dict_tags)
            line_tags.append(dict_tags[tag])
        else:
            while len(line_tags) != 86:
                line_tags.append(0)
            mat_tags.append(line_tags)
            line_tags = []
    # Convert to numpy matrix
    mat_words = np.asmatrix(mat_words)
    mat_tags = np.asmatrix(mat_tags)
    mat_tags = np.expand_dims(mat_tags, axis=2)  # Embedding will produce the 3rd dim

    inv_word_dict = {}
    for elt in dict_words:
        inv_word_dict[dict_words[elt]] = elt
    inv_tags_dict = {}
    for elt in dict_tags:
        inv_tags_dict[dict_tags[elt]] = elt
    return mat_words, mat_tags, inv_word_dict, inv_tags_dict


def launch_clf(input_matrix, tag_matrix):
    X_train, X_test, y_train, y_test = train_test_split(input_matrix, tag_matrix, test_size=0.33)

    max_seq_size = 86
    nb_labels = 5000
    entree = Input(shape=(max_seq_size,), dtype='int32')
    emb = Embedding(len(tag_matrix), 100)(entree)
    bi = LSTM(100, return_sequences=True)(emb)
    # bi = Bidirectional(LSTM(config.hidden, return_sequences=True))(emb)
    drop = Dropout(0.5)(bi)
    out = TimeDistributed(Dense(units=nb_labels, activation='softmax'))(drop)

    # model = Model(inputs=entree, outputs=out)
    # model.compile(loss="sparse_categorical_crossentropy", optimizer="adam")
    # # or use loss categorical_crossentropy
    # model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size=16, epochs=40)
    # model.save('./results/model.h5')
    model = load_model('./results/20/model_20_0.061.h5')

    res = model.predict(X_test).argmax(-1)
    ev = model.evaluate(res, y_test, batch_size=64)

    return ev, res, y_test, X_test


def generate_res(produced, ref, inv_tags_dict, word_dict, X_test):
    f = open("./results/res.txt", "a")
    for i in range(produced.shape[0]):
        for j in range(produced.shape[1]):
            if produced[i, j] != 2622:
                produced_tag = inv_tags_dict[produced[i, j]]
            else:
                produced_tag = inv_tags_dict[0]
            ref_tag = inv_tags_dict[ref[i, j, 0]]
            wd = word_dict[X_test[i, j]]
            # if produced_tag != 'O' and ref_tag != 'O':
            f.write(wd + ' ' + ref_tag + ' ' + produced_tag + '\n')
        f.write('\n')
    # f.write("Now the file has more content!")
    f.close()


if __name__ == '__main__':
    word_mat, tags_mat, word_dict, tags_dict = init_mat('../atis.train')
    # print(tags_dict)
    # print(word_dict)
    # reconstruct_words(word_mat, word_dict)
    # reconstruct_tags(tags_mat, tags_dict)
    ev, produced, ref, X_test = launch_clf(word_mat, tags_mat)
    print('Accuracy: ', ev)
    generate_res(produced, ref, tags_dict, word_dict, X_test)


'''
def reconstruct_words(word_mat, word_dict):
    inv_word_dict = {}
    for elt in word_dict:
        inv_word_dict[word_dict[elt]] = elt
    for x in range(word_mat.shape[0]):
        for y in range(word_mat.shape[1]):
            if word_mat[x, y] != 0:
                print(word_mat[x, y], '->', inv_word_dict[word_mat[x, y]])
        print()


def reconstruct_tags(tags_mat, tags_dict):
    inv_tags_dict = {}
    for elt in tags_dict:
        inv_tags_dict[tags_dict[elt]] = elt
    for x in range(tags_mat.shape[0]):
        for y in range(tags_mat.shape[1]):
            # if tags_mat[x, y][0] != 0:
            print(tags_mat[x, y][0], '->', inv_tags_dict[tags_mat[x, y][0]])
        print()


def print_mat(m):
    print('shape: ', m.shape)
    for x in range(m.shape[0]):
        s = ''
        for y in range(m.shape[1]):
            s += '\'' + m[x, y] + '\','
        print(s)
'''
