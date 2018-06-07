# ML modules
from sklearn.ensemble import RandomForestClassifier
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import accuracy_score

from data import data
import math

all_X,all_Y, column_names = data.get_data(get_feature_names=True)
input_dim = len(all_X[0])

# Create Keras model, two classes as output (no need for one-hot)
model = Sequential()
model.add(Dense(10, input_dim=input_dim, kernel_initializer='uniform', activation='relu'))
model.add(Dense(6, kernel_initializer='uniform', activation='relu'))
model.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))

# Compile model, we are choosing between two classes
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])

n_train = 1000
X = all_X[:n_train]
Y = all_Y[:n_train]
# Fit the model
model.fit(X, Y, epochs=50, batch_size=10,  verbose=2)

# Get some samples to test our model on
test_set_range = (10000, 20000)
x_test = all_X[test_set_range[0]:test_set_range[1]]
y_test = all_Y[test_set_range[0]:test_set_range[1]]

# Calculate predictions
nn_predictions = model.predict(x_test)

# Change to 0/1 predictions and get accuracy
nn_predictions = map(lambda x: int(round(x)) if not math.isnan(x) else 0, nn_predictions)
print "\nNeural Network Accuracy: %.4f%%" % (accuracy_score(y_test, nn_predictions))

clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(X, Y.reshape(n_train,))
rf_predictions = clf.predict(x_test)

print "Random Forest Accuracy: %.4f%%\n" % (accuracy_score(y_test, rf_predictions))

# print "Random Forest Feature importance:"
# for i in zip(column_names, clf.feature_importances_):
#     print "%s importance: %.2f" % i