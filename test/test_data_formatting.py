from data import data
import models


def test_format_title_simple():
    assert data.format_title('asdas') == 'asdas'


def test_format_title_keyword1():
    assert data.format_title('Business Loan') == 'Business'


def test_format_title_keyword2():
    assert data.format_title('other') == 'Other'


def test_parse_employment_length_simple():
    assert data.parse_employment_length('Noise++--8yearsmonthsdays') == 0.8


def test_parse_employment_length_special():
    assert data.parse_employment_length('< 1 year') == 0.05


def test_format_dti():
    assert data.format_dti('100%') == 1


def test_format_dti_string():
    assert data.format_dti('100%') == 1


def test_format_dti_num():
    assert data.format_dti(67.0) == 0.67


def test_catch_nan_number():
    assert data.not_nan(56)


def test_catch_nan_invalid():
    assert not data.not_nan(float('nan'))