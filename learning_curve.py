""" Exploring learning curves for classification of handwritten digits """

import matplotlib.pyplot as plt
import numpy
from sklearn.datasets import *
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression


def display_digits():
    print("display")
    digits = load_digits()
    # print(digits.DESCR)
    fig = plt.figure()
    for i in range(10):
        subplot = fig.add_subplot(5, 2, i+1)
        subplot.matshow(numpy.reshape(digits.data[i], (8, 8)), cmap='gray')

    plt.show()


def train_model():
    # train models with training percentages between 5 and 90 (see
    # train_percentages) and evaluate the resultant accuracy for each.
    # You should repeat each training percentage num_trials times to smooth out
    # variability.
    # For consistency with the previous example use
    # model = LogisticRegression(C=10**-10) for your learner
    print("training")
    data = load_digits()
    num_trials = 2000
    train_percentages = range(5, 95, 5)
    length = len(train_percentages)
    test_accuracies = numpy.zeros(length)

    for i in range(length):
        total = 0
        for j in range(num_trials):
            size = train_percentages[i]
            x_train, x_test, y_train, y_test = train_test_split(data.data,
                                                                data.target,
                                                                train_size=size)
            model = LogisticRegression(C=10**-20)
            model.fit(x_train, y_train)
            total += model.score(x_test, y_test)
        test_accuracies[i] = total/num_trials

    fig = plt.figure()
    plt.plot(train_percentages, test_accuracies)
    plt.xlabel('Percentage of Data Used for Training')
    plt.ylabel('Accuracy on Test Set')
    plt.show()


if __name__ == "__main__":
    # Feel free to comment/uncomment as needed
    display_digits()
    train_model()
