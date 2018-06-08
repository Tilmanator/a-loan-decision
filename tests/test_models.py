from context import models


def test__get_nn():
    models.get_nn_model(5)


def test_get_rf():
    models.get_random_forest_model()