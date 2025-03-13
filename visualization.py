import matplotlib.pyplot as plt
import numpy as np

def showFigure(data_list):
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    features = ["gender","race/ethnicity","parental level of education","test preparation course"]
    subject =  "math"
    for i in range(0,2):
        for j in range(0,2):
            feature = features[i*2+j]
            categories = list(set([data[feature] for data in data_list]))
            x2 = np.arange(len(categories))

            pasedList = [sum(1 for data in data_list if data[feature] == category and int(data[subject+" score"]) > 60) for category in categories]
            failedList = [sum(1 for data in data_list if data[feature] == category) - pasedList[index] for index, category in enumerate(categories)]
            axes[i, j].bar(categories, pasedList, color='g')
            axes[i, j].bar(categories, failedList, bottom=pasedList, color='r')
            axes[i, j].set_title(feature.capitalize())
            axes[i, j].set_xticks(x2)
            axes[i, j].set_xticklabels(categories)

    plt.show()