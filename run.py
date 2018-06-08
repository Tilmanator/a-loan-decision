from data import data
import models
import math
from sklearn.metrics import accuracy_score
import argparse


def main(args):
    all_X, all_Y, column_names = data.get_data(get_feature_names=True)
    input_dim = len(all_X[0])

    nn = models.get_nn_model(input_dim)
    rf = models.get_random_forest_model()

    n_train = 1000
    X = all_X[:n_train]
    Y = all_Y[:n_train]
    # Fit the model
    nn.fit(X, Y, epochs=50, batch_size=10, verbose=2)

    # Get some samples to test our model on
    test_set_range = (10000, 20000)
    x_test = all_X[test_set_range[0]:test_set_range[1]]
    y_test = all_Y[test_set_range[0]:test_set_range[1]]

    # Calculate predictions
    nn_predictions = nn.predict(x_test)

    # Change to 0/1 predictions and get accuracy
    nn_predictions = map(lambda x: int(round(x)) if not math.isnan(x) else 0, nn_predictions)
    print "\nNeural Network Accuracy: %.4f%%" % (accuracy_score(y_test, nn_predictions))

    rf = rf.fit(X, Y.reshape(n_train, ))
    rf_predictions = rf.predict(x_test)

    print "Random Forest Accuracy: %.4f%%" % (accuracy_score(y_test, rf_predictions))

    if args.feature_importance:
        print "\nRandom Forest Feature importance:"
        for i in zip(column_names, rf.feature_importances_):
            print "%s importance: %.2f" % i


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Learn about loans!")
    parser.add_argument('--feature-importance', '-fi', action='store_true')
    args, leftover = parser.parse_known_args()
    main(args)