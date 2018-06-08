# ML modules
from sklearn.ensemble import RandomForestClassifier
from keras.models import Sequential
from keras.layers import Dense


def get_nn_model(input_dim):
    # Create Keras model, two classes as output (no need for one-hot)
    model = Sequential()
    model.add(Dense(10, input_dim=input_dim, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(6, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))

    # Compile model, we are choosing between two classes
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
    return model


def get_random_forest_model():
    clf = RandomForestClassifier(n_estimators=10)
    return clf
