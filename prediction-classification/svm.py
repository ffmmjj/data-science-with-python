#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=========================================================
SVM Classification
=========================================================

The first plot displays the iris classification training data.
The second one shows the predictions given a new dataset.

If you don't see anything, try Alt+Tab or Cmd+Tab to switch to the plot window.

Close all plot windows to finish the program.

"""
print(__doc__)

import numpy as np

import matplotlib
matplotlib.use('Qt4Agg')

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn import svm
from sklearn import datasets

def plotIrisData(figureNumber, X, y):
	plt.figure(figureNumber, figsize=(8, 6))
	plt.clf()

	plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
	plt.xlabel('Sepal length')
	plt.ylabel('Sepal width')

	plt.xlim(x_min, x_max)
	plt.ylim(y_min, y_max)
	plt.xticks(())
	plt.yticks(())

iris = datasets.load_iris()

X = iris.data[:, :2]  # We only take the first two features.
Y = iris.target

# Calculate min and max values for the axes.
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

# Plot training points.
plotIrisData(1, X, Y)

svc = svm.SVC(kernel='linear')

# Train the model.
svc.fit(X, Y) 

newData = np.array([[4, 2],[6,3],[7,3.5],[3,4],[5,2.5],[5,4],[5,2]])
prediction = svc.predict(newData)

# Plot predicted points.
plotIrisData(2, newData, prediction)

plt.show()