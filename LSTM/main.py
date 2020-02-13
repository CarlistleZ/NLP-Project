import numpy as np


def init_mat():
    dict = {}
    dict[0] = 'zeroelt'
    dict[1] = 'oov'
    counter = 2

    f = open("./../atis.train", "r")
    res = []
    sentence = []
    sentence_num = 0
    for x in f:
        if x != '\t\n':
            word = x.split('\t')[0]
            sentence.append(word)
            if word not in dict:
                dict[counter] = word
                counter += 1
        else:
            res.append(sentence)
            sentence = []
            sentence_num += 1
    res = np.asmatrix(res)
    return res, dict


def launch_clf():
    # opti = Adam()
    #
    # hiddensize = 0.3
    # dropout_val = 0.5
    # nblabels = 10000

    my_matrix, my_dict = init_mat()

    # input = Input(shape=(4978*86),my_matrix)
    # layer = Dense(hiddensize,activation='relu')(input)
    # layer = Dropout(dropout_val)(layer)
    # out = Dense(nblabels,activation='softmax')(layer)
    #
    # model = Model(inputs=input, outputs=out)
    # model.compile(loss='sparse_categorical_crossentropy',
    #               optimizer = opti, metrics = ['accuracy'])
    #
    # # Y_train: output (labels vector, coded as numbers [0,nblabels])
    # model.fit(X_train, Y_train, nb_epoch=20, batch_size=32)
    # predictions = model.predict(X_test).argmax(−1)
    # print classification_report(Y_test, predictions)
    return my_matrix, my_dict


if __name__ == '__main__':
    my_mat, my_dict = launch_clf()
    print(my_dict)
    for x in my_mat:
        print(x)
